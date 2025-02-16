# WebScraping_Shopping_Data
This project automates the extraction of product details from Google Shopping using Selenium and Pandas. It takes a list of item names from an Excel file, searches them on Google Shopping, extracts details such as product title, price, and website name, and saves the results in an output Excel file. 

## Project Overview
This project automates the extraction of product details from Google Shopping using Selenium and Pandas. It reads product names from an Excel file, searches them on Google Shopping, extracts relevant details such as product title, price, and website name, and saves the results in an output Excel file. The script also filters out listings from Amazon and eBay to ensure a more diverse dataset.

## Features
- Reads product names from an Excel file.
- Searches each product on Google Shopping.
- Extracts product details including title, price, and seller website.
- Excludes Amazon and eBay listings for a diverse dataset.
- Saves the results into an output Excel file.

## Prerequisites
Ensure the following dependencies are installed before running the script:
- Python 3.x
- Selenium
- Pandas
- ChromeDriver (must match your Chrome browser version)

### Installation
Install the required Python libraries using:
```bash
pip install selenium pandas openpyxl
```

## Setup and Usage
1. **Clone the Repository**
```bash
git clone https://github.com/your-username/google-shopping-web-scraper.git
cd google-shopping-web-scraper
```

2. **Prepare Input File**
   - Create an Excel file (`input.xlsx`) with a column named `item_name.value` containing the list of products to search.

3. **Run the Script**
   ```bash
   python script.py input.xlsx output.xlsx /path/to/chromedriver
   ```
   Replace `/path/to/chromedriver` with the actual path of the ChromeDriver executable.

## Script Workflow
1. Initializes the Selenium WebDriver.
2. Reads product names from an input Excel file.
3. Searches for each product on Google Shopping.
4. Extracts product details (title, price, old price, seller website, and URL).
5. Excludes Amazon and eBay listings.
6. Saves the extracted data into an output Excel file.

## Example Usage
```python
# Example Usage:
main("input.xlsx", "output.xlsx", "chromedriver.exe")
```

## Best Practices for Open Source
- **Respect Google’s Terms of Service:** Scraping public data may have restrictions. Check Google’s [robots.txt](https://www.google.com/robots.txt) and [Terms of Service](https://policies.google.com/terms).
- **Implement Rate Limits:** Avoid sending excessive requests to prevent getting blocked. Consider adding delays between requests.
- **Use a User-Agent Header:** Customize request headers to mimic human behavior.
- **Consider Alternative APIs:** Google provides a [Shopping API](https://developers.google.com/shopping-content) for retrieving shopping data.
- **Include a Disclaimer:** State that this project is for educational purposes only and should not be misused.
- **Add a License:** Use an open-source license (e.g., MIT) to clarify permissions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
[Vigneshwaran](https://github.com/your-username)

