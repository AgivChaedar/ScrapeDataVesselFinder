
# Vessel Data Scraper

This project is a web scraping script to collect vessel data from [VesselFinder](https://www.vesselfinder.com/vessels) using Selenium and Python. The script navigates through multiple pages and captures details about each vessel, storing the information in a CSV file.

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Troubleshooting](#troubleshooting)

## Overview

The script collects data about vessels, such as their name, type, estimated time of arrival, speed, navigation status, and more. It loops through multiple pages on the website, accessing each vessel's detailed page and retrieving the relevant information.

## Technologies Used
- Python
- Selenium
- pandas (for data handling)
- WebDriver for Chrome

## Installation

1. Install the required packages:
   ```bash
   pip install selenium pandas
   ```
2. Download the Chrome WebDriver that matches your version of Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in a known directory.

3. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/vessel-data-scraper.git
   ```
   
4. Edit the `path` variable in the script to point to the location of your Chrome WebDriver.

## Usage

1. Run the script:
   ```bash
   python vessel_data_scraper.py
   ```
2. The script will navigate through multiple pages on the VesselFinder website, extracting information from each vessel's page.
3. After completing the process, the data is saved to a CSV file in the specified location.

## Output

The output is a CSV file (`vessel_detail_data_10hlmnew.csv`) containing the following information:
- Vessel Name
- Vessel Type
- Predicted ETA
- Distance / Time
- Course / Speed
- Current Draught
- Navigation Status
- Position Received
- IMO / MMSI
- Callsign
- Flag
- Length / Beam

## Troubleshooting

### Timeout Issues
If the script experiences timeouts, consider increasing the `WebDriverWait` duration or adding `time.sleep()` to ensure pages load fully before the script attempts to interact with elements.

### Pagination
If the pagination changes or the website layout is updated, you may need to update the selectors for the "Next" button or the vessel detail elements.

## License
This project is licensed under the MIT License.
