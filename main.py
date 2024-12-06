import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data into a pandas DataFrame from the CSV file
df = pd.read_csv('sales_data.csv')

# Group by category and calculate total sales
sales_summary = df.groupby('Category')['Sales'].sum()

# Create a bar chart
plt.figure(figsize=(10, 6))
sales_summary.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()

# Create an output directory if it doesn't exist
output_directory = 'output2'  # Change this to your desired folder name
os.makedirs(output_directory, exist_ok=True)  # Create the folder if it doesn't exist

# Save the figure in JPG format within the output directory
output_file_path = os.path.join(output_directory, 'total_sales_by_category.jpg')
plt.savefig(output_file_path, format='jpg')
