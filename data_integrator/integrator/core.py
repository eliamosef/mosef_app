import pandas as pd


columns_mapping = {
    "Horodateur": "timestamp",
    "Courriel": "mail",
    "Nom": "name",
    "Prénom": "first_name",
    "Formation précédente": "q1",
    "Quelles sont les compétences que vous souhaitez acquérir à la suite de ce cours?": "q2"
}

raw_file_path = "../../raw_data.csv"
staged_file_path = "../../staged_data.csv"

#read data from raw_file

print('Reading raw file at: ' + raw_file_path)
raw_file: pd.DataFrame = pd.read_csv(
    raw_file_path,
    sep=",",
    header=0,
    skipinitialspace = True,
    encoding='utf8'
)

#renaming columns according new schema
print('Renaming columns from raw data')
renamed_columns: pd.DataFrame = raw_file.rename(columns= columns_mapping)

#TODO: triming data

#write file data

print('Writing raw data at: '+  staged_file_path )
renamed_columns.to_csv(
    staged_file_path,
    sep=",",
    header=True
)

print('Data written successfully')