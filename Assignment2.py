#code by Abhimanyu

"""
1) Find total revenue
2) Find top-selling product
3) Find average price
4) Filter products with high sales (sales>5)
"""
import pandas as pd

df = pd.read_csv("data.csv")

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
