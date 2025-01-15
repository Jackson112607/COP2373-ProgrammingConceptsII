# This program pre-sells a limited number of movie tickets to buyers. Each buyer can buy up to 4 tickets and a
# maximum of 20 tickets can be sold. The user will be asked how many tickets to buy. After selecting the amount
# of tickets, the amount of remaining tickets will be displayed, until all tickets have been sold.

# Initialize global variables.
remaining_tickets = 20
total_buyers = 0

# get_user_tickets function asks the user how many tickets they would like to buy.
def get_user_tickets():
    while True:
        try:
            user_tickets = int(input('How many tickets would you like to purchase? Enter a number 1-4. '))
            if user_tickets < 0 or user_tickets > 4:
                print('Please enter a number 1-4.') # If the input does not satisfy the integer requirement.
            else:
                return user_tickets # Sends value to sell_tickets function.
        except ValueError:
            print('Invalid input. Enter a number.') # If the input does not satisfy the integer requirement.

# sell_tickets function loops the question to buy tickets until there are no more tickets available.
def sell_tickets(remaining_tickets, total_buyers):
    while remaining_tickets > 0:
        print(f'Remaining tickets: {remaining_tickets}') # Shows the user how many tickets are available for purchase.
        tickets_to_buy = get_user_tickets()
        if tickets_to_buy > remaining_tickets:
            print('Not enough tickets available.') # If the user enters a number that is greater than the number of tickets available.
        else:
            remaining_tickets -= tickets_to_buy
            total_buyers += 1
    return remaining_tickets, total_buyers

# Assigns values to variables and calls the sells_tickets function to loop and accumulate the number of remaining tickets and the number of total buyers.
remaining_tickets, total_buyers = sell_tickets(remaining_tickets, total_buyers)

# Displaying the result.
print('\n' + 'All tickets have been sold! No more are available.')
print(f'The total number of buyers is {total_buyers}.')