#while True:

fname = str(input("Enter name:"))
lname = str(input("Enter Last name:"))


old = int(input("Enter age:"))
weight = int(input("Enter weight:"))

if fname == str("") or lname == str("") or old == "" or weight == "":

    print("Need to enter all values! Try again.")

#        break

elif old <= 30 and weight >= 50 and weight < 120:

    print(fname, lname, old,"age,", "weight", weight, "- Your health is good.")

elif old > 30 and weight < 50 or weight > 120:

    print(fname, lname, old,"age,", "weight", weight, "- You need to monitor your health.")

elif old > 40 and weight < 50 or weight > 120:

    print(fname, lname, old,"age,", "weight", weight, "- You should see a doctor.")

elif old > 30 and weight > 40 and weight < 120:

    print(fname, lname, old,"age,", "weight", weight, "- Your health is good.")
