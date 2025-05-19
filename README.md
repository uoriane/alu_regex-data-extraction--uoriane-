# alu_regex-data-extraction--uoriane-
# Regex Data Extraction Project

This project was developed as part of a Junior Full Stack Developer challenge. The goal was to build a Python-based solution using **Regular Expressions (regex)** to extract and validate different types of data from raw strings. The solution simulates how an API might process large sets of data to validate and extract useful information for a web application.

#Technologies Used
- Python 3
- Regular Expressions (`re` module)
- GitHub for version control and project sharing

#Validations Implemented
The following **7 data types** are validated using custom regex patterns:

1. **Email Addresses**
   - Examples: `user@example.com`, `firstname.lastname@company.co.uk`

2. **URLs**
   - Examples: `https://www.example.com`, `https://subdomain.example.org/page`

3. **Phone Numbers**
   - Formats supported:
     - `(123) 456-7890`
     - `123-456-7890`
     - `123.456.7890`
4. **Currency Amounts**
   - Examples: `$19.99`, `$1,234.56`

5. **Credit Card Numbers**
   - Formats supported:
     - `1234 5678 9012 3456`
     - `1234-5678-9012-3456`

6. **Time Formats**
   - 24-hour format: `14:30`
   - 12-hour format: `2:30 PM`, `9:45 am`

7. **HTML Tags**
   - Examples:
     - `<p>`
     - `<div class="example">`
     - `<img src="image.jpg" alt="description">`



