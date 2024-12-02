# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the CSV file and the script into the container (adjust 'sales_data.csv' path if needed)
COPY sales_data.csv sales_data.csv
COPY script.py script.py  # Assuming the script is named 'script.py'

# Install necessary Python libraries
RUN pip install pandas matplotlib

# Create the output directory (this ensures permissions and structure)
RUN mkdir output

# Command to run the script
CMD ["python", "script.py"]
