#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to initialize WebDriver
def initialize_webdriver(chromedriver_path):
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)
    return driver

# Function to extract product grid data
def extract_product_grid_data(driver):
    product_details = {}

    try:
        product_details["Product Title"] = driver.find_element(By.XPATH, "//h4[contains(@class, 'RU1dPb')]").text
    except Exception:
        product_details["Product Title"] = "Not available"

    try:
        product_details["Current Price"] = driver.find_element(By.XPATH, "//span[contains(@class, 'Pgbknd')]").text
    except Exception:
        product_details["Current Price"] = "Not available"

    try:
        product_details["Old Price"] = driver.find_element(By.XPATH, "//div[contains(@class, 'AoPnCe')]/span").text
    except Exception:
        product_details["Old Price"] = "Not available"

    try:
        product_details["Website Name"] = driver.find_element(By.XPATH, "//div[@class='hP4iBf gUf0b uWvFpd']").text
    except Exception:
        product_details["Website Name"] = "Not available"

    try:
        product_details["Product URL"] = driver.find_element(By.XPATH, "//a[contains(@class, 'P9159d') and contains(@class, 'BbI1ub')]").get_attribute("href")
    except Exception:
        product_details["Product URL"] = "Not available"

    return product_details

# Main function to perform the automation
def main(input_file, output_file, chromedriver_path):
    driver = initialize_webdriver(chromedriver_path)
    input_df = pd.read_excel(input_file)
    all_product_data = []

    for index, row in input_df.iterrows():
        item_name = row["item_name.value"]  # Adjust column name as needed
        print(f"\nSearching for: {item_name}")

        # Open Google Shopping
        driver.get("https://www.google.com/shopping")
        time.sleep(2)

        # Perform search
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(item_name)
        search_box.submit()
        time.sleep(3)

        # Locate product elements
        products = driver.find_elements(By.XPATH, "//div[@jsname='ZvZkAe']")
        product_count = 0
        item_product_data = []

        for product in products[:10]:
            if product_count >= 10:
                break
            try:
                product.click()
                time.sleep(3)

                product_data = extract_product_grid_data(driver)

                if not product_data:
                    continue
                
                if "amazon" in product_data["Website Name"].lower() or "ebay" in product_data["Website Name"].lower():
                    continue

                product_data["Item Name"] = item_name
                item_product_data.append(product_data)
                product_count += 1
                time.sleep(2)

            except Exception as e:
                print(f"Error extracting data: {e}")

        all_product_data.extend(item_product_data)
        print(f"Completed search for {item_name}")

    driver.quit()

    product_df = pd.DataFrame(all_product_data)
    product_df.to_excel(output_file, index=False)
    print(f"Results saved to {output_file}")

# Example Usage:
# main("input_file_path.xlsx", "output_file_path.xlsx", "chromedriver_path.exe")

