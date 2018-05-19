
while True:

    intro = input("Is your number binary or decimal? Type Binary or Decimal.")

    if intro.lower() == "decimal":

        number = int(input("Input your decimal number: "))
        binary = ""
        while number > 0 :
            binary = str(number%2)+binary
            number = number//2
        print("The binary number is {}.".format(binary))
        break

    elif intro.lower() == "binary":
        number = int(input("Input your binary number: "))
        decimal = 0
        depth = 0
        weight = 0   
        for bit in str(number)[::-1]:  
            weight = (2**depth)
            if bit == "1":
                decimal+=weight
            else:
                decimal+=0
            depth +=1   
        print ("The decimal number equivalent is {}.".format(str(decimal)))
        break
    else:
        print("Please provide a valid input, either 'binary' or 'decimal'.")
