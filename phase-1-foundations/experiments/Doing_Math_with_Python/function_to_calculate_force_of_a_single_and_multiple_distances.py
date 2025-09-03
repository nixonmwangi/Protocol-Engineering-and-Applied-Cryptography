# Function to calculate force for a single distance

import matplotlib
matplotlib.use('TkAgg')  # Choose the TkAgg backend for matplotlib (used for showing plots in a window)
import matplotlib.pyplot as plt  # Import plotting library

# Function to calculate gravitational force for a single distance
def force_calc(m1, m2, r):
    g = 6.674 * (10 ** -11)   # Gravitational constant G = 6.674 × 10^-11 N·m²/kg²
    f = (g * m1 * m2)/(r ** 2)  # Newton's law of gravitation: F = G * m1 * m2 / r²
    print(" ") 
    print(f"The gravitational force at distance {r}m is {f} N")

# Function to calculate gravitational force for multiple distances
def force_array(mm2, mm3, values):
    g = 6.674 * (10 ** -11)
    forces = []  # List to store the calculated force values

    # Loop over all distance values entered
    for value in values:
        f = (g * mm2 * mm3)/(value ** 2)
        print(f"The gravitational force at distance {value}m is {f} Newtons")
        forces.append(f)  # Add the calculated force into the list
    print(" ")   

    graph_plot(values, forces)  # Call function to optionally plot the graph

# Function to optionally plot the forces    
def graph_plot(values, forces):
    choice_2 = (input("Do you want a graph of force vs distance? (y/n):"))
    if choice_2 == "y":   # Only draw the graph if user agrees

            # Plot the data points (distance vs force)
            plt.plot(values, forces, marker='o')
            plt.xlabel('Distance in meters (m)')
            plt.ylabel('Gravitational force in newtons (N)')
            plt.title('Gravitational force vs distance')
            plt.grid(True)  # Add grid lines
            plt.savefig("force_vs_distance.png")  # Save graph as PNG file
            plt.show()  
            print("Graph saved as force_vs_distance.png")  
    
# Main program starts here
if __name__ == "__main__":
    # Intro message for user
    print("Calculate the gravitational force between two bodies using Newton’s law of universal gravitation.")
    print("g = 6.674 × 10^-11 N/m²")
    print(" ")
    print("Calculate force for a single distance     press 1")
    print("Calculate force for multiple distances    press 2")
    print(" ")

    try:
        # Ask the user whether they want single or multiple calculations
        choice = int(input("Press 1 or 2 :"))
        if choice == 1 :
            print(" ")
            try:
                # Take input values for masses and distance
                m1 = float(input("Enter mass of the first body in kg : "))
                m2 = float(input("Enter mass of the second body in kg : "))
                print(" ")
                r  = float(input("Enter the distance between the two bodies in meters : "))
                # Call single calculation function
                force_calc(m1,m2,r)
            except  ValueError:
                print("Please enter a valid number!")

        elif choice == 2:
            try:
                # Take input values for masses
                mm2 = float(input("Enter mass of the first  body in kg : "))
                mm3 = float(input("Enter mass of the second body in kg : "))
                print(" ")
                # Ask user how many distances they want to calculate
                distances  = int(input("How many various distances do you want to calculate: "))
                print(" ")
                values = []  # List to store distances

                # Loop to collect all distance values
                for i in range (distances):
                    try:
                         v = float(input(f"Enter  distance value of {i+1} : "))
                         values.append(v)
                    except  ValueError:
                        print("Please enter a valid number!")  
                print(" ")
                # Call multiple calculation function
                force_array(mm2, mm3, values)        
                                     
            except  ValueError:
                print("Please enter a valid number!")
                
        else:   
            print("Please enter a valid number!")
                
    except ValueError:
           print("Please enter 1 or 2 !")
