name = input("What is your name ?")
print("Hello", name)

if name == "Hetal":
    res = input("You are a passionate developer right ?")
    print("Your answer is : ", res)
else:
    print("Nice to see you")

age = int(input("What is your age ?"))
print("You are", age, "years old")

if age < 18:
    print("You are a minor")
else:
    print("You are an adult")

height = float(input("What is your height ?"))
print("You are", height, "feet tall")

if height < 5.5:
    print("You are short")
else:
    print("You are tall")

weight = float(input("What is your weight in kg ?"))
print("You weigh", weight, "kg")

if weight < 50:
    print("You are underweight")
elif weight < 100:
    print("You have a healthy weight")
else:
    print("You are overweight")

print("Thank you for sharing your details, " + name + "!")
print("Have a great day ahead!")

