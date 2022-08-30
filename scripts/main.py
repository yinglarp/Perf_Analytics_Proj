import numpy as np
import pandas as pd
from datetime import datetime
import src.perf_metrics as pm

dates = [datetime(2022,8,1),datetime(2022,8,2),datetime(2022,8,3),datetime(2022,8,4),datetime(2022,8,5),datetime(2022,8,6),datetime(2022,8,7),datetime(2022,8,8)]
rtn_series = pd.Series(np.random.randn(8), index=dates)
print(rtn_series)
print(rtn_series.index)
print(rtn_series.prod())
print(pm.PerfMetrics.compute_cumulative_return(rtn_series))

