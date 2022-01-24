from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

def _get_info(URL, choice):
	choice = choice
	if choice == 1 or choice == 2 or choice == 3:
		req = requests.get(URL)
		soup = BeautifulSoup(req.text, "html.parser")
		vehicle_container = soup.find("div", {"id":"vehicle-cards-container"})
		per_car = vehicle_container.find_all("div", {"class":"vehicle-card-with-reviews"})
		client_choice = input("write info in file or just show ?(write/show)\n:")
		if client_choice.lower() == "write":
			car_info = ["Data"]
			for i in per_car:
				my_dict = {}
				my_dict["Car Model"] = i.find("h2", {"class":"title"}).text.strip()
				my_dict["Miles"] = i.find("div", {"class":"mileage"}).text.strip()
				my_dict["Car Price"] = i.find("span", {"class":"primary-price"}).text.strip()
				my_dict["Dealer Name"] = i.find("div", {"class":"dealer-name"}).text.strip()
				car_info.append(my_dict)
			
			j = json.dumps(car_info)
			with open("Cars.json", "w") as f:
				f.write(j)
				f.close()

			client_choice_2 = input("Do you want to read file?(Yes/No): ")

			if client_choice_2.lower() == "yes":
				info_of_cars = json.load(open("Cars.json"))
				print(info_of_cars)

		elif client_choice.lower() == "show":
			car_info = []
			for i in per_car:
				my_dict = {}
				my_dict["Car Model"] = i.find("h2", {"class":"title"}).text.strip()
				my_dict["Miles"] = i.find("div", {"class":"mileage"}).text.strip()
				my_dict["Car Price"] = i.find("span", {"class":"primary-price"}).text.strip()
				my_dict["Dealer Name"] = i.find("div", {"class":"dealer-name"}).text.strip()
				car_info.append(my_dict)
			df = pd.DataFrame(car_info)
			print(df)
	elif choice == 4:
		req = requests.get(URL)
		soup = BeautifulSoup(req.text, "html.parser")
		main_container = soup.find("div", {"class":"card-container"})
		each_car = main_container.find_all("li", {"class":"card-list-item"})
		client_choice = input("write info in file or just show ?(write/show)\n:")
		if client_choice.lower() == "write":
			car_info = []
			for i in each_car:
				my_dict = {}
				my_dict["Car Year"] = i.find("span", {"class":"card-date"}).text.strip()
				my_dict["Car Model"] = i.find("h3", {"class":"card-vehicle-name"}).text.strip()
				my_dict["Starting MSPR"] = i.find("strong", {"class":"card-price"}).text.strip()
				car_info.append(my_dict)

			j = json.dumps(car_info)
			with open("Cars.json", "w") as f:
				f.write(j)
				f.close()

			client_choice_2 = input("Do you want to read file?(Yes/No): ")

			if client_choice_2.lower() == "yes":
				info_of_cars = json.load(open("Cars.json"))
				print(info_of_cars)	
		elif client_choice.lower() == "show":
			car_info = []
			for i in each_car:
				my_dict = {}
				my_dict["Car Year"] = i.find("span", {"class":"card-date"}).text.strip()
				my_dict["Car Model"] = i.find("h3", {"class":"card-vehicle-name"}).text.strip()
				my_dict["Starting MSPR"] = i.find("strong", {"class":"card-price"}).text.strip()
				car_info.append(my_dict)
			df = pd.DataFrame(car_info)
			print(df)

print("\nChoose The Car You Want to see!\n")
print("1.Ford F-150")
print("2.BMW M3")
print("3.Chevrolet_Camaro")
print("4.Electric Cars")
client_choice = int(input("\nEnter Your Choice: "))
if client_choice < 5:
	dict_of_links = {1: 'https://www.cars.com/shopping/ford-f_150/',
										2: 'https://www.cars.com/shopping/bmw-m3/',
										3: 'https://www.cars.com/shopping/chevrolet-camaro/',
										4: 'https://www.cars.com/electric-cars/'}
	_get_info(dict_of_links[client_choice], client_choice)
elif client_choice > 4:
	print("Sorry !")


