# Bonus Challenge:
# Create a Python script that reads a CSV file containing information about products.
# (e.g., product ID, name, category, price) and filters out products based on a specified price range and category.
# Output the results to a new CSV file.


import csv
import os

def filter_products(input_csv, output_csv, price_range, category):
    """
    Filter products based on price range and category, and save to a new CSV.
    
    :param input_csv: Path to input CSV file.
    :param output_csv: Path to output CSV file.
    :param price_range: Tuple (min_price, max_price).
    :param category: Category to filter by.
    """
    if not os.path.exists(input_csv):
        raise FileNotFoundError(f"Input file '{input_csv}' not found.")
    
    if not isinstance(price_range, tuple) or len(price_range) != 2:
        raise ValueError("Price range must be a tuple of two values: (min_price, max_price).")
    
    try:
        with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                try:
                    price = float(row['price'])
                    if price_range[0] <= price <= price_range[1] and row['category'] == category:
                        writer.writerow(row)
                except ValueError:
                    print(f"Skipping row with invalid price: {row}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
filter_products('products.csv', 'filtered_products.csv', (10.0, 50.0), 'Electronics')

