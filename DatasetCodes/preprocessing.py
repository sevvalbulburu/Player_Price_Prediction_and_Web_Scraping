import pandas as pd
import urllib
from unidecode import unidecode

# Read the first CSV file
#df1 = pd.read_csv('player_statistics.csv', encoding='utf-8')
#df1.to_csv('anne.csv', index=False, encoding='utf-8')
# Read the second CSV file
#df2 = pd.read_csv('players_url_api_all.csv', encoding='utf-8')

# Read the third CSV file
#df3 = pd.read_csv('players_url_api_all_save.csv', encoding='utf-8')

# Merge the DataFrames and remove duplicates
# df = pd.concat([df1, df2, df3]).drop_duplicates()

#df1 = pd.read_csv('player_statistics_labeled.csv', encoding='utf-8')
#df2 = pd.read_csv('player_statistics_latest.csv', encoding='utf-8')

#df = df.applymap(lambda x: urllib.parse.unquote(x) if isinstance(x, str) else x)
# Concatenate the DataFrames and remove duplicates based on 'full_name' column
#merged_df = pd.concat([df1, df2]).drop_duplicates(subset='full_name')

# Write the merged DataFrame to a new CSV file
#merged_df.to_csv('baba.csv', index=False, encoding='utf-8')

#df = pd.read_csv('players_url_api.csv', encoding='utf-8')
#df['full_name'] = df['full_name'].apply(unidecode)
#df.to_csv('players_url_api.csv', index=False, encoding='utf-8')

def merge_tables():
    # Read the CSV files
    file1 = pd.read_csv('player_statistics_unlabeled_is.csv', encoding='utf-8')
    file2 = pd.read_csv('player_statistics_labeled.csv', encoding='utf-8')

    # Merge the files and handle missing attributes
    merged = pd.merge(file1, file2, how='outer')

    # Fill missing values with None
    merged = merged.where(pd.notnull(merged), None)

    # Save the merged data to a new CSV file
    merged.to_csv('merged.csv', index=False, encoding='utf-8')

def analys():
    df = pd.read_csv('player_statistics.csv', encoding='utf-8')

    # Fill missing values with None
    df = df.where(pd.notnull(df), None)

    # Count None values in each column
    none_counts = df.isnull().sum()

    # Print the None counts
    #print(df.describe())
    for i in range(6):
        print(none_counts[i*20:(i+1)*20])
#    print(none_counts[20:40])

def add_info_pass():
    df = pd.read_csv('player_statistics.csv', encoding='utf-8')
    df_base = pd.read_csv('dataset.csv', encoding='utf-8')
    columns_to_extract = ['Total Passes', 'Total Successful Passes']
    new_table = df[columns_to_extract].copy()
    new_table['Successfull Pass Rate'] = new_table['Total Successful Passes'] / new_table['Total Passes']
    new_table = new_table.drop('Total Passes', axis=1)
    for i in ['Successfull Pass Rate', 'Total Successful Passes']:
        df_base[i] = new_table[i]
    df_base.to_csv('dataset.csv', index=False, encoding='utf-8')


def add_info_duel():
    df = pd.read_csv('player_statistics.csv', encoding='utf-8')
    df_base = pd.read_csv('dataset.csv', encoding='utf-8')
    columns_to_extract = ['Duels won', 'Duels']
    new_table = df[columns_to_extract].copy()
    new_table['Duels Rate'] = new_table['Duels won'] / new_table['Duels']
    for i in ['Duels Rate', 'Duels']:
        df_base[i] = new_table[i]
    df_base.to_csv('dataset.csv', index=False, encoding='utf-8')


def add_info():
    df = pd.read_csv('player_statistics.csv', encoding='utf-8')
    columns_to_extract = ['label', 'full_name','priceA','height','body_mass_index','foot','age','position']
    new_table = df[columns_to_extract].copy()
    new_table.to_csv('dataset.csv', index=False, encoding='utf-8')


def add_info2():
    df = pd.read_csv('player_statistics.csv', encoding='utf-8')
    df_base = pd.read_csv('dataset.csv', encoding='utf-8')
    columns_to_extract = ['Time Played', 'Appearances', 'Recoveries', 'Touches', 'Games Played', 'Winning Goal']
    new_table = df[columns_to_extract].copy()
    new_table.to_csv('dataset.csv', index=False, encoding='utf-8')
    for i in columns_to_extract:
        df_base[i] = new_table[i]
    df_base.to_csv('dataset.csv', index=False, encoding='utf-8')


