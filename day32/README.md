# Day 32 - E-commerce Product Scraper & Excel Report Generator

A Python automation project that scrapes product information from an e-commerce demo website using Selenium and exports the collected data into a formatted Excel workbook.

## Features

- **Keyword Filtering:** Search for products by keyword.
- **Custom Page Limit:** Choose how many pages to scrape.
- **Scrape All Pages:** Enter `0` to scrape all available pages.
- **Duplicate Detection:** Prevent duplicate products using a Python set.
- **Excel Export:** Save scraped product information using Pandas and OpenPyXL.
- **Excel Formatting:** Apply header styling, currency formatting, column width adjustment, and freeze panes.
- **Summary Report:** Generate a separate worksheet containing scraping statistics.
- **Input Validation:** Handle empty keywords and invalid page numbers.
- **Error Handling:** Handle internet connection errors and other exceptions.
- **Browser Cleanup:** Ensure the browser is closed after execution.

## Technologies Used

- Python
- Selenium
- Pandas
- OpenPyXL

## Project Structure

```text
day32/
│
├── main.py
├── README.md
└── products.xlsx  (generated after execution)
```

## Installation

Clone the repository:

```bash
git clone https://github.com/DipDay/Python-Automation-60Days.git
```

Navigate to the project directory:

```bash
cd Python-Automation-60Days/day32
```

Install the required libraries:

```bash
pip install selenium pandas openpyxl
```

Make sure Google Chrome is installed on your computer.

## Usage

Run the Python script:

```bash
python main.py
```

Enter a search keyword and the number of pages when prompted.

Example:

```text
Enter keyword: watch
Enter number of pages (0 for all): 3
```

To scrape all available pages:

```text
Enter number of pages (0 for all): 0
```

## Excel Output

The script generates `products.xlsx` with two worksheets:

### 1. All Products

Contains:
- Product
- Price
- URL
- Keyword

### 2. Summary

Contains:
- Pages Visited
- Repeat Products Removed
- Total Products Found

## Error Handling

The script handles invalid inputs, internet connection errors, and unexpected exceptions. It also ensures that the Selenium browser session is closed properly.

## Data Source

[ScrapingCourse - E-commerce Demo](https://www.scrapingcourse.com/ecommerce/)

This project is intended for educational and automation practice.

---

**Day 32 of my 60 Days of Python Automation Journey.**