#######################################################################################################################################################
# 
# Name: Arfa Shaikh
# SID: 750004846
# Exam Date: 27-03-2025
# Module: BEMM458
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-arfa-10
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 
# Given customer feedback string

# Initializing an empty list to store (start, end) positions of words
my_list = []

# Using a for loop to find the start and end positions of the words with keys 7 and 6 (first and last digits of your SID)
for key in [7, 6]: 
    word = key_comments[key]
    start_pos = customer_feedback.find(word)  # Finds the starting index of the word
    end_pos = start_pos + len(word)  # Calculates the ending index of the word
    my_list.append((start_pos, end_pos))  # Append the positions as a tuple to the list

# Print the list of positions
print("Positions of keywords:", my_list)

# OUTPUT: Positions of keywords: [(129, 136), (18, 28)]

#Explanation of Code:I started by using the given dictionary key_comments and focused only on the keys 7 and 6, which correspond to the first and last digits of my SID (750004846).
#I then created an empty list called my_list to store the positions of the words. I then used a for loop to go through only the keys 7 and 6 from the dictionary. For each word, I used the .find() method to find the starting index of the word within the customer_feedback text. 
#Then,I calculated the end position by adding the length of the word to the starting index.
#Finally, I stored the positions as tuples (start, end) in my_list and printed the results.


##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here: 75
# Insert last two digits of ID number here: 46

# Write your code for Operating Profit Margin
def operating_profit_margin(operating_profit, revenue):
    """
    I created this function to calculate the Operating Profit Margin.
    Formula: (Operating Profit / Revenue) * 100
    """
    return (operating_profit / revenue) * 100
# Write your code for Revenue per Customer
def revenue_per_customer(total_revenue, total_customers):
    """
    I created this function to calculate Revenue per Customer.
    Formula: Total Revenue / Total Customers
    """
    return total_revenue / total_customers
# Write your code for Customer Churn Rate
def customer_churn_rate(lost_customers, total_customers):
    """
    I created this function to calculate Customer Churn Rate.
    Formula: (Lost Customers / Total Customers) * 100
    """
    return (lost_customers / total_customers) * 100
# Write your code for Average Order Value
def average_order_value(total_revenue, number_of_orders):
    """
    I created this function to calculate Average Order Value.
    Formula: Total Revenue / Number of Orders
    """
    return total_revenue / number_of_orders
# Call your designed functions here
op_margin = operating_profit_margin(75, 200)  # 75 (Operating Profit), 200 (Revenue)
rev_per_customer = revenue_per_customer(2000, 75)  # 2000 (Total Revenue), 75 (Total Customers)
churn_rate = customer_churn_rate(46, 200)  # 46 (Lost Customers), 200 (Total Customers)
avg_order_value = average_order_value(2000, 46)  # 2000 (Total Revenue), 46 (Number of Orders)

#Output:
#Operating Profit Margin: 37.50%
#Revenue per Customer: 26.67
#Customer Churn Rate: 23.00%import numpy as np
#Average Order Value: 43.48

#Explanation of code:I started by creating four separate functions to calculate important financial metrics required for the weekly report. 
#The first function, operating_profit_margin(), calculates the Operating Profit Margin which shows how profitable the company's operations are. 
#I used the formula (Operating Profit / Revenue) * 100 and called the function using the values 75 (Operating Profit) and 200 (Revenue) to get the result in percentage form. 
#The second function, revenue_per_customer(), measures the revenue generated per customer by using the formula Total Revenue / Total Customers. 
#I called this function with 2000 (Total Revenue) and 75 (Total Customers). 
#Next, I created the customer_churn_rate() function to find out how many customers were lost during a certain period. This function uses the formula (Lost Customers / Total Customers) * 100
# Then I tested it with 46 (Lost Customers) and 200 (Total Customers). 
# Lastly, I wrote the average_order_value() function to determine the average value of each order, using the formula Total Revenue / Number of Orders. For this calculation, I used the values 2000 (Total Revenue) and 46 (Number of Orders). 
# Finally, I printed the results of all these calculations.

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# I created two arrays: 'prices' and 'demands' to store the data provided in the question
# The prices array is reshaped to a 2D array as required by sklearn
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demands = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# I initialized the LinearRegression model and trained it using the 'fit()' function with the provided data
model = LinearRegression()
model.fit(prices, demands)

# I used the 'predict()' function to find the demand at the specified price
predicted_demand = model.predict(np.array([[52]]))
print(f"Predicted Demand at £52: {predicted_demand[0]}")

# I calculated revenue for each price by multiplying predicted demand by the price
# Then, I found the index of the maximum revenue using 'np.argmax()' and used that index to get the optimal price
predicted_demands = model.predict(prices)
revenues = prices.flatten() * predicted_demands  # Revenue = Price * Predicted Demand
max_revenue_index = np.argmax(revenues)  # Finding the index of the highest revenue
optimal_price = prices.flatten()[max_revenue_index]  # Getting the price corresponding to max revenue

# Printing the optimal price for maximum revenue
print(f"Optimal Price for Maximum Revenue: £{optimal_price}")

# I used 'plt.scatter()' to plot the original data points and 'plt.plot()' for the regression line
plt.figure(figsize=(8, 6))
plt.scatter(prices, demands, color='blue', label='Actual Data')
plt.plot(prices, predicted_demands, color='pink', label='Regression Line')
plt.title('Price vs Demand')
plt.xlabel('Price (£)')
plt.ylabel('Demand (Units)')
plt.legend()
plt.grid(True)
plt.show()

#Explanation of code: started by preparing the data by creating two arrays called prices and demands, which contain the price levels and their corresponding demand values. Since sklearn requires the input to be in a 2D format, I reshaped the prices array using .reshape(-1, 1).
# Next, I created a linear regression model using LinearRegression() and trained it using the .fit() method with the given data. After training the model, I used the .predict() method to estimate the demand when the price is set at £52.
#To find the price that maximizes revenue, I calculated the revenue for each price by multiplying the predicted demand by the price. Then, I used np.argmax() to get the index of the maximum revenue and retrieved the corresponding price.
#Finally, I plotted the original data points along with the regression line using plt.scatter() and plt.plot() to visualize the relationship between price and demand. The graph helps me understand how price changes affect demand and allows me to determine the best price for maximum revenue.

#Output: Predicted Demand at £52: 158.17272727272726
#Optimal Price for Maximum Revenue: £45

#Image pasted in word file

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt
'''
# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()
'''
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

