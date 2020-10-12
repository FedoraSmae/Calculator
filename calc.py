carry=input("Do you want to proceed? Enter True or False if so")
while carry == "True":
    print("1 for adding,2 for subtracting, 3 for timesing, 4 for devision")
    calc=input("Enter a value")
    if calc == "1":
                    numinit = int(input("Enter first number"))
                    numinit2 = int(input("Enter first number"))
                    answer = numinit + numinit2
                    print(answer)
                    carry=input("Enter True or False")
        

    elif calc == "2":
                      numinit = int(input("Enter first number"))
                      numinit2 = int(input("Enter first number"))
                      answer = numinit - numinit2
                      print(answer)
                      carry=input("Enter True or False")

    elif calc == "3":
                      numinit = int(input("Enter first number"))
                      numinit2 = int(input("Enter first number"))
                      answer = numinit * numinit2
                      print(answer)
                      carry=input("Enter True or False")


    elif calc == "4":
                      numinit = int(input("Enter first number"))
                      numinit2 = int(input("Enter first number"))
                      answer = numinit / numinit2
                      print(answer)
                      carry=input("Enter True or False")
    else:
        print("Invalid")
        carry=input("Enter True or False")
SystemExit()
    

            

    


                 
