import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import seaborn as sns
from load_csv import load


def show_country_graph(country_name: str) -> None:
    df = load("life_expectancy_years.csv")

    # Filter the DataFrame for the specific country
    country_data = df[df['country'] == country_name]

    # Rshape from wide format to a long format
    country_data_melted = country_data.melt(
        id_vars=['country'], var_name='year', value_name='value')
    country_data_melted['year'] = pd.to_numeric(
        country_data_melted['year'])

    # Create the plot
    plt.figure(figsize=(8, 6))

    # Set the tick locations for the x-axis and y-axis
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(40))
    ax.yaxis.set_major_locator(MultipleLocator(10))

    # Plot the data
    sns.lineplot(data=country_data_melted, x='year', y='value')

    # Set plot title and labels
    plt.title(f"{country_name} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    plt.show()


def main():
    try:
        show_country_graph('Finland')

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
