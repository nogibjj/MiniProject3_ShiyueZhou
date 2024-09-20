import polars as pl
import pandas as pd
import matplotlib.pyplot as plt

url = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"


# data loading using pandas
def load_data_pandas(link):
    data = pd.read_csv(link)
    return data


# data loading using polars
def load_data_polars(link):
    data = pl.read_csv(link)
    return data


# data descriptive can be use in both cases
def generate_descriptive_statistics(data):
    des_stat = data.describe()
    return des_stat


def generate_summary_statistics(filter_data):
    summary_stat = {
        "mean": filter_data.mean(),
        "median": filter_data.median(),
        "std": filter_data.std(),
    }
    return summary_stat


def main():
    df_Pl = load_data_polars(url)
    df_PD = load_data_pandas(url)
    df_filtered_pl = df_Pl[
        [
            "Mortality rate, infant (per 1,000 live births)",
            "GDP per capita (constant 2010 US$)",
        ]
    ]
    df_filtered_pd = df_PD[
        [
            "Mortality rate, infant (per 1,000 live births)",
            "GDP per capita (constant 2010 US$)",
        ]
    ]

    # 1 descriptive statistics in Polars
    des_stat_pl = generate_descriptive_statistics(df_filtered_pl)
    print("Descriptive Statistics:\n", des_stat_pl)

    # 2 summary statistics in Polars
    summary_stat_pl = generate_summary_statistics(df_filtered_pl)
    print("\nSummary Statistics:\n", summary_stat_pl)

    # 3 Visualization in Pandas
    df_filtered_pd.plot.scatter(
        x="GDP per capita (constant 2010 US$)",
        y="Mortality rate, infant (per 1,000 live births)",
        title="Infant Mortality Against GDP per Capita",
    )
    print("\nVisualization:\n")
    plt.savefig("plot_from_data.png")


def save_to_md():
    main()
    df_Pl = load_data_polars(url)
    describe_df_PL = generate_descriptive_statistics(df_Pl)
    markdown_tablePL = str(describe_df_PL)

    # Write the markdown table to a file
    with open("DescribeStat Polar.md", "a") as file:
        file.write("Describe Polar DF:\n")
        file.write(markdown_tablePL)
        file.write("\n\n")
        file.write("![congress_viz](plot_from_data.png)\n")


if __name__ == "__main__":
    save_to_md()
