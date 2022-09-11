import pandas as pd
import numpy as np
from datetime import datetime, timedelta

current_date = datetime.now()
print('Current Date:', current_date.strftime("%Y-%m-%d"))

date_after_one_year = current_date + timedelta(days=365)
print('After One Year Date from Now:', date_after_one_year)

date_before_five_days = current_date - timedelta(days=5)
print(type(date_before_five_days))
print('Date before Five Days from Now:', date_before_five_days) 

class timespan():

    def __init__(self, current_date=datetime.now()):
        return current_date.strftime("%Y-%m-%d")

    def derive_start_dt_D_timespan(self, analysis_period_end_dt: datetime, days_periods:int) -> datetime:
        """
        Derive the analysis_period_start_dt based on x periods of Days from analysis_period_end_dt

        >>> input: analysis_period_end_dt datetime object
        >>> input: number of days to subtract from analysis_period_end_dt
        >>> output: analysis_period_start_dt datetime object
        """

        return (analysis_period_end_dt - timedelta(days=days_periods)).strftime("%Y-%m-%d")


