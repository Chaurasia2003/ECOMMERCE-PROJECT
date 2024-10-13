import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Establish connection to the MySQL database
connection = mysql.connector.connect(
    user='root',
    password='Aman@2003',
    host='localhost',
    database='ecommerce'
)

# Function to fetch data from a specific table
def fetch_data(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

# Load data into DataFrames
customer_data = fetch_data('SELECT * FROM customer')
product_data = fetch_data('SELECT * FROM product')
order_data = fetch_data('SELECT * FROM order_details')

# Close the database connection
connection.close()

# Display the first few rows of each DataFrame
print("Customer Data:\n", customer_data)
print("\nProduct Data:\n", product_data)
print("\nOrder Details Data:\n", order_data)

# ------------------ Customer Analysis ------------------ #
# Total number of customers city-wise
customers_citywise = customer_data['city'].value_counts().reset_index(name='total_customers')
customers_citywise.columns = ['City', 'Total Customers']
print("\nTotal Customers City-wise:\n", customers_citywise)

# Bar Chart for city-wise customer distribution
plt.figure(figsize=(10, 5))
plt.bar(customers_citywise['City'], customers_citywise['Total Customers'], color='skyblue')
plt.title('Total Number of Customers City-wise')
plt.xlabel('City')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Most frequent customers based on order history
customer_order_count = order_data['customer_id'].value_counts().reset_index()
customer_order_count.columns = ['Customer ID', 'Order Count']  # Ensure the columns are named correctly
print("\nCustomer Order Count:\n", customer_order_count)  # Print to debug

# Get the most frequent customers
most_frequent_customers = customer_order_count.nlargest(10, 'Order Count')
print("\nMost Frequent Customers:\n", most_frequent_customers)

# Bar Chart for Top 10 Most Frequent Customers
plt.figure(figsize=(10, 5))
plt.bar(most_frequent_customers['Customer ID'], most_frequent_customers['Order Count'], color='skyblue')
plt.title('Top 10 Most Frequent Customers')
plt.xlabel('Customer ID')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------ Product Analysis ------------------ #
# Total number of products by category
products_by_category = product_data['category'].value_counts().reset_index(name='total_products')
products_by_category.columns = ['Category', 'Total Products']
print("\nTotal Number of Products by Category:\n", products_by_category)

# Bar Chart for distribution of products
plt.figure(figsize=(10, 5))
plt.bar(products_by_category['Category'], products_by_category['Total Products'], color='skyblue')
plt.title('Distribution of Products by Category')
plt.xlabel('Category')
plt.ylabel('Number of Products')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Distribution of products across sub-categories
products_by_subcategory = product_data['sub_category'].value_counts().reset_index(name='total_products')
products_by_subcategory.columns = ['Sub-category', 'Total Products']
print("\nTotal Number of Products by Sub-category:\n", products_by_subcategory)

# Bar Chart for distribution of products across sub-categories
plt.figure(figsize=(10, 5))
plt.bar(products_by_subcategory['Sub-category'], products_by_subcategory['Total Products'], color='skyblue')
plt.title('Distribution of Products Across Sub-categories')
plt.xlabel('Sub-category')
plt.ylabel('Number of Products')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Products with low stock levels (threshold of 10 units)
low_stock_products = product_data[product_data['stock'] < 10][['product_name', 'stock']]
print("\nProducts with Low Stock Levels:\n", low_stock_products)

# Average, maximum, and minimum prices for products
price_stats = product_data['selling_price'].agg(['mean', 'max', 'min'])
print("\nProduct Price Statistics (Mean, Max, Min):\n", price_stats)

# ------------------ Order Analysis ------------------ #
# Top 10 orders product-wise
top_10_orders = order_data.groupby('product_id')['total_price'].sum().nlargest(10).reset_index()
print("\nTop 10 Orders Product-wise:\n", top_10_orders)

# Month-wise total sales
order_data['order_date'] = pd.to_datetime(order_data['order_date'])
monthwise_sales = order_data.groupby(order_data['order_date'].dt.to_period('M'))['total_price'].sum().reset_index()

# Line Chart: Month-wise total sales
plt.figure(figsize=(10, 5))
plt.plot(monthwise_sales['order_date'].astype(str), monthwise_sales['total_price'], marker='o', color='darkblue')
plt.title('Month-wise Total Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Total revenue generated from orders product-wise
revenue_productwise = order_data.groupby('product_id')['total_price'].sum().reset_index()
print("\nTotal Revenue Generated Product-wise:\n", revenue_productwise)

# ------------------ Sales Analysis ------------------ #
# Total revenue generated from all orders
total_revenue = order_data['total_price'].sum()
print("\nTotal Revenue Generated from All Orders:", total_revenue)

# Total revenue by product category percentageNNJN
category_revenue_percentage = (category_revenue / total_revenue) * 100
print("\nTotal Revenue by Product Category (Percentage):\n", category_revenue_percentage)

# Pie Chart: Revenue by product category (percentage)
plt.figure(figsize=(8, 8))
plt.pie(category_revenue_percentage, labels=category_revenue.index, autopct='%1.1f%%', startangle=140)
plt.title('Revenue by Product Category (Percentage)')
plt.show()

# Most profitable products based on profit calculations
merged_data1['profit'] = (merged_data1['selling_price'] - merged_data1['original_price']) * merged_data1['quantity']
most_profitable_products = merged_data1.groupby('product_name')['profit'].sum().nlargest(10).reset_index()
print("\nMost Profitable Products:\n", most_profitable_products)

# Bar Chart: Most profitable products
plt.figure(figsize=(10, 5))
plt.bar(most_profitable_products['product_name'], most_profitable_products['profit'], color='purple')
plt.title('Most Profitable Products')
plt.xlabel('Product Name')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------ Customer Retention ------------------ #
# Analyzing repeat customers and their order patterns
repeat_customers = customer_order_count[customer_order_count['Order Count'] > 1]
print("\nRepeat Customers:\n", repeat_customers)

# Customer retention rates over time (percentage of repeat customers)
customer_retention_rate = (len(repeat_customers) / len(customer_data)) * 100
print("\nCustomer Retention Rate:", customer_retention_rate)

# ------------------ Payment Analysis ------------------ #
# Payment status distribution
payment_status_count = order_data['order_status'].value_counts().reset_index(name='count')
payment_status_count.columns = ['Order Status', 'Count']
print("\nPayment Status Distribution:\n", payment_status_count)

# Pie Chart: Payment status distribution
plt.figure(figsize=(8, 8))
plt.pie(payment_status_count['Count'], labels=payment_status_count['Order Status'], autopct='%1.1f%%', startangle=140)
plt.title('Payment Status Distribution')
plt.show()

# ------------------ Geographical Analysis ------------------ #
# Distribution of customers across cities
customer_distribution_city = customer_data['city'].value_counts().reset_index(name='total_customers')
customer_distribution_city.columns = ['City', 'Total Customers']
print("\nDistribution of Customers Across Different Cities:\n", customer_distribution_city)

# Products more popular in specific cities
final_merged_data = pd.merge(merged_data1, customer_data[['customer_id', 'city']], on='customer_id')
popular_products_citywise = final_merged_data.groupby(['city', 'product_name'])['quantity'].sum().reset_index()
print("\nProducts More Popular in Specific Cities:\n", popular_products_citywise)

# Bar Chart: Products more popular in specific cities
plt.figure(figsize=(10, 5))
for city in popular_products_citywise['city'].unique():
    city_data = popular_products_citywise[popular_products_citywise['city'] == city]
    plt.bar(city_data['product_name'], city_data['quantity'], label=city)

plt.title('Products More Popular in Specific Cities')
plt.xlabel('Product Name')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.legend(title="City")
plt.tight_layout()
plt.show()

# Closing statement for analysis
print("\nAnalysis completed successfully.")
