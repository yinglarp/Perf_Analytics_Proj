from tracemalloc import start
import numpy as np
import pandas as pd


class PerfMetrics:

    def __init__(self):
        pass
    
    def compute_daily_return(self, rtn_series: pd.Series) -> pd.Series:
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
        shifted_rtn_series = rtn_series.shift(1, axis=0)
        return (rtn_series / shifted_rtn_series).dropna(inplace=True) - 1

    def compute_return_percentage(self, rtn_series: pd.Series) -> float:
        """
        >>> takes the first and last value in a return series and compute the return and converting the result to percentage
        >>> assumes the return series is sorted in ascending order by dates
        """
        return (rtn_series.iloc[-1] / rtn_series.iloc[0] - 1) * 100
    
    def compute_annualization_factor(self, rtn_series: pd.Series, days_in_year: float) -> float:
        """
        >>> calculate the years within the period of analysis based on the date index of the dataframe obj for annualization
        >>> assumes the return series is indexed by date
        >>> days_in_year = 365.25
        """
        analysis_period_start_date = rtn_series.index[0]
        analysis_period_end_date = rtn_series.index[-1]
        annualization_factor = (analysis_period_end_date - analysis_period_start_date).days / days_in_year
        return annualization_factor

    def compute_annualized_return(self, price_series: pd.Series) -> float:
        """
        >>> calculate annualized return 
        """
        start_price = price_series.iloc[0]
        end_price = price_series.iloc[-1]
        pror_usd = end_price / start_price
        annul_factor = self.compute_annualization_factor(price_series)
        return (pror_usd ** (1 / annul_factor)) - 1

    def compute_cumulative_return(self, rtn_series:pd.Series) -> float:
        """
        >>> Input: return series with datetimeindex 
        >>> Return: chainlinked return series
        """
        return (rtn_series + 1).prod() - 1






