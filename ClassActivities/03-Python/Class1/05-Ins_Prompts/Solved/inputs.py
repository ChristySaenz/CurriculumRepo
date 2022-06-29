# Collects the user's input for the prompt "What is your name?"
name = input("What is your name? ")
print(type(name))
# Collects the user's input for the prompt "How old are you?" and converts the string to an integer.
age = int(input("How old are you? "))
print(type(age))
# Collects the user's input for the prompt "Is input truthy?" and converts it to a boolean. Note that non-zero,
#   non-empty objects are truth-y.
trueOrFalse = bool(input("Is the input truthy? "))
print(type(trueOrFalse))
# Creates three print statements that to respond with the output.
print("My name is " + str(name))
print("I will be " + str(age + 1) + " next year.")
print("The input was converted to " + str(trueOrFalse))
