userstring = input("Give me a number thats greater than 100")
usernum = int(userstring)

while usernum < 100:
  print(str(usernum) + " is less than 100, Try again, I've got all day...")
  userstring = input(usernum + " is less than 100, Try again, I've got all day...")
  usernum = int(userstring)

print(usernum + " is greater than 100! Finally!")
