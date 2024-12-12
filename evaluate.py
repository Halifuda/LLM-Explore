import os
import pandas as pd

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
            
            print(f"File: {filename}, Ratio: {total_idk_rows}/{total_rows}, Percentage: {percentage}")

# Example usage
directory = '/data/data_public/dtw_data/LLM-Explore/results/results_Llama-3___2-1B'
calculate_idk_ratio(directory)
