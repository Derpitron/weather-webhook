import time
import os
import requests
from dhooks import Webhook
from dotenv import load_dotenv
load_dotenv()
api_url = os.getenv('API')
hook = Webhook(os.getenv('HOOK'))
x = 0

while True:
	response = requests.get(api_url)
	data = response.json()
	rainData = data['rain']
	print("Polling the API")
	isRaining = "rain" in rainData

	if x == 0:
		isRaining2 = False

	def rainCheck():
		if ((isRaining) and (isRaining != isRaining2)):
			hook.send("THE CLOUD HAS ARIVED")
			hook.send("JJJJJJJJJJJJJJJJ")

	def send():
		rainCheck()

	isRaining2 = isRaining
	send()
	x += 1
	time.sleep(300)