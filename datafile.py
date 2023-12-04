

import pandas as pd 
import matplotlib.pyplot as plt 

def analyze_data(data):

    df = pd.DataFrame(list(data.items()), columns=['City','Population'])
    print("basic statistics")
    print(df.describe())

    df.plot(kind='bar', x='City', y='Population', legend=False)
    plt.title('Population of Cities')
    plt.xlabel('City')
    plt.ylabel('Population')
    plt.show()



def main():
    # Sample data as a dictionary
    city_population_data = {
        'New York': 8419600,
        'Los Angeles': 3990456,
        'Chicago': 2716000,
        'Houston': 2328046,
        'Phoenix': 1680992
    }

    analyze_data(city_population_data)

if __name__ == "__main__":
    main()