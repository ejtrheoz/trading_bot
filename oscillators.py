import numpy
import talib
import datetime
import pandas as pd

def oscilators_decision():
	df = pd.read_csv("BTC-USD.csv")

	closes = []
	highs = []
	lows = []

	PERIOD = 14
	RSI_OVERSOLD = 40
	RSI_OVERBOUGHT = 60

	AROON_LINE = 0

	WPR_BUY = -60
	WPR_SELL = -40

	STOCHASTIC_BUY = 40
	STOCHASTIC_SELL = 60


	for i in df["Close"]:
		closes.append(i)

	for i in df["High"]:
		highs.append(i)

	for i in df["Low"]:
		lows.append(i)

	np_closes = numpy.array(closes)
	np_highs = numpy.array(highs)
	np_lows = numpy.array(lows)

	rsi = talib.RSI(np_closes[-PERIOD-2:-1])
	aroondown, aroonup = talib.AROON(np_highs[-PERIOD-2:-1], np_lows[-PERIOD-2:-1])
	WPR = talib.WILLR(np_highs[-PERIOD-2:-1], np_lows[-PERIOD-2:-1], np_closes[-PERIOD-2:-1])
	slowk, slowd = talib.STOCH(np_highs[-PERIOD-2:-1], np_lows[-PERIOD-2:-1], np_closes[-PERIOD-2:-1], fastk_period=5, slowk_period=14, slowk_matype=0, slowd_period=3, slowd_matype=0)

	buy = 0
	sell = 0

	if rsi[-1] < RSI_OVERSOLD:
		buy+=1
	if rsi[-1] > RSI_OVERBOUGHT:
		sell+=1

	if aroonup[-1] - aroondown[-1] > AROON_LINE:
		buy+=1
	if aroonup[-1] - aroondown[-1] < AROON_LINE:
		sell+=1

	if WPR[-1] < WPR_BUY:
		buy+=1
	if WPR[-1] > WPR_SELL:
		sell+=1

	if slowk[-1] < STOCHASTIC_BUY:
		buy+=1
	if slowk[-1] > STOCHASTIC_SELL:
		sell+=1

	return (buy, sell, closes)

