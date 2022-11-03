import other_indicators
import mass_adopt
import base_funds
import oscillators
from datetime import datetime

f = open(datetime.now().date()+".txt", "w")
buy = 0
sell = 0

f.write("ДУМКА ТОВПИ\n")

if mass_adopt.mass_adopt() == 0:
	f.write("Товпа не вірить у криптовалютний ринок: КУПІВЛЯ\n\n")
	buy+=1
if mass_adopt.mass_adopt() == 1:
	f.write("Товпа занадто повірила у криптовалютний ринок: ПРОДАЖ\n\n")
	sell+=1
if mass_adopt.mass_adopt() == -1:
	f.write("Товпа не має однозначної оцінки\n\n")


f.write("СЛІДУВАННЯ ЗА ФУНДАМЕНТАЛЬНИМИ ПОКАЗНИКАМИ\n")
f.write("Очікуваний рух Біткоїна: " + str(base_funds.spx_dxy()) + "%\n\n")
if base_funds.spx_dxy() > 0:
	buy+=1
if base_funds.spx_dxy() < 0:
	sell+=1

f.write("ПОКАЗНИКИ ОСЦИЛЯТОРІВ\n")

if oscillators.oscilators_decision()[0] >= 2:
	f.write(str(buy) + " індикаторів вважають, що ринок перепроданий\n")
	f.write(str(sell) + " індикаторів вважають, що ринок перекуплений\n")
	f.write("Купувати\n")
	f.write("\n\n")
	buy+=oscillators.oscilators_decision()[0]
if oscillators.oscilators_decision()[1] >= 2:
	f.write(str(buy) + " індикаторів вважають, що ринок перепроданий\n")
	f.write(str(sell) + " індикаторів вважають, що ринок перекуплений\n")
	f.write("Продати\n")
	f.write("\n\n")
	sell+=oscillators.oscilators_decision()[1]

f.write("ІНШІ ІНДИКАТОРИ\n")
if other_indicators.moon() == -1:
	f.write("Крайні фази Луни ще не близько\n")
if other_indicators.moon() == 0:
	f.write("Новолуння близько: ПРОДАЖ\n")
	sell+=1
if other_indicators.moon() == 1:
	f.write("Повнолуння близько: КУПІВЛЯ\n")
	buy+=1


f.write(other_indicators.hash_ribbons() + " - остання дата рекомендації купівлі від hash ribbons\n\n")
buy+=1

f.write(str(buy) + " індикаторів за КУПІВЛЮ\n")
f.write(str(sell) + " індикаторів за ПРОДАЖ\n")
if Efficiency_Ratio > 0.65:
	f.write("РИНОК ОТРИМУЄ ЧІТКИЙ ТРЕНД")
if buy > 5:
	f.write("КУПУВАТИ")
if sell > 5:
	f.write("ПРОДАВАТИ")
if buy < 5 and sell < 5:
	f.write("РИНОК НА ДАНИЙ МОМЕНТ НЕЙТРАЛЬНИЙ")
if btc_volatility() > 7:
	f.write("РИНОК ЗАНАДТО ВОЛАТИЛЬНИЙ")


"""
среднеквадратическое отклонение
диаграммы idef0 по модели программы в Visio
"""