import datetime
import pandas as pd
from pandas.tseries.offsets import MonthBegin, MonthEnd
import seaborn as sns
import matplotlib.pyplot as plt

def month_table(ds):
	full_range = range_generator(ds)
	rds = ds.reindex(full_range.index)
	df = pd.DataFrame({"data": rds, "day": rds.index.day, "month": rds.index.month})
	dfp = df.pivot(index="month", columns="day", values="data")
	calplot(dfp)

def week_table(ds):
	full_range = range_generator(ds)
	rds = ds.reindex(full_range.index)
	df = pd.DataFrame({"data": rds, "day": rds.index.weekday, "week": rds.index.week})
	dfp = df.pivot(index="week", columns="day", values="data")
	calplot(dfp)

def range_generator(ds):
	full_range = pd.Series(index=pd.date_range(ds.index[0] - MonthBegin(), ds.index[-1] + MonthEnd()))
	return full_range

def calplot(df):
	sns.set()
	ax = sns.heatmap(df, cmap="Greens", linewidth=.5, square=True)
	plt.show()