number = int(input("Type here integer number from 0 to 10: "))

while True:
 
    if number <= 10:

        print("Is correct number: ", number) 

        sqr = number ** 2

        print("The correct number is squared: ", sqr)
   
        break
  
    elif number > 10:

        number = int(input("Number not correct, try again (from 0 to 10): "))  
    
    continue
