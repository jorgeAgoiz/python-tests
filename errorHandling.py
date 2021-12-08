# Error Handling
adult = False

while adult == False:
    try:
        age = int(input("What is your age?: "))
        if age > 17:
            adult = True
            print("Thank You!!")
            break
        else:
            print("You must have 18 or more!!")
            continue
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter age higher than 0")
