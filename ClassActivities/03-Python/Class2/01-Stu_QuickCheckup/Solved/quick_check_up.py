# Print Hello User!
print("Hello User!")

# Take in User Input
name = input("What is your name? ")

# Respond Back with User Input
print("Hi " + name + "!")

# Take in the User Favorite Number
fave = input("What is your favorite number? ")

# Respond Back with a statement based on your favorite number
if (int(fave) < 7):
    print("Your favorite number is lower than mine.")

if (int(fave) == 7):
    print("Your favorite number is the same as mine!")

if (int(fave) > 7):
    print("Your favorite number is higher than mine.")
