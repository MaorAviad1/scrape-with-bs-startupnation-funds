# scrape-with-bs-startupnation-funds
This script is a Python program for web scraping multiple web pages and extracting funding data from them. The program reads a list of URLs from a CSV file, fetches the HTML code for each URL using the requests library, and extracts the total funding value from the HTML code using the BeautifulSoup library.
## Usage

-   Install Python 3 on your machine
-   Install the `requests` and `BeautifulSoup` libraries using pip:

Copy code

`pip install requests
pip install beautifulsoup4` 

-   Update the `input.csv` file with the URLs you wish to scrape
-   Run the script using the following command:

cssCopy code

`python main.py` 

-   The script will scrape the funding data from each URL and store it in a new CSV file named `output.csv`.

## Input and Output

The input file `input.csv` should be formatted with one URL per row. The output file `output.csv` will be formatted with the URL in column A and the total funding value in column B.

## Modifying the Script

If you wish to modify the script to scrape different data or from different web pages, you can do so by modifying the following parts of the code:

-   **Input and output filenames:** You can change the input and output filenames by modifying the `input_filename` and `output_filename` variables at the top of the script.
    
-   **Column indices:** You can change the column indices for the input and output data by modifying the `url_column` and `output_column` variables at the top of the script.
    
-   **HTML tags:** You can change the HTML tags used to extract the funding data by modifying the `soup.find_all()` and `find()` functions in the main loop of the script.
    

## Contributing

If you find any bugs or issues with the script, please feel free to open an issue or submit a pull request on GitHub.
