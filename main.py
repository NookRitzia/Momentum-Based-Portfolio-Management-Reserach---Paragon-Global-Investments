import pandas
from pandas import DatetimeIndex

dti = pandas.DatetimeIndex(['2024-07-06'], tz='America/New_York')
dti = dti.tz_localize(None)
print(dti)