# Python XML to CSV Converter

This project allows you to convert XML data into CSV format using Python. It is designed to take an XML file containing structured data, process it, and save the information as a CSV file.

## Features

- Reads an XML file containing structured product data.
- Converts the XML data into a CSV format.
- Saves the CSV output in a designated folder.

## Files in this Project

- `export_to_csv.py`: The main script for converting XML to CSV.
- `phones.xml`: A sample XML file with product data (you can replace this with your own XML files).
- `data/`: Folder where the generated CSV file will be saved.

## Requirements

Before running the project, you’ll need:

- Python 3.x installed.
- The `pandas` library for handling CSV files.

You can install `pandas` by running:

```bash
pip install pandas
```

## Setup Instructions

1. **Clone the repository or download the project files.**
2. **Install the required dependencies** (like `pandas`).
3. **Place your XML file** (e.g., `phones.xml`) in the project folder.

## How to Use

1. Navigate to the project directory in your terminal or command prompt.
2. Run the conversion script:
   ```bash
   python export_to_csv.py
   ```
   This will process your XML file and generate a CSV file.

3. Check the `data/` folder for the generated CSV file.

## Example XML Structure

The script is designed to work with XML files structured like this:

```xml
<phones>
  <phone name="iPhone 6">
    <company>Apple</company>
    <price>40000</price>
  </phone>
  <phone name="Samsung Galaxy S5">
    <company>Samsung</company>
    <price>33000</price>
  </phone>
</phones>
```

