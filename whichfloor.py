maximum_stories = 5
usernum = input("What floor do u work on?")
usernum = int(userstring)

while usernum > maximum_stories:
print(usernum + "there are only 5 floors please enter a valid number")
userstring = prompt("Please input the floor number again")
usernum = int(userstring)
}
print("Congradulations you work on" + usernum)
