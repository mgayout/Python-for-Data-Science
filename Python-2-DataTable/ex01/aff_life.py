from load_csv import load
import matplotlib.pyplot as plt


def main():
    
    """

    """
    dataset = load("life_expectancy_years.csv")
    germany_data = dataset[dataset['country'] == 'Germany']
    years = germany_data.columns[1:]
    life_expectancy = germany_data.values[0][1:]

    plt.plot(years, life_expectancy, label='Germany')
    plt.title('Life Expectancy in Germany Over the Years')
    plt.xlabel('Year')
    plt.xticks(years[::40], rotation=45)
    plt.ylabel('Life Expectancy')
    plt.yticks(range(30, 101, 10))
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
	main()
