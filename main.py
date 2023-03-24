import csv
import requests
from bs4 import BeautifulSoup

# Define the input and output filenames
input_filename = "input.csv"
output_filename = "output.csv"

# Define the column indices for the input and output data
url_column = 0  # Column A
output_column = 1  # Column B

# Open the input and output files
with open(input_filename, "r") as input_file, open(output_filename, "w", newline="") as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Iterate over each row in the input file
    for i, row in enumerate(reader):
        # Skip the header row
        if i == 0:
            writer.writerow(["URL", "Total Funding"])  # Add the new header to the output file
            continue

        # Extract the URL from the current row
        url = row[url_column]

        # Fetch the HTML code from the URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the funding value in the HTML code, if it exists
        funding_divs = soup.find_all("div", {"class": "company-funding-item"})
        if len(funding_divs) > 0:
            total_funding = funding_divs[0].find("div", {"class": "company-funding-inner-text"}).find("span").text
        else:
            total_funding = "Not found"

        # Write the funding value to the output file
        writer.writerow([url, total_funding])  # Write the URL and funding value to the output file
