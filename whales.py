import configparser
import json
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)
class counter():
	counter_down = 0
	counter_up = 0
		
api_id = "1145697"
api_hash = "6b614a55e1fbce5d6b4e917d9a63f280"
client = TelegramClient("user", api_id, api_hash)

client.start()

user_input_channel = ['https://t.me/CryptoCoinsCoach', "https://t.me/Crypto_Swings", "https://t.me/whale_alert_io", "https://t.me/WhaleSniper", "https://t.me/BinanceLiquidations", "https://t.me/awiat"]

@client.on(events.NewMessage(chats=user_input_channel))
async def normal_handler(event):
	newMessage = event.message.message
	if ("MicroStrategy" in newMessage) and ("buy" in newMessage):
		print("Очікується падіння BTC на 5%")
	if ("MicroStrategy" in newMessage) and ("sell" in newMessage):
		print("Очікується зростання BTC на 5%")
	if ("Barry Silbert" in newMessage) and ("buy" in newMessage):
		print("Очікується падіння BTC на 5%")
	if (("BTC" in newMessage) or ("Bitcoin" in newMessage))  and ("allow" in newMessage):
		print("Очікується зростання BTC на 3%")
	if (("BTC" in newMessage) or ("Bitcoin" in newMessage))  and ("allow" in newMessage):
		print("Очікується зростання BTC на 3%")
	if "Chin" in newMessage and (("ban" in newMessage) or ("FUD" in newMessage)):
		print("Зростання Біткоїна у довгостроковому режимі")
	if "El" in newMessage and "Salvador" in newMessage:
		print("Очікується зростання BTC на 4%")
	if "FED" in newMessage and ("HIKE" in newMessage or "RAISE" in newMessage or "raise" in newMessage):
		print("Зростання Біткоїна на 4%")
	if (("BTC" in newMessage) or ("Bitcoin" in newMessage)) and "ETF" in newMessage:
		print("Очікується зростання BTC на 5%")
	if ("transferred from #" in newMessage) and ("BTC" in newMessage or "ETH" in newMessage):
		counter.counter_up+=1
	if ("transferred from unknown wallet" in newMessage) and ("BTC" in newMessage or "ETH" in newMessage):
		counter.counter_down+=1 
	if ("#BTC" in newMessage or "#ETH" in newMessage) and ("Unusual selling activity" in newMessage):
		counter.counter_down+=1
	if ("#BTC" in newMessage or "#ETH" in newMessage) and ("Unusual buying activity" in newMessage):
		counter.counter_up+=1
	if ("#BTC" in newMessage or "#ETH" in newMessage) and ("Liquidated Long" in newMessage):
		counter.counter_up+=1
	if ("#BTC" in newMessage or "#ETH" in newMessage) and ("Liquidated Short" in newMessage):
		counter.counter_down+=1
	print(counter.counter_up, counter.counter_down)
	if counter.counter_down >= 10:
		print("Загальний ведмежий настрій у китів")
	if counter.counter_up >= 10:
		print("Загальний бичачий настрій у китів")

with client:
	client.run_until_disconnected()
