import datetime
import pandas as pd
from pandas.tseries.offsets import MonthBegin, MonthEnd
import seaborn as sns
import matplotlib.pyplot as plt

def month_table(ds):
	full_range = range_generator(ds)
	rds = ds.reindex(full_range.index).fillna(value=0)
	df = pd.DataFrame({"data": rds, "day": rds.index.day, "month": rds.index.month})
	dfp = df.pivot(index="month", columns="day", values="data")
	sns.set()
	sns.set_style("whitegrid")
	calplot(dfp)

def week_table(ds):
	full_range = range_generator(ds)
	rds = ds.reindex(full_range.index)
	df = pd.DataFrame({"data": rds, "day": rds.index.weekday, "week": rds.index.week})
	dfp = df.pivot(index="week", columns="day", values="data")
	sns.set()
	calplot(dfp)

def range_generator(ds):
	full_range = pd.Series(index=pd.date_range(ds.index[0] - MonthBegin(), ds.index[-1] + MonthEnd()))
	return full_range

def calplot(df):
	base_color = "#eaeaf2"
	shading = int(df.max().max())
	colors = sns.color_palette("OrRd", n_colors=shading)
	colors[0] = base_color

	ax = sns.heatmap(df, cmap=colors, linewidth=.5, square=True)
	plt.show()