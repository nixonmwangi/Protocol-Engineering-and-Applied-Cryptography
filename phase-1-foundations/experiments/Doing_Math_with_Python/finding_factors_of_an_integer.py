'''
Finding the factors of an integer
'''

def factors(b):
    for i in range(1, b+1):
        if b % i == 0:
            print(i)

if __name__ == '__main__':
    b = input("Please enter a number: ")

    try:
        b = int(b)
        if b > 0:
            factors(b)

        else:
            print("Please enter a valid number!")

    except ValueError:
        print("please enter a valid number!")            
        