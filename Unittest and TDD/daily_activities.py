def work(hour):
    if hour >= 8 and hour < 16:
        return True
    return False

def can_take_nap(hour):
    if hour > 15 and hour < 20:
       return "Ok, I can take a nap."
    return "I will not nap at this time, have other things to do."

