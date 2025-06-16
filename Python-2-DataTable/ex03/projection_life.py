from load_csv import load
import matplotlib.pyplot as plt


def main():

    """

    """

    file1 = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    file2 = "life_expectancy_years.csv"
    dataset1 = load(file1)
    dataset2 = load(file2)

    year = "1900"
    gdp = dataset1[["country", year]].copy()
    life_exp = dataset2[["country", year]].copy()

    merged = gdp.merge(life_exp, on="country", suffixes=("_gdp", "_life"))
    merged = merged.dropna()
    merged[year + "_gdp"] = merged[year + "_gdp"].astype(float)
    merged[year + "_life"] = merged[year + "_life"].astype(float)

    plt.scatter(merged[year + "_gdp"], merged[year + "_life"])
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.ylabel('Life Expectancy')
    plt.yticks(range(20, 56, 5))
    plt.ylim(18, 55)
    plt.tight_layout()
    plt.savefig("1900.png")
#    plt.show()


if __name__ == "__main__":
    main()
