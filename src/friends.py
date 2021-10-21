def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, snack):
    for food in person["favourites"]["snacks"]:
        if snack == food:
            return True
    
    return False

def add_friend(person, new_friend):
    person["friends"].append(new_friend)
    print(len(person["friends"]))

def remove_friend(person, old_friend):
    person["friends"].remove(old_friend)
    print(len(person["friends"]))

def total_money(person):
    total_cash = 0
    for cash in person:
        total_cash += cash["monies"]
        
    return total_cash

def l_money(loaner, loanee, loan_amount):
    loaner["monies"] -= loan_amount
    loanee["monies"] += loan_amount
    print(loaner["monies"])
    print(loanee["monies"])

