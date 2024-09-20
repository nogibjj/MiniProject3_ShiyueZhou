from main import generate_descriptive_statistics, generate_summary_statistics
import polars as pl

url = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"


def test_generate_descriptive_statistics_in_Polars():
    """testing out generate_descriptive_statistics function"""
    df = pl.read_csv(url)
    des_stat = generate_descriptive_statistics(df)
    # print(des_stat["Mortality rate, infant (per 1,000 live births)"])

    # # Check if the counts are correct
    assert round(des_stat["Mortality rate, infant (per 1,000 live births)"][0]) == 193

    # # Check if the mean is correct
    assert round(des_stat["Mortality rate, infant (per 1,000 live births)"][2]) == 23

    # # Check if the min is correct
    assert round(des_stat["Mortality rate, infant (per 1,000 live births)"][4]) == 2


def test_generate_summary_statistics_in_Polars():
    """testing out generate_summary_statistics function"""
    df = pl.read_csv(url)
    summary_stat = generate_summary_statistics(df)

    # Check if the mean of column1 and column2 are correct
    assert (
        round(
            summary_stat["mean"][
                "Mortality rate, infant (per 1,000 live births)"
            ].item()
        )
        == 23
    )

    # Check if the median is correct
    assert (
        round(
            summary_stat["median"][
                "Mortality rate, infant (per 1,000 live births)"
            ].item()
        )
        == 16
    )
    # Check if the standard deviation is correct
    assert (
        round(
            summary_stat["std"]["Mortality rate, infant (per 1,000 live births)"].item()
        )
        == 21
    )


if __name__ == "__main__":
    test_generate_descriptive_statistics_in_Polars()
    test_generate_summary_statistics_in_Polars()
