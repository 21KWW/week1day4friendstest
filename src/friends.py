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

def all_favourite_foods(people):
    all_snacks=[]
    for person in people:
        for snack in person["favourites"]["snacks"]:
            all_snacks.append(snack)
    
    return all_snacks

def find_no_friendends(people):
    no_friends=[]
    for person in people:
        if len(person["friends"]) == 0:
            no_friends.append(person)

    return no_friends
