"""
Unit Conversion Program
"""

def variable():
    while True:  # keep asking until valid input
        print("Select unit for conversion") 
        print("-----------") 
        print("Mass conversion")
        print("------------")
        print("kg -> g     : 1")
        print("g -> kg     : 2")
        print("kg -> pound : 3")
        print("pound -> kg : 4") 
        print("------------")   
        print("Temperature conversion") 
        print("------------")
        print("celsius -> kelvin     : 5")
        print("kelvin -> celsius     : 6")
        print("celsius -> fahrenheit : 7")
        print("kelvin -> fahrenheit  : 8")
        print("------------")
        print("Distance conversion")
        print("------------")
        print("km -> m     : 9")
        print("m -> km     : 10")
        print("m -> cm     : 11")
        print("km -> miles : 12")
        print("miles -> km : 13")
        print("miles -> m  : 14")
        print("------------")
        print("Speed conversion")
        print("------------")
        print("km/s -> m/s   : 15")
        print("km/hr -> m/hr : 16")
        print("km/hr -> m/s  : 17")
        print("------------")
        print("Discount")
        print("------------")
        print("Enter original price : 18")
        print("------------")
        
        user_input = input("Enter number (1 - 18): ")
        try:
            convert = int(user_input)
            if 1 <= convert <= 18:
                return convert
            else:
                print("Enter a valid number between 1 and 18.\n")
        except ValueError:
            print("Invalid input! Please enter an integer number between 1 and 18.\n")


def conversion(convert, value=None, discount=None):
    if convert == 1:
        print(f"{value} kg = {value * 1000} g")
    elif convert == 2:
        print(f"{value} g = {value / 1000} kg")
    elif convert == 3:
        print(f"{value} kg = {value * 2.20462:.2f} pounds")
    elif convert == 4:
        print(f"{value} pounds = {value / 2.20462:.2f} kg")
    elif convert == 5:
        print(f"{value} °C = {value + 273.15} K")
    elif convert == 6:
        print(f"{value} K = {value - 273.15} °C")
    elif convert == 7:
        print(f"{value} °C = {(value * 9/5) + 32} °F")
    elif convert == 8:
        print(f"{value} K = {((value - 273.15) * 9/5) + 32} °F")
    elif convert == 9:
        print(f"{value} km = {value * 1000} m")
    elif convert == 10:
        print(f"{value} m = {value / 1000} km")
    elif convert == 11:
        print(f"{value} m = {value * 100} cm")
    elif convert == 12:
        print(f"{value} km = {value * 0.621371:.2f} miles")
    elif convert == 13:
        print(f"{value} miles = {value / 0.621371:.2f} km")
    elif convert == 14:
        print(f"{value} miles = {value / 0.000621371:.2f} m")
    elif convert == 15:
        print(f"{value} km/s = {value * 1000} m/s")
    elif convert == 16:
        print(f"{value} km/hr = {value * 1000} m/hr")
    elif convert == 17:
        print(f"{value} km/hr = {value * 1000 / 3600:.2f} m/s")
    elif convert == 18:
        discounted_price = value * (1 - discount / 100)
        print(f"Discounted price: {discounted_price:.2f}")
    else:
        print("Invalid conversion option.")


if __name__ == "__main__": 
    while True: 
        convert = variable()
        
        if convert == 18:
            while True:
                try:
                    value = float(input("Enter price to get discount: "))
                    discount = float(input("Enter discount (%) : "))
                    break
                except ValueError:
                    print("Invalid input! Please enter numeric values for price and discount.")
            conversion(convert, value, discount)  
        else:
            while True:
                try:
                    value = float(input("Enter value to convert: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")
            conversion(convert, value)
        
        print("----------")
        choice = input("Do you want to exit (y/n): ").lower()
        if choice == "y":
            break
