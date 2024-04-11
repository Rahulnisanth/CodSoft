import math

def add(nums):
    return sum(nums)

def sub(nums):
    return nums[0] - nums[1]

def mul(nums):
    return math.prod(nums)

def division(nums):
    if nums[1] == 0:
        return "Error occurred, Division by zero"
    return nums[0] // nums[1], nums[0] % nums[1]

def power(nums):
    return math.pow(nums[0], nums[1])

def sqrt(nums):
    if nums[0] < 0:
        return "Error occurred, Cannot find square root of a negative number"
    return math.sqrt(nums[0])

def main():
    while True:
        print("\n------- A Simple arithmetic calculator --------")
        print("[1] Addition")
        print("[2] Subtraction")
        print("[3] Multiplication")
        print("[4] Division")
        print("[5] Power")
        print("[6] Square root")
        print("[7] Exit")
        choice = input("Enter the calculation choice: ")

        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Invalid choice! Please enter a valid option.")
            continue

        if choice == '7':
            print("Exiting....")
            break

        nums = list(map(int, input("Enter the numbers separated by space: ").split()))
        if choice == '1':
            print(f"The Result for addition is:  {add(nums)}")
        elif choice == '2':
            print(f"The Result for subtraction is:  {sub(nums)}")
        elif choice == '3':
            print(f"The Result for multiplication is:  {mul(nums)}")
        elif choice == '4':
            quotient, remainder = division(nums)
            print(f"Quotient:  {quotient}")
            print(f"Remainder:  {remainder}")
        elif choice == '5':
            print(f"The Result for {nums[0]} power {nums[1]} is:  {power(nums)}")
        elif choice == '6':
            print(f"Square Root of {nums[0]} is:  {sqrt(nums)}")

if __name__ == '__main__':
    main()
