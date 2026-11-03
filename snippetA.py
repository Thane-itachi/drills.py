# x = input("Type a number: ")
# print(type(x))
# print(x + 1)



# x = int(input("Type a number: "))
# print(type(x))
# print(x + 1)


# nickname = input("Nickname: ")
# print(f"Welcome, {nickname}")



# score = 0
# print(score)
# score = score + 10
# print(score)


# a = "5"
# b = 5
# c = True 
# print(type(a))
# print(type(b))
# print(type(c))
# print("5" + "5")
# print(5 + 5)




# The critical idea: == compares both value and type

# This is where the Mystery Island bug lives. Read these carefully:

# print(1 == 1)        # True   — int vs int
# print("1" == 1)      # False  — str vs int, NO conversion happens
# print("1" == "1")    # True   — str vs str
# print(1 == True)     # True   — because True is 1 in Python (surprising!)
# print(0 == False)    # True   — because False is 0

# Line 2 is the whole point: "1" == 1 is False. Python does not convert. A string and an integer are simply different things, and == reports that honestly.


# Why this breaks the game

# Your menu will look like this:

# choice = input("> ")        # player types 1
# if choice == 1:             # ❌ "1" == 1 → False, ALWAYS
#     print("You go north.")
# elif choice == 2:
#     print("You go south.")
# else:
#     print("Invalid choice.")





choice = input("> ")
if choice == "1":
    print("You go north.")
elif choice == 2:
    print("You go south.")
else:
    print("Invalid choice.")     