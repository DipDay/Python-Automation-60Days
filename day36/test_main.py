from pathlib import Path
import pandas as pd
import shutil 

input_folder = Path("day36\\input")
output_folder = Path("day36\\output")
destination = Path("day36\\archive")
csv_files = list(input_folder.glob("*.csv"))

dataframes = []
valid_files = []

for file in csv_files:

    try:
        df = pd.read_csv(file)
        dataframes.append(df)
        valid_files.append(file)

        print(f"Successfully read: {file.name}")

    except pd.errors.ParserError as e:
        print(f"Skipping {file.name}: {e}")

if dataframes:

    final_df = pd.concat(dataframes, ignore_index=True)

    output_file = output_folder / "final_report.xlsx"
    final_df.to_excel(output_file, index=False)

    for file in valid_files:
        shutil.move(file, destination)

else:
    print("No valid CSV files found!")