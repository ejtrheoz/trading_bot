import requests
from pytrends.request import TrendReq


"""
0 - disbelieve
1 - believe
-1 - average
"""


def mass_adopt():
	s = requests.get("https://alternative.me/crypto/fear-and-greed-index/")
	find_word_index = s.text.find('<div class="gray">Now</div>')

	greed_and_fear = int(s.text[find_word_index+197:find_word_index+199])

	pytrends = TrendReq(hl='en-US', tz=360) 
	kw_list = ["crypto"]

	pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m') 

	data = pytrends.interest_over_time() 
	data = data.reset_index() 
	last_index = len(data['crypto'])
	last_thought = data['crypto'][last_index-1]

	if greed_and_fear < 25 and last_thought <= 30:
		return 0
	if greed_and_fear > 90 and last_thought > 80:
		return 1
	return -1
