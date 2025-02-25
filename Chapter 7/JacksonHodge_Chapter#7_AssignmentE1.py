# This program allows the user to enter a paragraph, including sentences with numbers.
# The program will then display each individual sentence and the count of sentences in the paragraph.

# Import the re method.
import re

# split_into_sentences(paragraph) takes the input from the user and splits up each sentence in the paragraph.
def split_into_sentences(paragraph):
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)(?=\s|$)", paragraph)
    cleaned_sentences = [s.strip() for s in sentences if s.strip()]
    return cleaned_sentences

# display_and_count(sentences) displays the output and counts the number of sentences in the paragraph.
def display_and_count(sentences):
    sentence_number = 1 # Initialize an accumulator.
    # for loop to count the number of sentences and display the result.
    print('')  # For creating space between the input and the output in the console.
    for sentence in sentences:
        print(f"Sentence {sentence_number}: {sentence}")
        sentence_number += 1
    print(f"\nTotal number of sentences: {len(sentences)}")

# main function receives input from the user and calls the other functions in the program.
def main():
    paragraph = input("Enter your paragraph:\n")
    sentences = split_into_sentences(paragraph)
    display_and_count(sentences)

# Call main() to run program.
main()