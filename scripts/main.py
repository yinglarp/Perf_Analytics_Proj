from importlib.metadata import entry_points
import numpy as np
import pandas as pd
from datetime import datetime
from src.perf_metrics import PerfMetrics

dates = [datetime(2022,8,1),datetime(2022,8,2),datetime(2022,8,3),datetime(2022,8,4),datetime(2022,8,5),datetime(2022,8,6),datetime(2022,8,7),datetime(2022,8,8)]
rtn_series = pd.Series(np.random.randn(8), index=dates)
print(rtn_series)
print(rtn_series.index)
print((rtn_series+1).prod()-1)
print(rtn_series.rolling(2).apply(np.prod)) #rolling returns for n number of periods
print(np.cumprod(1 + rtn_series) -1) #rolling cumulative returns for daily/weekly/monthly based on df.index
print(rtn_series.rolling(2).apply(np.prod).shift(0))



#create an instance of the class PerfMetrics
pm = PerfMetrics()
print(pm.compute_cumulative_return(rtn_series))
print(pm.compute_annualization_factor(rtn_series,365.25))
print(pm.compute_annualized_return(rtn_series))
print(pm.compute_rolling_cumulative_return(rtn_series))
print(pm.compute_rolling_cumulative_return_periods(rtn_series,2))
print(pm.compute_rolling_return(rtn_series,2))

print(len(rtn_series))
print((rtn_series.index[-1] - rtn_series.index[0]).days + 1)

df = pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [10, 20, 30, 40, 50]
})
print(df)
print(df.shift(0))
print(df.shift(1,axis=0,fill_value=0))

