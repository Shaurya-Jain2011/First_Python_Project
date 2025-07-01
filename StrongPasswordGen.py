from pprint import pprint
import random
import string


def StrengthLogic():
# Asking for user's password
    UserPassword = input("Enter your password here: ")

    point = 0
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    SpecialChar = ['!','@','#','$','%','^','&','*']
    suggestions = []

    # Length logic
    if len(UserPassword) >= 8:
        point += 1
    else:
        suggestions.append("It is easier to hack a shorter password, so use at least 8 characters.")

    # Lowercase logic
    if any(i.islower() for i in UserPassword):
        point += 1
    else:
        suggestions.append("Include at least one lowercase letter.")

    # Uppercase logic
    if any(i.isupper() for i in UserPassword):
        point += 1
    else:
        suggestions.append("Include at least one uppercase letter.")

    # Numeric logic
    if any(i in numbers for i in UserPassword):
        point += 1
    else:
        suggestions.append("Include at least one number.")

    # Special character logic
    if any(i in SpecialChar for i in UserPassword):
        point += 1
    else:
        suggestions.append("Include at least one special character (!, @, #, $, %, ^, &, *).")

    # Password strength
    print("\nStrength Result:")
    if point == 5:
        print(f"Strength: Strong\nStrength Points: {point}")
    elif 3 <= point < 5:
        print(f"Strength: Medium\nStrength Points: {point}")
    elif point == 2:
        print(f"Strength: Weak\nStrength Points: {point}")
    elif point == 1:
        print(f"Strength: Very Weak\nStrength Points: {point}")
    else:
        print(f"Strength: Extremely Weak\nStrength Points: {point}")

    # Suggestions if any
    if len(suggestions) != 0:
        print("\nSuggestions:")
        for i in suggestions:
            print(f"-->\t{i}")


# Strong Password Generator
def PasswordGen():
    answer = input("\nDo you want a strong random password? (y/n): ").lower()
    if answer != 'y':
        return

    SpecialChar = ['!','@','#','$','%','^','&','*']
    RandomPassword = [random.choice(string.ascii_letters) for _ in range(8)]

    # Choose 3 different unique indexes using random.sample
    RandomUpper, RandomNum, RandomSpecialChar = random.sample(range(8), 3)

    # Apply rules
    RandomPassword[RandomUpper] = RandomPassword[RandomUpper].upper()
    RandomPassword[RandomNum] = str(random.randint(0, 9))
    RandomPassword[RandomSpecialChar] = random.choice(SpecialChar)

    finalPassword = ''.join(str(c) for c in RandomPassword)
    print("\nGenerated Strong Password:", finalPassword)

while True:
# Run generator
    # PasswordGen()

# Run strength logic

    StrengthLogic()