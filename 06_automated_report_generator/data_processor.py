from config import FILE_PATH, OUTPUT_PATH
import pandas as pd
from datetime import datetime
import numpy as np

def is_valid_data(dataset):

    # Step 1: Is the date valid?
    # Convert to datetime
    converted = pd.to_datetime(dataset["order_date"], errors='coerce')
    
    # If more than a certain threshold (or all) are invalid, return False
    if converted.isna().all():
        print("Invalid Dates")
        return False

    # Step 2: Is quantity and unit price numeric and positive?
    if not pd.api.types.is_numeric_dtype(dataset["quantity"]) or not pd.api.types.is_numeric_dtype(dataset["unit_price"]):
        print("Invalid Col Quantity or Unit price: Not numeric")
        return False
    
    # Check if any quantity is less than or equal to 0
    if (dataset["quantity"] <= 0).any() or (dataset["unit_price"] <= 0).any():
        print("Invalid Col Quantity or Unit Price: Contains zero or negative values")
        return False

    # Step 3: Does revenue equal quantity multiplied by unit price?
    expected_revenue = dataset["quantity"] * dataset["unit_price"]
    if not np.isclose(dataset["revenue"], expected_revenue, rtol=1e-05, atol=1e-02).all():
        print("Invalid Revenue: Revenue doesn't match quantity * unit_price")
        return False

    # Step 4: Does cost equal quantity multiplied by unit cost?
    expected_cost = dataset["quantity"] * dataset["unit_cost"]
    if not np.isclose(dataset["cost"], expected_cost, rtol=1e-05, atol=1e-02).all():
        print("Invalid Cost: Cost doesn't match quantity * unit_cost")
        return False

    # Step 5: Does margin equal revenue minus cost?
    expected_margin = dataset["revenue"] - dataset["cost"]
    if not np.isclose(dataset["margin"], expected_margin, rtol=1e-05, atol=1e-02).all():
        print("Invalid Margin: Margin doesn't match revenue - cost")
        return False

    return True

def calculate(dataset):
    result = {}

    try:
        # 1. Sum
        result["total_revenue"] = float(dataset["revenue"].sum())
        result["total_cost"] = float(dataset["cost"].sum())
        result["total_margin"] = float(dataset["margin"].sum())
        result["total_units_sold"] = int(dataset["quantity"].sum())

        # 2. Best-performing products by revenue (sorted descending, taking top N or as a dictionary)
        best_products = dataset.groupby("product")["revenue"].sum().sort_values(ascending=False)
        result["best_products_by_revenue"] = best_products.to_dict()

        # 3. Revenue by category
        revenue_category = dataset.groupby("category")["revenue"].sum()
        result["revenue_by_category"] = revenue_category.to_dict()

        # 4. Revenue by month
        # First ensure order_date is datetime, then extract year-month string or period
        dates = pd.to_datetime(dataset["order_date"])
        dataset_copy = dataset.copy()
        dataset_copy["order_month"] = dates.dt.to_period("M").astype(str)
        
        revenue_month = dataset_copy.groupby("order_month")["revenue"].sum()
        result["revenue_by_month"] = revenue_month.to_dict()

    except Exception as e:
        print(f"Error during calculation: {e}")
        return None

    return result

# process 
def data_processing():
    if not FILE_PATH.exists():
        print(f"File not found: {FILE_PATH}")
        return None

    if not FILE_PATH.is_file() or FILE_PATH.suffix != ".csv":
        print(f"Invalid File: {FILE_PATH}")
        return None

    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


    try:

        dataset = pd.read_csv(FILE_PATH)


        if dataset.isnull().sum().any():
            dataset = dataset.dropna()

        # Require Co
        req_cols = ["product", "quantity", "unit_price", "unit_cost", "revenue", "cost", "margin", "order_date"] 
        col_names = list(dataset.columns)

        # Require cols
        if not set(req_cols).issubset(col_names):
            print(f"Skipped '{col_names}': column names don't match the Req Col ({req_cols})")
            return None

        # Is valid Dataset
        if not is_valid_data(dataset):
            print("Dataset isn't valid")
            return None

        
        result = calculate(dataset)

        if result:
            return result
        
        print("Invalid Calculation")
        return None

    except Exception as e:
        print(f"Process failed: {e}")
        return None

data_processing()