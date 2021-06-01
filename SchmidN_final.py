# Schmid, Nick
# Draft 1 of final project

# Importing packages

# For requesting connection to API
import requests 
# For time delay to read before executing script
import time
# For printing JSON data in a readable format, use "pprint".
from pprint import pprint

# Define the Main function
def main():
	print("Welcome! Let's check the weather for the next 5 days, in 3 hour increments.")

# Choice - If using city, use City URL, if using zip, use Zip URL.
	city = str(input('What city or zip code? '))
	try:
		url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=21bce4c53b3b224b83041276ac99f782'.format(city)
	except: 
		url = 'http://api.openweathermap.org/data/2.5/forecast?zip={}&appid=21bce4c53b3b224b83041276ac99f782'.format(city)

# Notify user if connection was successful or failed..
	try:
		res = requests.get(url)
		print('Connection successful')
	except:
		print('Connection failed.')
#Time to view connection status
	time.sleep(2)
# Return the JSON data from the Open Weather site.
	data = res.json()
#Print the response and the data
	print(res)
	pprint(data)
if __name__ == "__main__":
	main()

#Run again? - use .lower to capture correct response
runAgain = (input('Another location? (yes or no) ')).lower()
#ok to answer "yes" or "y"
if runAgain =="yes" or runAgain=="y":
	main()	
	
else:
	print("Thank you, goodbye.")
	time.sleep(2)
	exit
#back to Main
