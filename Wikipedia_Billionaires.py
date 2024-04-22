import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrap_url(url):
	url = requests.get(url)
	soup = BeautifulSoup(url.text, 'html.parser')

	table = soup.find("table", class_='wikitable sortable')
	rows = table.find_all('tr')

	# Extract the table headings
	headings = [title.text.strip() for title in rows[0].find_all('th')] # Index 0 is to specify the foremost data i.e. our headings

	# Create an empty list to store the data
	data = []

	# Iterate through the rows and extract data
	for row in rows[1:]:
	    row_data = [value.text.strip() for value in row.find_all('td')]
	    # Ensure each row has the same number of elements as the headings
	    if len(row_data) == len(headings): 
	        data.append(row_data)
	# Create the DataFrame
	df = pd.DataFrame(data, columns=headings)
	print("Successfully scraped datas")
	return(df)

def extract_excel(data):
	# Extract the DataFrame to Excel
	df.to_excel("Top 10 Billionaires.xlsx", index=False)
	print("Successfully exported to excel")


# print(df)

if __name__ == '__main__':
	url = 'https://en.wikipedia.org/wiki/The_World\'s_Billionaires'
	df =scrap_url(url)
	extract_excel(df)
