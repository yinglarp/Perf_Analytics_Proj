import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

current_date = datetime.now()
print('Current Date:', current_date.strftime("%Y-%m-%d"))

date_after_one_year = current_date + timedelta(days=365)
print('After One Year Date from Now:', date_after_one_year)

date_before_five_days = current_date - timedelta(days=5)
print(type(date_before_five_days))
print('Date before Five Days from Now:', date_before_five_days) 

class Timespan():

    def __init__(self):
        pass

    def derive_start_dt_D_timespan(self, analysis_period_end_dt: datetime, day_periods:int) -> datetime:
        """
        Derive the analysis_period_start_dt based on x periods of Days from analysis_period_end_dt

        >>> input: analysis_period_end_dt datetime object
        >>> input: number of days to subtract from analysis_period_end_dt
        >>> output: analysis_period_start_dt datetime object
        """

        return (analysis_period_end_dt - timedelta(days=day_periods)).strftime("%Y-%m-%d")

    def derive_start_dt_W_timespan(self, analysis_period_end_dt: datetime, week_periods:int) -> datetime:
        """
        Derive the analysis_period_start_dt based on x periods of Weeks from analysis_period_end_dt

        >>> input: analysis_period_end_dt datetime object
        >>> input: number of weeks to subtract from analysis_period_end_dt
        >>> output: analysis_period_start_dt datetime object
        """

        return (analysis_period_end_dt - timedelta(weeks=week_periods)).strftime("%Y-%m-%d")       

    def derive_start_dt_M_timespan(self, analysis_period_end_dt: datetime, month_periods:int) -> datetime:
        """
        Derive the analysis_period_start_dt based on x periods of Months from analysis_period_end_dt

        >>> input: analysis_period_end_dt datetime object
        >>> input: number of months to subtract from analysis_period_end_dt
        >>> output: analysis_period_start_dt datetime object
        """

        return (analysis_period_end_dt - relativedelta(months=month_periods)).strftime("%Y-%m-%d")   

    def derive_start_dt_Y_timespan(self, analysis_period_end_dt: datetime, year_periods:int) -> datetime:
        """
        Derive the analysis_period_start_dt based on x periods of Years from analysis_period_end_dt

        >>> input: analysis_period_end_dt datetime object
        >>> input: number of years to subtract from analysis_period_end_dt
        >>> output: analysis_period_start_dt datetime object
        """

        return (analysis_period_end_dt - relativedelta(years=year_periods)).strftime("%Y-%m-%d")   