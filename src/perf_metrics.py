import numpy as np
import pandas as pd


class Metrics:

    def __init__(self):
        pass
    
    def calculate_return_series(series: pd.Series) -> pd.Series:
        """
        Calculates the return series of a given time series.

        >>> data = load_eod_data('VBB')
        >>> close_series = data['close']
        >>> return_series = return_series(close_series)

        The first value will always be NaN.
        """
        shifted_series = series.shift(1, axis=0)
        return series / shifted_series - 1
