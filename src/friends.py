def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, snack):
    for food in person["favourites"]["snacks"]:
        if snack == food:
            return True
    
    return False

