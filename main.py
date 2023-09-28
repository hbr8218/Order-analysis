import pandas as pd
import numpy as np

# Read data from the CSV file
df = pd.read_csv('orders.csv')

# Task 1: Compute total revenue generated by the online store for each month
df['order_date'] = pd.to_datetime(df['order_date'])
df['order_month'] = df['order_date'].dt.strftime('%Y-%m')
monthly_revenue = df.groupby('order_month')['product_price'].sum()

# Task 2: Compute total revenue generated by each product
product_revenue = df.groupby('product_name')['product_price'].sum()

# Task 3: Compute total revenue generated by each customer
customer_revenue = df.groupby('customer_id')['product_price'].sum()

# Task 4: Identify the top 10 customers by revenue generated
top_10_customers = customer_revenue.nlargest(10)

# Print the results
print("Task 1: Total Revenue by Month")
print(monthly_revenue)
print("\nTask 2: Total Revenue by Product")
print(product_revenue)
print("\nTask 3: Total Revenue by Customer")
print(customer_revenue)
print("\nTask 4: Top 10 Customers by Revenue")
print(top_10_customers)
