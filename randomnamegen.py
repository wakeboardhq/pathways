import names
import csv


with open('names.csv', 'a') as csvfile:
	for _ in range(0,7637):
		writer = csv.writer(csvfile)
		writer.writerow(names.get_full_name())

		

