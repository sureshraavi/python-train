print("Interview by computer")
name = input("your name : ")
print(f"hello {name}")
age = input("your age : ")
favorite_color = input("your fav color : ")

second_person_name_etc = input()

# above is no an efficient way

# Below is an efficient way (using Tuples)


questions = (
    "Your name: ",
    "Your age: ",
    "Favourite color: ",
    "Pet's name: ",
)

answers = []
for question in questions:
    answers.append(input(question))

print(answers)

# in the above program, input is tuple, and output is list

# tuples are immutable
# If you're never gonna change something after creating it, then it should be a tuple (so that it cannot be changed even accidentally)