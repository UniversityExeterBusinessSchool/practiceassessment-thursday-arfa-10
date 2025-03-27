
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














# Insert first two digits of ID number here: 75
# Insert last two digits of ID number here: 46

# Step 1: Operating Profit Margin
def operating_profit_margin(operating_profit, revenue):
    """
    I created this function to calculate the Operating Profit Margin.
    Formula: (Operating Profit / Revenue) * 100
    """
    return (operating_profit / revenue) * 100

# Step 2: Revenue per Customer
def revenue_per_customer(total_revenue, total_customers):
    """
    I created this function to calculate Revenue per Customer.
    Formula: Total Revenue / Total Customers
    """
    return total_revenue / total_customers

# Step 3: Customer Churn Rate
def customer_churn_rate(lost_customers, total_customers):
    """
    I created this function to calculate Customer Churn Rate.
    Formula: (Lost Customers / Total Customers) * 100
    """
    return (lost_customers / total_customers) * 100

# Step 4: Average Order Value
def average_order_value(total_revenue, number_of_orders):
    """
    I created this function to calculate Average Order Value.
    Formula: Total Revenue / Number of Orders
    """
    return total_revenue / number_of_orders


# Step 5: Calling Functions with Example Values (Using SID 75 and 46)
op_margin = operating_profit_margin(75, 200)  # 75 (Operating Profit), 200 (Revenue)
rev_per_customer = revenue_per_customer(2000, 75)  # 2000 (Total Revenue), 75 (Total Customers)
churn_rate = customer_churn_rate(46, 200)  # 46 (Lost Customers), 200 (Total Customers)
avg_order_value = average_order_value(2000, 46)  # 2000 (Total Revenue), 46 (Number of Orders)

# Printing the results
print(f"Operating Profit Margin: {op_margin:.2f}%")
print(f"Revenue per Customer: {rev_per_customer:.2f}")
print(f"Customer Churn Rate: {churn_rate:.2f}%")
print(f"Average Order Value: {avg_order_value:.2f}")


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Preparing the data
# I created two arrays: 'prices' and 'demands' to store the data provided in the question
# The prices array is reshaped to a 2D array as required by sklearn
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demands = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# Step 2: Creating and training the linear regression model
# I initialized the LinearRegression model and trained it using the 'fit()' function with the provided data
model = LinearRegression()
model.fit(prices, demands)

# Step 3: Making predictions for demand when price is set at £52
# I used the 'predict()' function to find the demand at the specified price
predicted_demand = model.predict(np.array([[52]]))
print(f"Predicted Demand at £52: {predicted_demand[0]}")

# Step 4: Finding the price that maximizes revenue
# I calculated revenue for each price by multiplying predicted demand by the price
# Then, I found the index of the maximum revenue using 'np.argmax()' and used that index to get the optimal price
predicted_demands = model.predict(prices)
revenues = prices.flatten() * predicted_demands  # Revenue = Price * Predicted Demand
max_revenue_index = np.argmax(revenues)  # Finding the index of the highest revenue
optimal_price = prices.flatten()[max_revenue_index]  # Getting the price corresponding to max revenue

# Printing the optimal price for maximum revenue
print(f"Optimal Price for Maximum Revenue: £{optimal_price}")

# Step 5: Plotting the data points and regression line
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

