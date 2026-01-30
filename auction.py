img = '''
                                                                      
                                          88                          
                                    ,d    ""                          
                                    88                                
,adPPYYba, 88       88  ,adPPYba, MM88MMM 88  ,adPPYba,  8b,dPPYba,   
""     `Y8 88       88 a8"     ""   88    88 a8"     "8a 88P'   `"8a  
,adPPPPP88 88       88 8b           88    88 8b       d8 88       88  
88,    ,88 "8a,   ,a88 "8a,   ,aa   88,   88 "8a,   ,a8" 88       88  
`"8bbdP"Y8  `"YbbdP'Y8  `"Ybbd8"'   "Y888 88  `"YbbdP"'  88       88  
                                                                      
                                                                      
'''

print(img)
print("Welcome to the auction game!")

bidders = {}
is_bidder = True

def find_best_bidder(bidding_dictionary):
    winner_name = ""
    winner_bid = 0

    for bidder_name in bidding_dictionary:
        if bidding_dictionary[bidder_name] > winner_bid:
            winner_name = bidder_name
            winner_bid = bidders[bidder_name]
    return winner_name

while is_bidder:
    user_name = input("What's your name?")

    while user_name in bidders:
        user_name = input("This username is busy. Give another username!")

    user_bid = int(input("What's your bid? $"))

    while user_bid <= 0:
        user_bid = int(input("The bid is too low. Please provide a higher value. $"))

    bidders[user_name] = user_bid

    are_other_bidders = ''

    while are_other_bidders != 'yes' and are_other_bidders != 'no':
        are_other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

    if are_other_bidders == "no":
        is_bidder = False

        winner = find_best_bidder(bidders)

        print(f"The winner is {winner} with a bid of ${bidders[winner]}")



