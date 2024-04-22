import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_wikipedia_table(url, table_index):
    try:
        # Fetch the page content using requests
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all tables on the page
        tables = soup.find_all('table')

        if table_index >= len(tables):
            print(f"Table index {table_index} not found on the page.")
            return None

        # Assuming the desired table is at the given index
        table = tables[table_index]

        # Extract the table headings
        headings = [title.text.strip() for title in table.find_all('th')]

        # Create an empty list to store the data
        data = []

        # Iterate through the rows and extract data
        rows = table.find_all('tr')
        for row in rows[1:]:
            row_data = [value.text.strip() for value in row.find_all(['td', 'th'])]
            # Ensure each row has the same number of elements as the headings
            if len(row_data) == len(headings):
                data.append(row_data)

        # Create the DataFrame
        df = pd.DataFrame(data, columns=headings)

        print("Successfully extracted the table.")
        return df
    except Exception as e:
        print("Error:", e)
        return None

def save_to_excel(df, file_name):
    try:
        df.to_excel(f'{file_name}.xlsx', index=False)
        print("Successfully saved data to Excel file:", file_name)
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    url = input("Enter the Wikipedia URL: ")
    # url = 'https://en.wikipedia.org/wiki/The_World\'s_Billionaires'
    print("Check your table index and choose only a entirely text based table")
    table_index = int(input("Enter the table index (0 for the first table, 1 for the second, and so on): "))
    # table_index= 2

    df = extract_wikipedia_table(url, table_index)
    if df is not None:
        print(df)

        # Ask the user for the Excel file name to save the data
        file_name = input("Enter the Excel file name to save the data (e.g., data.xlsx): ")
        # file_name='sdf'
        save_to_excel(df, file_name)


# Demo:
# https://en.wikipedia.org/wiki/List_of_cities_in_Nepal
# https://en.wikipedia.org/wiki/The_World's_Billionaires