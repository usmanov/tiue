from logo import logo
print(logo)

bidders = {"name":"","bid":1}

def new_bidder():
    new_name = input("What is your name?: ")
    new_bid = input("What is your bid?: ")
    return new_name,new_bid
