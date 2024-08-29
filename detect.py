import pandas as pd

def predict_column_data_types(csv_file_path):
    # Step 1: Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Step 2: Use pandas `infer_objects` to attempt to infer better data types
    df = df.infer_objects()
    
    # Step 3: Analyze the data types of each column
    data_types = df.dtypes.to_dict()

    # Step 4: Output the predicted data types
    for column, dtype in data_types.items():
        print(f"Column: {column}, Predicted Data Type: {dtype}")

    return data_types

# Example usage:
csv_file_path = 'data/test_file_1.csv'
predicted_types = predict_column_data_types(csv_file_path)
