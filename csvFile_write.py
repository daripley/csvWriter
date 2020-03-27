import os
import csv
import sys
def main():
	filename='Yourcsv.csv'    ##your file name
	with open(filename, 'w', newline='') as csvfile:
		entries = os.listdir('/usr/local/bin')  ##directory
		writer=csv.writer(csvfile, delimiter= ' ')
		for entry in entries:
			writer.writerow(entry)
main()
