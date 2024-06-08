from datetime import datetime

def greet_user():
    current_time = datetime.now()
    current_hour = current_time.hour

    name = input("What's your name? ")

    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(f"{greeting}, {name}!")

greet_user()
