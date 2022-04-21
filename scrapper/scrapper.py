from bs4 import BeautifulSoup
import requests
import json


class Scrapper:
	def __init__(self, url, main_URL):
		self.url = url
		self.main_URL = main_URL

	def write_in_json(self, data_list):
		data = json.dumps(data_list, indent=4, sort_keys=True)
		with open("Data.json", "w") as fw:
			fw.write(data)
			fw.close()

	def json_reader(self):
		with open('Data.json', 'r') as fr:
			info = json.load(fr)
			pt_info = json.dumps(info, indent=4, sort_keys=True)

		print(pt_info)


	def parser(self, user_choice):
		Data = json.load(open('data_ti_li.json'))
		URL = Data[user_choice]["Link"]
		title = Data[user_choice]["Title"]
		if title == 'Electric cars':
			req = requests.get(URL)
			soup = BeautifulSoup(req.text, "html.parser")
			main_container = soup.find("div", {"class":"card-container"})
			each_car = main_container.find_all("li", {"class":"card-list-item"})
			cars_list = ["Cars Data"]
			for index, item in enumerate(each_car):
				cars_dictionary = {}
				cars_dictionary['Year'] =item.find("span", {"class":"card-date"}).text.strip()
				cars_dictionary['Model'] = item.find("h3", {"class":"card-vehicle-name"}).text.strip()
				cars_dictionary['Price'] = item.find("strong", {"class":"card-price"}).text.strip()
				cars_list.append(cars_dictionary)
			return cars_list

		else:
			req = requests.get(URL)
			soup = BeautifulSoup(req.text, "html.parser")
			vehicle_container = soup.find("div", {"id":"vehicle-cards-container"})
			per_car = vehicle_container.find_all("div", {"class":"vehicle-card-with-reviews"})
			cars_list = ["Cars Data"]
			for item in per_car:
				cars_dictionary = {}
				cars_dictionary['Title'] = item.find("h2", {"class":"title"}).text.strip()
				cars_dictionary['Mileage'] = item.find("div", {"class":"mileage"}).text.strip()
				cars_dictionary['Price'] = item.find("span", {"class":"primary-price"}).text.strip()
				cars_dictionary['Dealer Name'] = item.find("div", {"class":"dealer-name"}).text.strip()
				cars_list.append(cars_dictionary)

			return cars_list

	def titles_links(self, data):
		data_ti_li = json.dumps(data, indent=4, sort_keys=True)
		with open('data_ti_li.json', 'w') as fw:
			fw.write(data_ti_li)
			fw.close()

	def get_URLs(self):
		req = requests.get(self.url)
		soup = BeautifulSoup(req.text, "html.parser")
		cars_container = soup.find("div", {"class":"sds-page-section__content searches-near-you"})
		cars_data = cars_container.find_all("div", {"class":"sds-card sds-card--research"})
		list_of_data = []
		for infos in cars_data:
			dictionary = {}
			dictionary["Link"] = self.main_URL + infos.find("a")["href"]
			dictionary["Title"] = infos.find("h4", {"class":"sds-card__title"}).text.strip()
			list_of_data.append(dictionary)

		return list_of_data

	def make_choice(self):
		data = json.load(open('data_ti_li.json'))
		for i in range(0, len(data)):
			print(str(i+1) + '. ' + data[i]["Title"])

		user_choice = int(input("Enter your choice: "))
		return user_choice - 1




URL = 'https://www.cars.com/shopping/'
main_url = 'https://www.cars.com'

scrapper = Scrapper(URL, main_url)
scrapper.get_URLs()
scrapper.titles_links(scrapper.get_URLs())
scrapper.write_in_json(scrapper.parser(scrapper.make_choice()))
scrapper.json_reader()
