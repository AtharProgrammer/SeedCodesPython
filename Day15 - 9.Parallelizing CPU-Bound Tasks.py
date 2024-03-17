import threading

def calculate_square(numbers):
    for number in numbers:
        print(f"Square of {number}: {number * number}")

def calculate_cube(numbers):
    for number in numbers:
        print(f"Cube of {number}: {number * number * number}")

numbers = [1, 2, 3, 4, 5]

thread1 = threading.Thread(target=calculate_square, args=(numbers,))
thread2 = threading.Thread(target=calculate_cube, args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Calculation complete")
