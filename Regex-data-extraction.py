import re

# Email validation
def is_valid_email(email):
    """Validates email addresses like user@example.com"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

# URL validation
def is_valid_url(url):
    """Validates URLs like https://www.example.com"""
    pattern = r'^https?://(?:[\w\-]+\.)+[a-z]{2,6}(?:/[\w\-./?%&=]*)?$'
    return re.match(pattern, url) is not None

# Phone number validation
def is_valid_phone(phone):
    """Validates phone numbers in formats like (123) 456-7890, 123-456-7890, 123.456.7890"""
    pattern = r'^(\(\d{3}\)\s?\d{3}[-.]\d{4}|\d{3}[-.]\d{3}[-.]\d{4})$'
    return re.match(pattern, phone) is not None

# Currency amount validation
def is_valid_currency(amount):
    """Validates currency amounts like $19.99 or $1,234.56"""
    pattern = r'^\$\d{1,3}(,\d{3})*(\.\d{2})?$'
    return re.match(pattern, amount) is not None

# Credit card validation
def is_valid_credit_card(card):
    """Validates credit card numbers like 1234 5678 9012 3456 or 1234-5678-9012-3456"""
    pattern = r'^\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}$'
    return re.match(pattern, card) is not None

# Time validation (12-hour and 24-hour)
def is_valid_time(time_str):
    """Validates 24-hour time (e.g., 14:30) and 12-hour time (e.g., 2:30 PM)"""
    pattern_24 = r'^([01]\d|2[0-3]):[0-5]\d$'  # 24-hour format
    pattern_12 = r'^(1[0-2]|0?[1-9]):[0-5]\d\s?(AM|PM|am|pm)$'  # 12-hour format
    return re.match(pattern_24, time_str) is not None or re.match(pattern_12, time_str) is not None

# HTML tag validation
def is_valid_html_tag(tag):
    """Validates simple HTML tags like <p>, <div class="...">, <img src="..." />"""
    pattern = r'^<[^>]+>$'
    return re.match(pattern, tag.strip()) is not None

# Sample data
test_data = {
    "emails": [
        "user@example.com",
        "firstname.lastname@company.co.uk",
        "bad-email@"
    ],
    "urls": [
        "https://www.example.com",
        "https://subdomain.example.org/page",
        "htp://wrong.url"
    ],
    "phones": [
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "4567890"
    ],
    "currencies": [
        "$19.99",
        "$1,234.56",
        "$123456.78"
    ], 
    "credit_cards": [
        "1234 5678 9012 3456",
        "1234-5678-9012-3456",
        "1234567890123456"   
    ],
    "times": [
        "14:30",
        "2:30 PM",
        "25:00",       # Invalid
        "13:75"        # Invalid
    ],
    "html_tags": [
        "<p>",
        "<div class=\"example\">",
        "<img src=\"image.jpg\" alt=\"description\">",
        "plain text"
    ]

}

# Display results
print("\n=== EMAIL VALIDATION ===")
for email in test_data["emails"]:
    print(f"Email '{email}' is valid? {is_valid_email(email)}")

print("\n=== URL VALIDATION ===")
for url in test_data["urls"]:
    print(f"URL '{url}' is valid? {is_valid_url(url)}")

print("\n=== PHONE VALIDATION ===")
for phone in test_data["phones"]:
    print(f"Phone '{phone}' is valid? {is_valid_phone(phone)}")

print("\n=== CURRENCY VALIDATION ===")
for currency in test_data["currencies"]:
    print(f"Currency '{currency}' is valid? {is_valid_currency(currency)}")
    print("\n=== CREDIT CARD VALIDATION ===")
for card in test_data["credit_cards"]:
    print(f"Credit Card '{card}' is valid? {is_valid_credit_card(card)}")

print("\n=== TIME VALIDATION ===")
for time in test_data["times"]:
    print(f"Time '{time}' is valid? {is_valid_time(time)}")

print("\n=== HTML TAG VALIDATION ===")
for tag in test_data["html_tags"]:
    print(f"HTML Tag '{tag}' is valid? {is_valid_html_tag(tag)}")


