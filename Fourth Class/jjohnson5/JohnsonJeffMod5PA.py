import numpy as np

def solveAndPrint(coefficients, constraintMatrix, constraintLimits):
    # Create numpy arrays for the constraints limits
    A = np.array(constraintMatrix)
    # Create numpy array for the constraint limits
    b = np.array(constraintLimits)

    # Gives me the shape as in rows and cols of the constraint matrix https://www.w3schools.com/python/numpy/numpy_array_shape.asp
    rows, cols = A.shape
    # Create numpy array for the coefficients
    profit = np.array(coefficients)

    # Balanced solution
    # Finds the exact intersection point where all constraints are satisfied simultaneously https://www.geeksforgeeks.org/numpy/numpy-linear-algebra/
    balancedValue = np.linalg.solve(A, b)

    # calculates the total profit for the balanced solution by performing a dot product operation
    balancedAmount = float(np.dot(profit, balancedValue))

    # prints the header for the output
    print("Supply" , "Constraint 1", "Constraint 2", "Constraint 3", "Profit")

    # loops through the variables and prints the supply, constraints, and profit for each to match the header
    for j in range(cols):
        col = [A[i, j] for i in range(rows)]
        # need to be floats cause we have some with decimals
        row = []
        # loop through the constraints and append to the row
        row.append(f"Variable {j+1}")
        for k in col:
            row.append(float(k))
        row.append(float(profit[j]))
        print(row)

    # prints the availability of each constraint
    result = ["Availability"]
    for limit in b:
        result.append(float(limit))
    print(result)

    # This calculates the best solo option
    for j in range(cols):
        # Find the maximum number of units that can be produced for each variable
        limits = [b[i] / A[i, j] for i in range(rows) if A[i, j] > 0]
        maxUnits = int(min(limits)) if limits else 0.0
        # Calculate the best solo option
        bestSolo = int(maxUnits * profit[j])

        # prints out the bestsolo solution
        print(f"If only Variable {j+1} is made, there would be a profit of: ${bestSolo}. "
              f"The number of units produced would be {maxUnits}.")
        
    # formats the balanced values to 5 decimal places and so it doesnt have the huge space
    values = []
    for v in balancedValue:
        values.append(str(round(v, 5)))
    breakdown = "[" + ", ".join(values) + "]"

    # prints out the balanced solution
    print(f"The balanced amount is ${balancedAmount:.2f}. "
          f"The break down is {breakdown} of each of the {cols} variables.")
    print(f"The best possible solution is ${balancedAmount:.2f} using the Balanced option.")

def getInputs():
    # get the number of variables from the user
    variables = int(input("Enter the number of variables: "))
    # gets the coefficients for the objective function from the user
    coefficients = list(map(float, input("Enter the coefficients of each variable for the objective function separated by a comma per thousand (for example: 3000, 2000, 2000): ").split(",")))
    # initializes the constraint matrix
    constraintMatrix = []

    # loops through the variables to get the constraint coefficients
    for i in range(variables):
        print("Example numbers [2,4,5] [1,2,4] [8,0,3]")
        # gets the constraint coefficients for each variable and appends to the matrix
        row = list(map(float, input(f"Enter the data for the square matrix stating the constraints: row {i+1} (for example: 2, 4, 5 and press enter and do the next row): ").split(",")))
        constraintMatrix.append(row)
    # gets the constraint limits from the user
    constraintLimits = list(map(float, input("Enter the constraint limits: separated by a comma (for example: 300, 200, 300): ").split(",")))
    return coefficients, constraintMatrix, constraintLimits

def main():
    # Gets all the inputs from the user
    coefficients, constraintMatrix, constraintLimits = getInputs()
    solveAndPrint(coefficients, constraintMatrix, constraintLimits)

main()

# Enter the number of variables: 3
# Enter the coefficients of each variable for the objective function separated by a comma per thousand (for example: 3000, 2000, 2000): 3000,2000,2000
# Example numbers [2,4,5] [1,2,4] [8,0,3]
# Enter the data for the square matrix stating the constraints: row 1 (for example: 2, 4, 5 and press enter and do the next row): 2,4,5
# Example numbers [2,4,5] [1,2,4] [8,0,3]
# Enter the data for the square matrix stating the constraints: row 2 (for example: 2, 4, 5 and press enter and do the next row): 1,2,4
# Example numbers [2,4,5] [1,2,4] [8,0,3]
# Enter the data for the square matrix stating the constraints: row 3 (for example: 2, 4, 5 and press enter and do the next row): 8,0,3
# Enter the constraint limits: separated by a comma (for example: 300, 200, 300): 300,200,300
# Supply Constraint 1 Constraint 2 Constraint 3 Profit
# ['Variable 1', 2.0, 1.0, 8.0, 3000.0]
# ['Variable 2', 4.0, 2.0, 0.0, 2000.0]
# ['Variable 3', 5.0, 4.0, 3.0, 2000.0]
# ['Availability', 300.0, 200.0, 300.0]
# If only Variable 1 is made, there would be a profit of: $111000. The number of units produced would be 37.
# If only Variable 2 is made, there would be a profit of: $150000. The number of units produced would be 75.
# If only Variable 3 is made, there would be a profit of: $100000. The number of units produced would be 50.
# The balanced amount is $183333.33. The break down is [25.0, 20.83333, 33.33333] of each of the 3 variables.
# The best possible solution is $183333.33 using the Balanced option.


# Enter the number of variables: 2
# Enter the coefficients of each variable for the objective function separated by a comma per thousand (for example: 3000, 2000, 2000): 50,40
# Example numbers [2,4,5] [1,2,4] [8,0,3]
# Enter the data for the square matrix stating the constraints: row 1 (for example: 2, 4, 5 and press enter and do the next row): 1,1.5
# Example numbers [2,4,5] [1,2,4] [8,0,3]
# Enter the data for the square matrix stating the constraints: row 2 (for example: 2, 4, 5 and press enter and do the next row): 2,1
# Enter the constraint limits: separated by a comma (for example: 300, 200, 300): 750,1000
# Supply Constraint 1 Constraint 2 Constraint 3 Profit
# ['Variable 1', 1.0, 2.0, 50.0]
# ['Variable 2', 1.5, 1.0, 40.0]
# ['Availability', 750.0, 1000.0]
# If only Variable 1 is made, there would be a profit of: $25000. The number of units produced would be 500.
# If only Variable 2 is made, there would be a profit of: $20000. The number of units produced would be 500.
# The balanced amount is $28750.00. The break down is [375.0, 250.0] of each of the 2 variables.
# The best possible solution is $28750.00 using the Balanced option.


# here down you can uncomment to run faster

#clothes
# coefficients = [50, 40]
# constraintsMax = [[1, 1.5],[2, 1]]
# constraintLimit = [750, 1000]
# solveAndPrint(coefficients, constraintsMax, constraintLimit)

# chemicals
# coefficients = [3000, 2000, 2000]
# constraintsMax = [[2, 4, 5], [1, 2, 4], [8, 0, 3]]
# constraintLimit = [300, 200, 300]
# solveAndPrint(coefficients, constraintsMax, constraintLimit)