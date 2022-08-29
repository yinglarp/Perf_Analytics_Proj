from tracemalloc import start
import numpy as np
import pandas as pd


class Metrics:

    def __init__(self):
        pass
    
    def compute_daily_return(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        -function annotation to indicate the func has a return type of Series data struct
        -function annotation to indicate that the func takes in a series obj as its parameters

        Calculates the return series of a given time series.

        >>> data = load_eod_data('VBB')
        >>> close_series = data['close']
        >>> return_series = return_series(close_series)

        The first value will always be NaN.
        Drop all NAN values using drop method -> df.dropna(inplace = True)
        """
        shifted_df = df.shift(1, axis=0)
        return (df / shifted_df).dropna(inplace=True) - 1

    def compute_return_percentage(self, df: pd.DataFrame) -> float:
        """
        >>> takes the first and last value in a return series and compute the return and converting the result to percentage
        >>> assumes the return series is sorted in ascending order by dates
        """
        return (df.iloc[-1] / df.iloc[0] - 1) * 100
    
    def compute_annualization_factor(self, df: pd.DataFrame, days_in_year: float) -> float:
        """
        >>> calculate the years within the period of analysis based on the date index of the dataframe obj for annualization
        >>> assumes the return series is indexed by date
        >>> days_in_year = 365.25
        """
        analysis_period_start_date = df.index[0]
        analysis_period_end_date = df.index[-1]
        annualization_factor = (analysis_period_end_date - analysis_period_start_date).days / days_in_year
        return annualization_factor

    def compute_annualized_return(self, df: pd.DataFrame) -> float:
        """
        >>> calculate annualized return 
        """
        start_price = df.iloc[0]
        end_price = df.iloc[-1]
        pror_usd = end_price / start_price
        annul_factor = self.compute_annualization_factor(df)
        return (pror_usd ** (1 / annul_factor)) - 1





