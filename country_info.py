import requests

def fetch_country_info(country_code):
    url = f'https://restcountries.com/v3.1/alpha/{country_code}'
    response = requests.get(url)

    if response.status_code == 200:
        country_data = response.json()

        # Extract relevant information
        country_name = country_data[0]['name']['common']
        population = country_data[0]['population']
        currencies = ', '.join(country_data[0]['currencies'].keys())

        print(f"Country: {country_name}")
        print(f"Population: {population}")
        print(f"Currencies: {currencies}")
    else:
        print(f"Error: Unable to fetch country information. Status code: {response.status_code}")

def main():
    country_code = input("Enter the country code (e.g., USA, IND): ")
    fetch_country_info(country_code)

if __name__ == "__main__":
    main()
