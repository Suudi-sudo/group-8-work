# question 1
def find_unique_numbers(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers

numbers = [1,2,2,3,4,4,5,6]
result = find_unique_numbers(numbers) 
print(result)   
# question 2
def is_sorted_ascending(list):
    for i in range (len (list)- 1):
      if list[i] > list[i + 1]:
          return False        
    return True
list1 =[1,2,3,4,5]
list2 = [1,3,2,4]
print(is_sorted_ascending(list1))
print(is_sorted_ascending(list2))

# question 3
def skip_seven(start, end):
    numbers_to_print = []

    for num in range(start, end + 1):
        if num % 7 != 0:
            numbers_to_print.append(str(num))
   
    print(" ".join(numbers_to_print)) 


skip_seven(10, 20)      

# question 4
def get_number_input(prompt):
    """Prompt the user for a number and validate the input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    """Main function to collect numbers and find the maximum."""
    numbers = []

   
    for i in range(1, 6):
        num = get_number_input(f"Enter number {i}: ")
        numbers.append(num)

    
    max_value = max(numbers)
    
   
    print(f"The maximum value is: {max_value}")

if __name__ == "__main__":
    main()

    # question 5

