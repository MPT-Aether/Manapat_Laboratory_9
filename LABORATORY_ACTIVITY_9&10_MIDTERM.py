""" 
Print a right-angled triangle of numbers
based on the user input for the number of rows.

Sample output:

Enter the number of rows: 5
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

# Section for the User to Input a Number of his/her Choice
num_of_rows = int(input("Enter the number of rows: "))
row = 1
column = 1

# Initial Processing of the Program Towards the Desired Number of Rows
while column <= num_of_rows:
    # Individual Numerical Value of the Rows
    val = 1
    while val <= column:
        # Initial Format of How the Rows Would Like Alongside the Important Variables to be Inputted 
        print("{}".format(row), end = " ")
        val += 1
        row += 1
    print()
    column += 1
    

"""
For users who are using the Python Application in running this python file,
make sure to put the function "input()" to prevent the Python Application to 
automatically close down or kill code. The purpose of this is to enable users
to read and understand how the output works in a clean and authentic format.
"""
input()