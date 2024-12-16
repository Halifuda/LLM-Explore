import os
import pandas as pd
import argparse

def calculate_idk_ratio(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)
            idk_rows = df[df.apply(lambda row: row.astype(str).str.contains("I Don't Know").any(), axis=1)]
            total_idk_rows = len(idk_rows)
            total_rows = len(df) - 1  # Exclude header row

            if total_rows == 0:
                ratio = 0
                percentage = "0%"
            else:
                ratio = total_idk_rows / total_rows
                percentage = f"{ratio * 100:.2f}%"
            
            # print(f"File: {filename}, Ratio: {total_idk_rows}/{total_rows}, Percentage: {percentage}")
            
            # New functionality: print 1 minus the sum of the last 4 values in each row
            for index, row in df.iterrows():
                last_four_sum = row.iloc[-4:].sum()
                result = 1 - last_four_sum
                if abs(result) > 1e-6:
                    print(f"Row {index}: 1 - sum(last 4 values) = {result}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate IDK ratio and additional functionality.")
    parser.add_argument("-p", "--directory", type=str, default='/data/data_public/dtw_data/LLM-Explore/refuse-results/results_Llama-3___2-1B', help="Directory containing CSV files")
    args = parser.parse_args()
    
    calculate_idk_ratio(args.directory)
