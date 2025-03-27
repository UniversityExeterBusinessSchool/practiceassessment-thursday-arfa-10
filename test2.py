import random
import matplotlib.pyplot as plt

# Step 1: Generating 100 random numbers between 1 and the student's ID
# I used 'int()' instead of 'integer()' to correctly convert the input to an integer
max_value = int(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(100)]

# Step 2: Plotting the numbers in a line chart
# I corrected all the errors in the plotting code
plt.figure(figsize=(10, 6))  # Adjusting figure size
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')

# Step 3: Adding labels, title, and legend
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend()
plt.grid(True)

# Step 4: Displaying the plot
plt.show()
