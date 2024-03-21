"""
arrays_program1.py

This Python program allows the user to enter a series of numbers and then calculates and displays the sum and average of those numbers. The user can enter as many numbers as they want and stop entering numbers by typing 'q'.
"""
def calculate_average(numbers: list[float]) -> float:
    sum = 0
    for i in range(0, len(numbers), 1):
        sum += float(numbers[i])
    average = (sum/len(numbers))
    # Return the average of the provided list.
    return average
    
def calculate_sum(numbers: list[float]) -> float:
    sum = 0
    for i in range(0, len(numbers), 1):
        sum += int(numbers[i])
    # Return the sum of the provided list.
    return sum

def get_user_input() -> str:
    userinput = input("Enter a number (or 'q' to quit): ")
    return userinput


    # Prompt the user for a number or 'q'.
    pass

def print_average(average: float) -> None:
    print("Average: " + str(average))
    pass
    
def print_sum(sum: float) -> None:
    print("Sum: " + str(sum))
    # Print the sum.
    pass

def get_list_of_numbers() -> list[float]:
    numbers: list[float] = []
    Booleen = True
    while Booleen:
        userinput = get_user_input()
        if userinput != "q":
            numbers.append(float(userinput))
        else:
            return numbers
            break
        # TODO: Loop to get numbers from the user until quit.
        # Store numbers in array and return.



def main():
    # TODO: uncomment one at a time to get working.
    numbers: list[float] = get_list_of_numbers()
    sum: float = calculate_sum(numbers)
    average: float = calculate_average(numbers)
    print_sum(sum)
    print_average(average)
    pass


if __name__ == "__main__":
    main()
