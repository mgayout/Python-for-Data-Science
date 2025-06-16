from load_csv import load
import matplotlib.pyplot as plt


def main():

    """

    """
    dataset = load("life_expectancy_years.csv")
    france_data = dataset[dataset['country'] == 'France']
    years = france_data.columns[1:]
    life_expectancy = france_data.values[0][1:]

    plt.plot(years, life_expectancy, label='France')
    plt.title('France Life expectancy Projections')
    plt.xlabel('Year')
    plt.xticks(years[::40])
    plt.ylabel('Life Expectancy')
    plt.yticks(range(30, 100, 10))
    plt.tight_layout()
    plt.savefig("France.png")
#    plt.show()


if __name__ == "__main__":
    main()
