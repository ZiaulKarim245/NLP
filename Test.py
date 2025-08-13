password = input("Enter a password: ")
len = len(password)
if len >= 8:
  if "AI"  in password:
    print("Strong Password")
  else:
    print("Weak Password")
else:
  print("Invalid Password")