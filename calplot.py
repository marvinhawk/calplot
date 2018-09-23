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
	months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
	month_plot(dfp, months)

def week_table(ds):
	full_range = range_generator(ds)
	rds = ds.reindex(full_range.index)
	df = pd.DataFrame({"data": rds, "day": rds.index.weekday, "week": rds.index.week})
	dfp = df.pivot(index="week", columns="day", values="data")
	weekdays = ["M", "T", "W", "T", "F", "S", "S"]
	week_plot(dfp, weekdays)

def range_generator(ds):
	full_range = pd.Series(index=pd.date_range(ds.index[0] - MonthBegin(), ds.index[-1] + MonthEnd()))
	return full_range

def month_plot(df, ylabel="auto"):
	ymax = len(df.index)
	base_color = "#eaeaf2"
	shading = int(df.max().max())
	colors = sns.color_palette("GnBu", n_colors=shading)
	colors[0] = base_color
	sns.set()
	sns.set_style("whitegrid")
	plt.figure(figsize=(6,2))
	ax = sns.heatmap(df, cmap=colors, linewidth=.5, square=True, yticklabels=ylabel[:ymax])
	plt.xlabel("Day")
	plt.ylabel("Month")
	plt.title("Month-indexed Heatmap")
	plt.show()

def week_plot(df, xlabel="auto"):
	sns.set()
	ax = sns.heatmap(df, cmap="GnBu", linewidth=.5, square=True, xticklabels=xlabel)
	plt.xlabel("Weekday")
	plt.ylabel("Week")
	plt.title("Week-indexed Heatmap")
	plt.show()