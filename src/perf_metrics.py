from tracemalloc import start
import numpy as np
import pandas as pd


class PerfMetrics:

    def __init__(self):
        pass
    
    def compute_daily_return(self, price_series: pd.Series) -> pd.Series:
        """
        -function annotation to indicate the func has a return type of Series data struct
        -function annotation to indicate that the func takes in a series obj as its parameters

        Calculates the return series of a given time series.

        >>> data = load_eod_data('TSLA')
        >>> close_series = data['close']
        >>> return_series = return_series(close_series)

        The first value will always be NaN.
        Drop all NAN values using drop method -> df.dropna(inplace = True) or fill_value=0 (I.e. price_series.shift(1, axis=0, fill_value=0))
        """
        shifted_price_series = price_series.shift(1, axis=0)
        rtn_series_daily = (price_series / shifted_price_series) - 1
        return rtn_series_daily

    def compute_return_percentage(self, price_series: pd.Series) -> float:
        """
        >>> takes the first and last value in a return series and compute the return and converting the result to percentage
        >>> assumes the return series is sorted in ascending order by dates
        """
        return (price_series.iloc[-1] / price_series.iloc[0] - 1) * 100
    
    def compute_annualization_factor(self, rtn_series: pd.Series, days_in_year: float) -> float:
        """
        >>> calculate the years within the period of analysis based on the date index of the dataframe obj for annualization
        >>> assumes the return series is indexed by date
        >>> days_in_year = 365.25
        """
        analysis_period_start_date = rtn_series.index[0]
        analysis_period_end_date = rtn_series.index[-1]
        days_count = (analysis_period_end_date - analysis_period_start_date).days + 1 
        if (days_count <= days_in_year):
            annualization_factor = 1
        else:
            annualization_factor = (analysis_period_end_date - analysis_period_start_date).days + 1 / days_in_year
        return annualization_factor
   
    def compute_cumulative_return(self, rtn_series:pd.Series) -> float:
        """
        >>> Input: return series with datetimeindex 
        >>> Output: chainlinked return series
        """
        return (1 + rtn_series).prod() - 1

    def compute_annualized_return(self, rtn_series: pd.Series) -> float:
        """
        >>> calculate annualized return 
        """
        cumulative_rtn = self.compute_cumulative_return(rtn_series)
        annul_factor = self.compute_annualization_factor(rtn_series,365.25)
        return ((1 + cumulative_rtn) ** annul_factor) - 1

    def compute_rolling_return(self, rtn_series:pd.Series, rolling_period:int) -> pd.Series:
        """
        func to compute rolling returns for a return series based on the defined periods

        >>> Input: return series with datetimeindex 
        >>> Input: integer to indicate periods to roll I.e. 3/5/7
        >>> Output: rolling returns based on rolling_period
        """

        return (rtn_series.rolling(rolling_period, min_periods=1).apply(np.prod))

    def compute_rolling_cumulative_return(self, rtn_series:pd.Series) -> pd.Series:
        """
        func to compute cumulative and rolling returns for a return series with period=1, axis=0

        >>> Input: return series with datetimeindex
        >>> Output: rolling cumulative returns based on return series datetimeindex
        """

        return (np.cumprod(1 + rtn_series) - 1)

    def compute_rolling_cumulative_return_periods(self, rtn_series:pd.Series, rolling_period:int) -> pd.Series:
        '''
        func to compute rolling cumulative returns for a return series with periods = rolling_period

        >>> Input: return series with datetimeindex 
        >>> Input: integer to indicate periods to roll I.e. 3/5/7
        >>> Output: rolling cumulative returns based on rolling_period
        '''

        return ((1 + rtn_series).rolling(rolling_period, min_periods=1).apply(np.prod) - 1)




 

