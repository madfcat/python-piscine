import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter
import seaborn as sns
from load_csv import load


def convert_to_numeric(value):
    """
    Convert the value to a numeric value.
    """
    if value[-1] == 'M':
        return float(value[:-1]) * 1e6
    elif value[-1] == 'k':
        return float(value[:-1]) * 1e3
    else:
        return float(value)


def get_country_data_melted(country_name: str,
                            df: pd.DataFrame) -> pd.DataFrame:
    """
    Get country data in a long format.
    """

    # Filter the DataFrame for the specific country
    country_data = df[df['country'] == country_name]

    # Rshape from wide format to a long format
    country_data_melted = country_data.melt(
        id_vars=['country'], var_name='year', value_name='value')

    country_data_melted['value'] = country_data_melted['value'].apply(
        convert_to_numeric)

    country_data_melted['year'] = pd.to_numeric(country_data_melted['year'])

    return country_data_melted


def main():
    """
    Create a line plot of the population projections from countries list.
    """
    countries = ['Finland', 'Belgium']
    start_year = 1800
    end_year = 2050

    # Define a custom formatter function for the y-axis labels
    def millions_formatter(x, pos):
        return f'{x / 1e6:.0f}M'

    def filter_melted(df_melted, start_year, end_year):
        return df_melted[(
            df_melted['year'] >= start_year) & (df_melted['year'] <= end_year)]

    try:

        df = load("population_total.csv")

        df_melted = list(map(lambda country:
                             get_country_data_melted(country, df),
                             countries))

        # Filter the data for certain years
        df_melted_filtered = list(map(lambda country_melted: filter_melted(
            country_melted, start_year, end_year), df_melted))

        # Create the plot
        plt.figure(figsize=(8, 6))

        # Set the tick locations for the x-axis and y-axis
        ax = plt.gca()
        ax.xaxis.set_major_locator(MultipleLocator(40))
        max_population = max(
            melted['value'].max() for melted in df_melted_filtered
        )
        step_y = 20 * 1e6 if max_population > 20 * 1e6 else max_population / 5
        ax.yaxis.set_major_locator(MultipleLocator(step_y))

        # Apply the custom formatter to the y-axis
        ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))

        # Plot the data
        for melted_filtered in df_melted_filtered:
            sns.lineplot(data=melted_filtered, x='year', y='value',
                         label=melted_filtered['country'].iloc[0])

        # Set plot title and labels
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")

        # Place legend to the bottom right corner outside the plot
        plt.legend(loc='lower right')

        plt.show()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
