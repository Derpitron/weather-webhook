import time
import requests
from dhooks import Webhook

hook = Webhook("https://discord.com/api/webhooks/864098878671814666/Kwu2gG373bBfWIR8t40cWb36bQgKdwHr9C-YfgnqYAVIiJHT9b_CKfEbfbgjfsV4yvE2")
url = 'http://api.openweathermap.org/data/2.5/weather?id=1264527&appid=0fd54c8d93dff4248d776d5644ef0946&units=metric'

while True:
	res = requests.get(url)
	data = res.json()
	weatherID1 = data['weather'][0]['id']
	cloud1 = data['clouds']['all']
	validWeather = ["200","201","202","210","211","212","221","230","231","232","300","301","302","310","311","312","313","314","321","503","504","511","520","521","522","530"]

	def rainCheck():
		if (weatherID1 in validWeather) and (weatherID2 in validWeather == 0):
			hook.send("THE CLOUD HAS ARIVED")
			hook.send("JJJJJJJJJJJJJJJJ")

	def cloudCheck():
    		if (((cloud1 >= 85) and (cloud1 <= 100)) and (weatherID1 in validWeather == 0) and ((cloud2 < 85))):
    			hook.send("DARKNESS RISES")	

	def send():
		rainCheck()
		cloudCheck()
		
	send()
	time.sleep(300)
	weatherID2 = weatherID1
	cloud2 = cloud1