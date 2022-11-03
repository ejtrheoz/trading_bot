import pandas as pd

def spx_dxy():
	df = pd.read_csv("S&P 500 Historical Data.csv")
	spx = float(df["Change %"][0][0:-1])*2.5

	df = pd.read_csv("Download Data - INDEX_US_IFUS_DXY.csv")

	dxy = ((float(df["Close"][0]) / float(df["Close"][1]))-1) * -600
	return (dxy + spx)/2