def add_Total_Losses_Of_Possession():
    df = pd.read_csv('player_statistics.csv', encoding='utf-8')
    df_base = pd.read_csv('dataset.csv', encoding='utf-8')
    columns_to_extract = ['Total Losses Of Possession']
    new_table = df[columns_to_extract].copy()
    df_base['Total Losses Of Possession'] = new_table['Total Losses Of Possession']
    df_base.to_csv('dataset.csv', index=False, encoding='utf-8')


def add_Goals_Conceded():
    df = pd.read_csv('player_statistics.csv', encoding='utf-8')
    df_base = pd.read_csv('dataset.csv', encoding='utf-8')
    columns_to_extract = ['Goals Conceded']
    new_table = df[columns_to_extract].copy()
    df_base['Goals Conceded'] = new_table['Goals Conceded']
    df_base.to_csv('dataset.csv', index=False, encoding='utf-8')


def add_key_passes():
    df = pd.read_csv('player_statistics.csv', encoding='utf-8')
    df_base = pd.read_csv('dataset.csv', encoding='utf-8')
    columns_to_extract = ['Key Passes']
    new_table = df[columns_to_extract].copy()
    print(new_table.describe(), new_table.mode())
    df_base['Key Passes'] = new_table['Key Passes']
    df_base.to_csv('dataset.csv', index=False, encoding='utf-8')


def add_Total_Shots():
    df = pd.read_csv('player_statistics.csv', encoding='utf-8')
    df_base = pd.read_csv('dataset.csv', encoding='utf-8')
    columns_to_extract = ['Total Shots']
    new_table = df[columns_to_extract].copy()
    df_base['Total Shots'] = new_table['Total Shots']
    df_base.to_csv('dataset.csv', index=False, encoding='utf-8')


def add_Yellow_Cards():
    df = pd.read_csv('player_statistics.csv', encoding='utf-8')
    df_base = pd.read_csv('dataset.csv', encoding='utf-8')
    columns_to_extract = ['Yellow Cards']
    new_table = df[columns_to_extract].copy()
    df_base['Yellow Cards'] = new_table['Yellow Cards']
    df_base.to_csv('dataset.csv', index=False, encoding='utf-8')

def check():
    df = pd.read_csv('dataset.csv', encoding='utf-8')

    # Check if any None values exist in the DataFrame
    has_none_values = df.isnull().values.any()

    # Print the result
    if has_none_values:
        print("The DataFrame contains None values.")
    else:
        print("The DataFrame does not contain None values.")


def assign_key_numbers(df, column_name):
    # Get unique strings from the specified column
    unique_strings = df[column_name].unique()

    # Create a mapping dictionary for strings and key numbers
    string_to_key = {string: key for key, string in enumerate(unique_strings, 1)}

    # Assign key numbers to the strings and create a new column
    df[column_name] = df[column_name].map(string_to_key)

    return df


def convert_string_values():
    df = pd.read_csv('player_statistics.csv', encoding='utf-8')
    df_base = pd.read_csv('dataset.csv', encoding='utf-8')
    #df=df.drop(labels='team_name', axis=1)
    #df=df.drop(labels='nationality', axis=1)
    #df.to_csv('player_statistics.csv', index=False, encoding='utf-8')

    # Assuming you have a DataFrame named 'df' and a column name to process
    #column_name = 'foot'
    #column_name = 'position'
    # increased: 1 decreased : 2
    column_name = 'label'

    # Call the function to assign key numbers
    df_base = assign_key_numbers(df_base, column_name)
    df = assign_key_numbers(df, column_name)
    df.to_csv('player_statistics.csv', index=False, encoding='utf-8')
    df_base.to_csv('dataset.csv', index=False, encoding='utf-8')

# merge_tables()
# analys()
# add_info()
# add_info2()
# add_info_pass()
# add_info_duel()
# add_Total_Losses_Of_Possession()
# add_key_passes()
# add_Total_Shots()
# add_Goals_Conceded()
# add_Yellow_Cards()
# check()
# convert_string_values()
# full_name,priceA,height,body_mass_index,foot,age,position,Successfull Pass Rate,Total Successful Passes,Duels Rate,Duels,Total Losses Of Possession,Time Played,Appearances,Recoveries,Touches,Games Played,Winning Goal,Goals Conceded,Key Passes,Total Shots,Yellow Cards
