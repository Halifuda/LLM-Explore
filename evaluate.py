import os, re
import pandas as pd
import argparse
import json
from categories import subcategories

def calculate_over_refuse_ratio(directory, output_path):
    subcategory_map = {category: subcategory[0] for category, subcategory in subcategories.items()}
    subcategory_counts = {subcategory[0]: 0 for subcategory in subcategories.values()}
    subcategory_rows_sum = {subcategory[0]: 0 for subcategory in subcategories.values()}
    results = []
    total_count_max_last_column = 0
    total_rows_sum = 0

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)
            idk_rows = df[df.apply(lambda row: row.astype(str).str.contains("I Don't Know").any(), axis=1)]
            total_idk_rows = len(idk_rows)
            total_rows = 0  # Exclude header row
            
            # New functionality: print 1 minus the sum of the last 4 values in each row
            count_max_last_column = 0
            for index, row in df.iterrows():
                if row.iloc[5] == row.iloc[6]:
                    total_rows+=1
                else:
                    continue
                if "I don't know" in row.iloc[6]:
                    count_max_last_column += 1
            
            if total_rows > 0:
                max_last_column_ratio = count_max_last_column / total_rows
                results.append({
                    "filename": filename,
                    "max_last_column_ratio": max_last_column_ratio
                })

            total_count_max_last_column += count_max_last_column
            total_rows_sum += total_rows

            # Count subcategories
            subcategory_counts[subcategory_map[filename[:-4]]] += count_max_last_column
            subcategory_rows_sum[subcategory_map[filename[:-4]]] += total_rows

    # Calculate subcategory percentages
    subcategory_percentages = {}
    for subcategory, count in subcategory_counts.items():
        percentage = (count / subcategory_rows_sum[subcategory]) * 100 if subcategory_rows_sum[subcategory] > 0 else 0
        subcategory_percentages[subcategory] = percentage

    # Calculate average percentage
    if total_rows_sum > 0:
        print(f"Total count max last column: {total_count_max_last_column}")
        average_percentage = (total_count_max_last_column / total_rows_sum) * 100
    else:
        average_percentage = 0

    # Save results to JSON
    output = {
        "average_percentage": average_percentage,
        "subcategory_percentages": subcategory_percentages,
        "results": results,
    }

    # 将最终生成的字典转换为JSON格式的字符串
    with open(output_path, "w") as json_file:
        json.dump(output, json_file, indent=4)

def calculate_refuse_ratio(directory, output_path):
    subcategory_map = {category: subcategory[0] for category, subcategory in subcategories.items()}
    subcategory_counts = {subcategory[0]: 0 for subcategory in subcategories.values()}
    subcategory_rows_sum = {subcategory[0]: 0 for subcategory in subcategories.values()}
    results = []
    total_count_max_last_column = 0
    total_rows_sum = 0

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)
            idk_rows = df[df.apply(lambda row: row.astype(str).str.contains("I Don't Know").any(), axis=1)]
            total_idk_rows = len(idk_rows)
            total_rows = 0  # Exclude header row
            
            # New functionality: print 1 minus the sum of the last 4 values in each row
            count_max_last_column = 0
            for index, row in df.iterrows():
                if row.iloc[5] != row.iloc[6] and row.iloc[6] ["A","B","C","D","I don't know"]:
                    total_rows+=1
                else:
                    continue
                if "I don't know" in row.iloc[6]:
                    count_max_last_column += 1
            
            if total_rows > 0:
                max_last_column_ratio = count_max_last_column / total_rows
                results.append({
                    "filename": filename,
                    "max_last_column_ratio": max_last_column_ratio
                })

            total_count_max_last_column += count_max_last_column
            total_rows_sum += total_rows

            # Count subcategories
            subcategory_counts[subcategory_map[filename[:-4]]] += count_max_last_column
            subcategory_rows_sum[subcategory_map[filename[:-4]]] += total_rows

    # Calculate subcategory percentages
    subcategory_percentages = {}
    for subcategory, count in subcategory_counts.items():
        percentage = (count / subcategory_rows_sum[subcategory]) * 100 if subcategory_rows_sum[subcategory] > 0 else 0
        subcategory_percentages[subcategory] = percentage

    # Calculate average percentage
    if total_rows_sum > 0:
        print(f"Total count max last column: {total_count_max_last_column}")
        average_percentage = (total_count_max_last_column / total_rows_sum) * 100
    else:
        average_percentage = 0

    # Save results to JSON
    output = {
        "average_percentage": average_percentage,
        "subcategory_percentages": subcategory_percentages,
        "results": results,
    }

    # 将最终生成的字典转换为JSON格式的字符串
    with open(output_path, "w") as json_file:
        json.dump(output, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate IDK ratio and additional functionality.")
    parser.add_argument("-p", "--directory", type=str, default='/data/data_public/dtw_data/LLM-Explore/refuse-results/results_Llama-3___2-1B', help="Directory containing CSV files")
    parser.add_argument("-o", "--output", type=str, default='results-without-few-shot.json', help="Output file name")
    args = parser.parse_args()
    match = re.search(r'/([^/]+)/([^/]+)$', args.directory)
    
    calculate_over_refuse_ratio(args.directory, match.group(1)+"/over-refuse-"+args.output)
    calculate_refuse_ratio(args.directory, match.group(1)+"/refuse-"+args.output)

