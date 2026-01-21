# Task 1: AI-Generated Logic Without Modularization (Fibonacci Sequence
# Without Functions)
# Fibonacci Sequence Generator - Logic implemented directly in main
n_input = input("Enter the number of terms (n): ")

if n_input.isdigit():
    n = int(n_input)
    
    if n <= 0:
        print("Please enter a number greater than 0.")
    else:
        # Starting values for the sequence
        a, b = 0, 1
        count = 0
        
        print(f"Fibonacci sequence with {n} terms:")
        
        # Iterative logic handled directly in the main execution path
        while count < n:
            print(a, end=" ")
            # Calculate next term and update variables
            next_term = a + b
            a = b
            b = next_term
            count += 1
        print() # Adds a newline at the end
else:
    print("Error: Invalid input. Please enter a positive integer.")

# Task 2: AI Code Optimization & Cleanup (Improving Efficiency)
# Fibonacci Sequence Generator - Modular Implementation

def generate_fibonacci(n):
    """
    This function contains the logic to generate 
    a Fibonacci sequence up to n terms.
    """
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        # Update logic: a becomes b, b becomes the sum
        a, b = b, a + b
    
    return sequence

# --- Main Execution Block ---
user_input = input("Enter the number of terms: ")

if user_input.isdigit():
    num_terms = int(user_input)
    
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        # Calling the user-defined function
        result = generate_fibonacci(num_terms)
        
        print(f"Fibonacci sequence with {num_terms} terms:")
        print(*result) # Unpacks the list for clean printing
else:
    print("Invalid input. Please enter a numeric value.")

# Task 3: Modular Design Using AI Assistance (Fibonacci Using Functions)

def get_fibonacci_sequence(n: int) -> list:
    """
    Generates a list containing the Fibonacci sequence up to n terms.
    
    Args:
        n (int): The number of terms to generate.
        
    Returns:
        list: A list of Fibonacci numbers.
    """
    # Initialize the sequence with the first two numbers
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        # Simultaneous assignment to calculate the next term efficiently
        a, b = b, a + b
        
    return sequence

def main():
    """
    Handles user interaction and displays the sequence.
    """
    try:
        user_input = input("Enter the number of terms for the Fibonacci sequence: ")
        n_terms = int(user_input)

        if n_terms <= 0:
            print("Please enter a positive integer greater than zero.")
        else:
            # Calling the modular function
            fib_list = get_fibonacci_sequence(n_terms)
            
            print(f"\nGenerated Sequence ({n_terms} terms):")
            print(fib_list)
            
    except ValueError:
        print("Invalid input! Please enter a numeric whole number.")

if __name__ == "__main__":
    main()

# Task 4: Comparative Analysis – Procedural vs Modular Fibonacci Code
def generate_fibonacci(n: int) -> list:
    """
    Generates a list containing the Fibonacci sequence up to n terms.
    Optimized using list appending and tuple unpacking.
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    try:
        n_terms = int(input("Enter the number of terms: "))
        if n_terms <= 0:
            print("Please enter a positive integer.")
            return
            
        # Calling the modular function
        result = generate_fibonacci(n_terms)
        print(f"Sequence: {result}")
        
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()


# Task 5: AI-Generated Iterative vs Recursive Fibonacci Approaches (Different
# Algorithmic Approaches for Fibonacci Series)


def display_tasks(task_list):
    """Prints all tasks in the list with their index."""
    if not task_list:
        print("\nYour task list is currently empty.")
    else:
        print("\n--- Your To-Do List ---")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def main():
    tasks = []
    print("Welcome to the Task Manager!")

    while True:
        print("\nOptions: [1] Add Task  [2] View Tasks  [3] Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            new_task = input("Enter the task description: ").strip()
            if new_task:
                tasks.append(new_task)
                print("Task added successfully.")
        
        elif choice == '2':
            display_tasks(tasks)
            
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()