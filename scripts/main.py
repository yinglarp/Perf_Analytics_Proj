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

#create an instance of the class PerfMetrics
pm = PerfMetrics()
print(pm.compute_cumulative_return(rtn_series))
print(pm.compute_annualization_factor(rtn_series,365.25))
print(pm.compute_annualized_return(rtn_series))

print(rtn_series.index[-1])
print(rtn_series.index[0])
print(rtn_series.index[-1] - rtn_series.index[0])