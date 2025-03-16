def get_number(prompt):
    """
    I am defining a function named `get_number`, which takes one argument, `prompt`. 
    This function will ask me (or the user) for a number input.

    Components:
    - def: A keyword used to define a function.
    - get_number: The function name.
    - (prompt): The argument that will be passed when calling the function (used to customize the input prompt message).
    """
    while True:
        try:
            """
            The `try` keyword starts a block where I check for errors. 
            If something goes wrong inside this block, the program moves to the `except` block below.

            Components:
            - try: I use this when I want to "try" running some code that might cause an error.
                   If an error occurs, I can handle it gracefully in the `except` block.
            """
            
            return float(input(prompt))
            # Here, I prompt the user using the input() function and attempt to convert the input to a float.
            # If successful, I return the number and exit the loop.
        
        except ValueError:
            """
            The `except` block catches a `ValueError`, which happens if the input cannot be converted to a float. 
            For example, if I enter letters or emojis instead of numbers, this block is triggered.

            Components:
            - except: Defines the code that runs if an error happens.
            - ValueError: This specific error occurs when my input cannot be converted to a float.
            """
            print("Invalid input! Please enter a valid number.")
            # This message lets the user or me know I need to try entering a valid number again.

def get_operator(prompt):
    """
    This function asks me (or the user) to input a mathematical operator.
    I begin by defining the function using the `def` keyword, followed by the function name `get_operator`, and the `prompt` argument.
    """
    valid_operators = ["+", "-", "*", "/", "**", "//", "%"]
    """
    I define a list of valid operators that I can use.
    This list helps me validate whether the user entered a correct operator.
    """
    while True:
        operator = input(prompt)
        # Here, I prompt the user to enter an operator and store the input in the `operator` variable.
        if operator in valid_operators:
            # I check if the input is in the `valid_operators` list.
            return operator
            # If the user's input matches one of the valid operators, I return the operator and exit the loop.
        else:
            # If the input is not valid, I inform the user and ask them to enter a valid operator again.
            print("Invalid operator! Please enter one of these: +, -, *, /")

while True:  
    # This creates an infinite loop to restart the program as the user sees fit.
    # Prompt user for two numbers and an operator
    num1 = get_number("Enter the first number: ")
    """
    This line creates a variable called num1. 
    Then, the get_number function is called, and the message "Enter the first number: " is passed to it as an argument.
    When the user inputs a number, that input is passed into the get_number function. 
    Inside the function, the number is validated (to ensure it's a valid numerical value). 
    If it's valid, the function returns the number. 
    That returned value is then stored in the variable (like num1), and the program can use it in the following operations, 
    such as calculations or comparisons.
    """

    num2 = get_number("Enter the second number: ")
    operator = get_operator("Enter a mathematical operator (+, -, *, /): ")
    # The same process as above is repeated for num2 and operator.
    # The get_number function is called to get the second number, and the get_operator function is called to get the operator.
    
    """
     The code below will:
     1. Perform the calculation based on the operator
     2. Initialize the result and sweet_message variables
     3. These variables will store the result of the calculation and a sweet message to be displayed to the user.
     4. If the operator is division and the second number is 0, the result will be None.
     5. The if elif else block checks the operator and performs the corresponding calculation.
     6. It also assigns a sweet message based on the operator used.
    """
    if operator == "+":
        result = num1 + num2
        sweet_message = "Addition is a team effort, and you've nailed it!"
    elif operator == "-":
        result = num1 - num2
        sweet_message = "Subtraction helps us find what truly matters!"
    elif operator == "*":
        result = num1 * num2
        sweet_message = "Multiplication shows us how things grow together!"
    elif operator == "**": 
        result = num1 ** num2
        sweet_message = "Power elevates things to the next level—literally!"
    elif operator == "//":
        result = num1 // num2
        sweet_message = "Floor division brings us closer to the ground!"
    elif operator == "%":
        result = num1 % num2
        sweet_message = "Modulus helps us find the remainder of our journey!"    
    elif operator == "/":
        if num2 != 0:  # Check for division by zero
            result = num1 / num2
            sweet_message = "Division brings balance to the universe!"
        else:
            result = None
            sweet_message = "Oops, dividing by zero is not allowed!"
    if result is not None:
        print(f"The result of {num1} {operator} {num2} is: {result}")
        print(sweet_message)
    else:
        print("Sorry, I cannot perform the calculation.")

    # Ask the user if they want to restart or exit
    restart = input("Would you like to perform another calculation? (yes/no): ").strip().lower()
    if restart not in ["yes", "y"]:  # Exit the loop if the user says "no"
        print("Thank you for using Peter's calculator! Goodbye!")
        break

# End of the Calculator.py script