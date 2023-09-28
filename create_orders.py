import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Set a seed for reproducibility
random.seed(0)

# Generate fake data for orders
fake = Faker()

order_data = []

for order_id in range(1, 2135):
    customer_id = random.randint(1, 1000)
    order_date = fake.date_between(start_date='-1y', end_date='today')
    product_id = random.randint(1, 100)
    product_name = fake.word()
    product_price = round(random.uniform(5, 100), 2)
    quantity = random.randint(1, 10)
    
    order_data.append([order_id, customer_id, order_date, product_id, product_name, product_price, quantity])

# Create a Pandas DataFrame
df = pd.DataFrame(order_data, columns=['order_id', 'customer_id', 'order_date', 'product_id', 'product_name', 'product_price', 'quantity'])

# Save the DataFrame to a CSV file
df.to_csv('orders.csv', index=False)

print("CSV file 'orders.csv' has been created with 2134 records.")
