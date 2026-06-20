#code by Abhimanyu

"""
1) Find total revenue
2) Find top-selling product
3) Find average price
4) Filter products with high sales (sales>5)
"""

"""
data.csv= 
product	price	sales
Laptop	50000	5
Phone	2000	10
Tablet	1500	7
Headphones	2000	25
Monitor	12000	6
Keyboard	1500	20
Mouse	800	30
"""
import pandas as pd
from io import StringIO

csv_data = """product,price,sales
Laptop,50000,5
Phone,2000,10
Tablet,1500,7
Headphones,2000,25
Monitor,12000,6
Keyboard,1500,20
Mouse,800,30
"""
# df = pd.read_csv("data.csv")

df = pd.read_csv(StringIO(csv_data))
df["revenue"] = df["price"] * df["sales"]
total_revenue = df["revenue"].sum()
print("Total revenue is:", total_revenue)

top_product = df.loc[df["sales"].idxmax(), "product"]
print("The Top selling product is:", top_product)

average_price = df["price"].mean().round(2)
print("The average price is:", average_price)

high_sales = df[df["sales"] > 5]

print("\nProducts with high sales:")
print(high_sales)
