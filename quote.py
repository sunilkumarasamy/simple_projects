import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes_divs = soup.find_all('div', class_='quote')
        
        quotes = []
        for quote_div in quotes_divs:
            quote = quote_div.find('span', class_='text').text
            author = quote_div.find('small', class_='author').text
            quotes.append({"quote": quote, "author": author})

        return quotes
    else:
        print(f"Error: Unable to fetch content. Status code: {response.status_code}")
        return []

def main():
    quotes_url = 'https://quotes.toscrape.com/'  # Replace with the URL of a quotes website
    quotes = scrape_quotes(quotes_url)

    if quotes:
        print("Fetched Quotes:")
        for i, quote_info in enumerate(quotes, 1):
            print(f"{i}. \"{quote_info['quote']}\" - {quote_info['author']}")
    else:
        print("No quotes found.")

if __name__ == "__main__":
    main()
