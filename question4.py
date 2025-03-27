
import random
import matplotlib.pyplot as plt


#Corrected Code 

# Generating 100 random numbers between 1 and the student's ID
# I used 'int()' instead of 'integer()' to correctly convert the input to an integer
max_value = int(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(100)]

# Plotting the numbers in a line chart
# I corrected all the errors in the plotting code
plt.figure(figsize=(10, 6))  # Adjusting figure size
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')

# Adding labels, title, and legend
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend()
plt.grid(True)

# Displaying the plot
plt.show()

#Explanation of code:I corrected the code by replacing integer() with int() for converting the input to an integer. Then, I generated 100 random numbers between 1 and the entered student ID using the random.randint() function. I fixed the plotting code by correcting several typos like marker='O' to marker='o' and using markerfacecolor and markeredgecolor properly. Additionally, I fixed the label argument, added labels for the axes, a title, and made sure the legend and grid were displayed correctly. Finally, I used plt.show() to display the plot.
#Output: Pasted in Word file

