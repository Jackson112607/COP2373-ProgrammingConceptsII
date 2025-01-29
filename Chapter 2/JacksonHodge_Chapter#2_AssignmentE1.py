# This program asks the user to enter an email message. It will then scan the message to see the likelihood for it to be
# spam. The program will output a "spam score" and found spam words.

# spam_dictionary() creates a dictionary of common spam words found in emails.
def spam_dictionary():
    spam_dict = {
        "free",
        "price",
        "cash",
        "money",
        "earn",
        "bonus",
        "winner",
        "customer",
        "account",
        "username",
        "confirm",
        "subscription",
        "make money",
        "now",
        "congratulations",
        "no hidden fees",
        "billing",
        "deal",
        "discount",
        "join millions",
        "offer",
        "quote",
        "rate",
        "trial",
        "free trial",
        "opt in",
        "social security number",
        "guaranteed",
        "credit card",
        "debit card",
    }
    return spam_dict

# calc_spam_score() calculates the spam score of the email.
def calc_spam_score(user_email, spam_dict):
    spam_score = 0 # Initialize variable to count the email's spam score.
    spam_words = [] # Creates a list to store the spam words from the email.
    # for loop to find spam words, add to score, and add to list.
    for spamWord in spam_dict:
        if spamWord in user_email.lower():   # Takes the user's email and makes everything lowercase.
            spam_score += 1
            spam_words.append(spamWord)
    return spam_score, spam_words

# main() gets user input and displays the output.
def main():
    spam_dict = spam_dictionary() # Call spam_dictionary()
    user_email = input('Enter email message for spam evaluation: ') # Get input from user.
    # Call calc_spam_score().
    spam_score, spam_words = calc_spam_score(user_email, spam_dict)
    # If statement determines the likelihood of the message being spam.
    if spam_score == 0:
        spam_possibility = "Not likely spam."
    elif spam_score <= 3:
        spam_possibility = "Possibly spam."
    elif spam_score <= 5:
        spam_possibility = "Likely spam."
    else:
        spam_possibility = "Highly likely spam."
    # Display the result.
    print('Spam evaluation of your email:')
    print(f"Spam score: {spam_score}")
    print(f'Likelihood of spam: {spam_possibility}')
    print(f'Found spam words/phrases: {spam_words}')

# Call main().
main()