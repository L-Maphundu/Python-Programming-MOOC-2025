# Write your solution here
name = input("Please type in your name: ").lower()

if name == "huey" or name == "dewey" or name == "louie":
    print("I think you might be one of Donald Duck's nephews")
elif name == "morty" or name == "ferdie":
    print("I think you might be one of Mickey Mouse's nephews")
else:
    print("You're not a nephew of any character I know of.")