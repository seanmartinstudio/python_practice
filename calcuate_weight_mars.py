#variable types: float, int, str
#assign vs use variable
#variable casting: function to specify variable type 

#Challenge: An earthling's weight on Mars is 37.8% of their weight on earth. Write a Python program that prompts the user (an earthling) to enter their weight on earth and prints their calculated weight on Mars.

# MARS_MULTIPLE = 0.378

def main():

    earth_weight_str = input('Enter a weight on earth: ')

    earth_weight = float(earth_weight_str)

    print(earth_weight)

    # mars_weight = earth_weight * MARS_MULTIPLE

    # print('The equivalent weight on Mars: ' + str(mars_weight))
    
if __name__ == "__main__":
    main()