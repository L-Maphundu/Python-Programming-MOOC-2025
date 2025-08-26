# Write your solution here
password = input("Password: ")
while True:
    check = input("Repeat password: ")
    if check == password:
        print("User account created!")
        break
    else:
        print("They do not match!")
    
