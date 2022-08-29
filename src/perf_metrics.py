import numpy as np
import pandas as pd


class Metrics:

    def __init__(self):
        pass
    
    def compute_cumulative_return(series: pd.Series) -> pd.Series:
        """
        -function annotation to indicate the func has a return type of Series data struct
        -function annotation to indicate that the func takes in a series obj as its parameters

        Calculates the return series of a given time series.

        >>> data = load_eod_data('VBB')
        >>> close_series = data['close']
        >>> return_series = return_series(close_series)

        The first value will always be NaN.
        """
        shifted_series = series.shift(1, axis=0)
        return series / shifted_series - 1

    def compute_return_percentage(series: pd.Series) -> float:
        """
        takes the first and last value in a return series and compute the return and converting the result to percentage
        assumes the return series is sorted in ascending order by dates
        """
        return (series.iloc[-1] / series.iloc[0] - 1) * 100
        

