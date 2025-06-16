from load_csv import load
import matplotlib.pyplot as plt


def parse_population(values):

    """

    """

    converted = []
    for val in values:
        val = str(val).strip()
        if val.endswith('M'):
            converted.append(float(val[:-1]))
        elif val.endswith('k'):
            converted.append(float(val[:-1]) / 1000)
        else:
            converted.append(float(val))
    return converted


def main():

    """

    """

    dataset = load("population_total.csv")

    france_data = dataset[dataset['country'] == 'France']
    belgium_data = dataset[dataset['country'] == 'Belgium']

    years = list(map(int, dataset.columns[1:]))
    limited_years = [year for year in years if year <= 2050]
    index = len(limited_years)
    france_population = parse_population(france_data.values[0][1:index+1])
    belgium_population = parse_population(belgium_data.values[0][1:index+1])

    yticks = range(20, 70, 20)

    plt.plot(limited_years, france_population, label='France')
    plt.plot(limited_years, belgium_population, label='Belgium')
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.xticks(range(1800, 2050, 40))
    plt.xlim(1790, 2060)
    plt.ylabel('Population')
    plt.yticks(yticks, [f"{y}M" for y in yticks])
    plt.tight_layout()
    plt.legend()
    plt.savefig("France_Belgium.png")
#    plt.show()


if __name__ == "__main__":
    main()
