from pathlib import Path
import pandas as pd
import shutil
import pandas.errors 

input_folder = Path("day36\\input")
csv_files = list(input_folder.glob("*.csv"))

if not csv_files:
    print("No CSV files found!")

else:

    try:
        dataframes = []

        for file in csv_files:
            df = pd.read_csv(file)
            dataframes.append(df)

        final_df = pd.concat(dataframes, ignore_index=True)
        print(final_df)

        output_folder = Path("day36\\output")
        output_file = output_folder / "final_report.xlsx"

        final_df.to_excel(output_file, index=False)
        print("Excel report created successfully!")

        destination = Path("day36\\archive")

        for file in csv_files:
            source = Path(file)
            shutil.move(source, destination)
        print("All CSV files moved to archive successfully!")

    except pandas.errors.ParserError as e:
        print("Something Wrong in csv files", e)