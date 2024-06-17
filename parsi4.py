import requests
from bs4 import BeautifulSoup
import json

base_url = "https://timing.batyrshin.name/tracks/narvskaya/karts?m=times&p="


def get_karting_data(period):
	url = base_url + period
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	rows = soup.find_all('tr')
	results = []

	def convert_time_to_seconds(time_str):
		if ':' in time_str:
			minutes, seconds = time_str.split(':')
			return int(minutes) * 60 + float(seconds)
		else:
			return float(time_str)

	for row in rows:
		columns = row.find_all('td')
		if len(columns) > 4:
			kart_number = columns[0].find('span', class_='kart').text.strip()
			lap_time = convert_time_to_seconds(columns[1].text.strip())
			driver_name = columns[2].find('a').text.strip()
			heat_name = columns[3].find('b').text.strip()
			race_time = columns[4].text.strip()

			if 48.5 < lap_time < 51:
				results.append({
					"kart_number": kart_number,
					"lap_time": lap_time,
					"driver_name": driver_name,
					"heat_name": heat_name,
					"race_time": race_time
				})

	results_sorted = sorted(results, key=lambda x: x['lap_time'])
	return results_sorted


for period in ['1d', '7d', '14d']:
	data = get_karting_data(period)
	with open(f'karting_data_{period}.json', 'w') as json_file:
		json.dump(data, json_file, indent=4)

#print("Data saved for 1d, 7d, and 14d periods")
