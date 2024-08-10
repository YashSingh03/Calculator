# Made by Ujjwal tandon
# Summer vacation project on computer science
# Project name - Multipurpose calculator

#Main default function
def main():
    #instructions and welcome code
    print("\nMultipurpose calculator!")
    choice = input("Please input the code from 1-5 for operation:- \n"
        "1 - Standard \n"
        "2 - Temperature \n"
        "3 - length \n"
        "4 - Speed \n"
        "5 - Weight \n")
    
    #To choose between different operations eg- standard, temp, length etc...
    #This runs when standard mode is selected
    if choice == '1':
         while True:
            #Taking the operator from the user
            print("\nEnter opertor +, -, ⨉, ÷")
            user_input = input(": ")

            if user_input == "quit":
                break

            elif user_input in ["+", "-", "*", "/"]:
                #Getting the input numbers to be operates on
                num1 = float(input("\nEnter a number: "))
                num2 = float(input("\nEnter another number: "))

                #Performing the desired operation
                if user_input == "+":
                    result = num1 + num2
                    print(num1, "+", num2, "=", result)
                elif user_input == "-":
                    result = num1 - num2
                    print(num1, "-", num2, "=", result)
                elif user_input == "*":
                    result = num1 * num2
                    print(num1, "*", num2, "=", result)
                elif user_input == "/":
                    result = num1 / num2
                    print(num1, "/", num2, "=", result)
            else:
                #To display the error code if the user enters undesired input 
                print("Invalid Input")

    #This runs when Temperature calculations are to be done 
    elif choice =='2':

        #Selecting the current type of data to be converted
        print("\nEnter value type to be converted:-\n1 - Celsius\n2 - Fahrenheit\n3 - Kelvin")
        val_type = float(input())

        #getting the data
        num = float(input("\nEnter operand: "))

        #Getting the desired conversion mode
        print("\nConvert value to:-\n1 - Celsius\n2 - Fahrenheit\n3 - Kelvin")
        conv_to = float(input())
        result = float()

        #To select the precise operations to be done and calculating the output
        if (val_type == 1) and (conv_to == 1):
            result = num
        elif (val_type == 1) and (conv_to == 2):
            result =  num + 33.8
        elif (val_type == 1) and (conv_to == 3):
            result =  num + 274.5
        elif (val_type == 2) and (conv_to == 1):
            result =  num - 17.22
        elif (val_type == 2) and (conv_to == 2):
            result =  num - 17.22
        elif (val_type == 2) and (conv_to == 3):
            result= num + 255.92
        elif (val_type == 3) and (conv_to == 1):
            result= num - 272.15
        elif (val_type == 3) and (conv_to == 2):
            result = num - 457.87
        elif (val_type == 3) and (conv_to == 3):
            result = num
        else:
            #This displays the error if something undesired is entered
            print("\n\nError! \nCheck your input value!")

        #Displaying the result
        print("\nThe converted Temperature is: ", result)

    #this runs when data is to be converted in length terms
    elif choice =='3':

        #Selecting the current type of data to be operated on
        print("\nEnter value type to be converted:-\n1 - Millimeters\n2 - Centimeters\n3 - Meters")
        val_type = float(input())

        #getting the data
        num = float(input("\nEnter operand: "))

        #Getting the desired conversion mode
        print("\nConvert value to:-\n1 - Millimeters\n2 - Centimeters\n3 - Meters")
        conv_to = float(input())
        result = float()

        #To select the precise operations to be done and calculating the output
        if (val_type == 1) and (conv_to == 1):
            result = num
        elif (val_type == 1) and (conv_to == 2):
            result =  num / 10
        elif (val_type == 1) and (conv_to == 3):
            result =  num / 1000
        elif (val_type == 2) and (conv_to == 1):
            result =  num * 10
        elif (val_type == 2) and (conv_to == 2):
            result =  num 
        elif (val_type == 2) and (conv_to == 3):
            result= num / 100
        elif (val_type == 3) and (conv_to == 1):
            result= num * 1000
        elif (val_type == 3) and (conv_to == 2):
            result = num * 100
        elif (val_type == 3) and (conv_to == 3):
            result = num
        else:
        #This displays the error if something undesired is entered
            print("\n\nError! \nCheck your input value!")

        #Displaying the result
        print("\nThe converted length is: ", result)

    #This runs when data is to be converted in Speed terms
    elif choice =='4':

        #Selecting the current type of data to be operated on
        print("\nEnter value type to be converted:-\n1 - Meters per second\n2 - Kilometers per hour\n3 - Miles per hour")
        val_type = float(input())

        num = float(input("\nEnter operand: "))

        print("\nConvert value to:-\n1 -Meters per second\n2 - Kilometers per hour\n3 - Miles per hour")
        conv_to = float(input())
        result = float()

        #To select the precise operations to be done and calculating the output
        if (val_type == 1) and (conv_to == 1):
            result = num
        elif (val_type == 1) and (conv_to == 2):
            result =  num * 3.6
        elif (val_type == 1) and (conv_to == 3):
            result =  num * 2.23
        elif (val_type == 2) and (conv_to == 1):
            result =  num / 3.6
        elif (val_type == 2) and (conv_to == 2):
            result =  num 
        elif (val_type == 2) and (conv_to == 3):
            result= num / 1.6
        elif (val_type == 3) and (conv_to == 1):
            result= num / 2.23
        elif (val_type == 3) and (conv_to == 2):
            result = num * 1.6
        elif (val_type == 3) and (conv_to == 3):
            result = num
        else:
        #This displays the error if something undesired is entered
            print("\n\nError! \nCheck your input value!")

        #Displaying the result
        print("\nThe converted length is: ", result)

    #This runs when data is to be converted in weight terms
    elif choice =='5':

        #Selecting the current type of data to be converted
        print("\nEnter value type to be converted:-\n1 - Grams\n2 - KiloGrams\n3 - Pounds")
        val_type = float(input())

        #getting the data
        num = float(input("\nEnter operand: "))

        #Getting the desired conversion mode
        print("\nConvert value to:-\n1 - Grams\n2 - KiloGrams\n3 - Pounds")
        conv_to = float(input())
        result = float()

        #To select the precise operations to be done and calculating the output
        if (val_type == 1) and (conv_to == 1):
            result = num
        elif (val_type == 1) and (conv_to == 2):
            result =  num / 1000
        elif (val_type == 1) and (conv_to == 3):
            result =  num / 453.59
        elif (val_type == 2) and (conv_to == 1):
            result =  num * 1000
        elif (val_type == 2) and (conv_to == 2):
            result =  num 
        elif (val_type == 2) and (conv_to == 3):
            result= num *2.20
        elif (val_type == 3) and (conv_to == 1):
            result= num * 453.59
        elif (val_type == 3) and (conv_to == 2):
            result = num / 2.20
        elif (val_type == 3) and (conv_to == 3):
            result = num
        else:
            #This displays the error if something undesired is entered
            print("\n\nError! \nCheck your input value!")
            
        #Displaying the result
        print("\nThe converted weightis: ", result)

main()


