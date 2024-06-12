import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from load_csv import load


# Define a formatting function for the tick labels
def format_func(value, tick_number):
    """
    Formats the tick labels of the plot.
    """
    if value >= 1000:
        return f'{int(value/1000)}k'
    else:
        return f'{int(value)}'


def main():
    """
    Main function that loads the data, extracts the data for the specified
    year, merges the two DataFrames, creates a scatter plot, sets the
    logarithmic scale for the x-axis, applies the custom formatter to the x
    and y axes, sets the plot title and labels, and displays the plot.
    """
    # Specify the year you want to extract
    year_to_extract = '1900'

    try:
        df_life = load("life_expectancy_years.csv")
        df_gdp = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

        # Extract data for the specified year from both DataFrames
        df_life_by_year = df_life[['country', year_to_extract]].copy()
        df_gdp_by_year = df_gdp[['country', year_to_extract]].copy()

        # Rename the columns for clarity
        df_life_by_year.columns = ['country', 'life_expectancy_1900']
        df_gdp_by_year.columns = ['country', 'gdp_1900']

        # Merge the two DataFrames on the 'country' column
        merged_df = pd.merge(df_life_by_year, df_gdp_by_year, on='country')

        # Convert columns to numeric
        merged_df['gdp_1900'] = pd.to_numeric(merged_df['gdp_1900'])
        merged_df['life_expectancy_1900'] = pd.to_numeric(
            merged_df['life_expectancy_1900'])

        # Create the plot
        plt.figure(figsize=(8, 6))

        plt.scatter(merged_df['gdp_1900'], merged_df['life_expectancy_1900'])

        # Set logarithmic scale for x and y axes
        plt.xscale('log')

        # Apply the custom formatter
        plt.gca().xaxis.set_major_formatter(FuncFormatter(format_func))
        plt.gca().yaxis.set_major_formatter(FuncFormatter(format_func))

        # Set plot title and labels
        plt.title("1900")
        plt.xlabel("Gross Domestic product")
        plt.ylabel("Life Excpectancy")

        plt.show()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
