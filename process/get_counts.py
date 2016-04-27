import csv
from math import sqrt, ceil
import json
from statistics import median, mean, stdev

fields = ['SEX',
		  'RAC1P',
		  'SCHL',
		  'SOCP12']

def read_pums(debug=False):
	f = open('data/raw/pums.csv')
	reader = csv.reader(f)

	for i, row in enumerate(reader): 
		if i == 0:
			header = row		
		else:
			keys = []
			for field in fields:
				keys.append(row[header.index(field)])
			job = row[header.index('SOCP12')]

			if job:
				key = tuple(keys)
				yield key

		if i % 100000 == 0:
			print('Reading line %d' % i)

		if debug and i == 200000:
			break

	f.close()

def get_counts():
	result = {}
	for key in read_pums():
		for i in range(0,5):
			sub_key = key[0:i]
			if sub_key not in result:
				result[sub_key] = 1
			else:
				result[sub_key] += 1
	return result

def save_counts(counts):
	reformatted = {}
	for key in counts:
		file_name = '-'.join(key[:3]) if len(key) > 0 else 'total'
		if file_name not in reformatted:
			if len(key) < 4:
				reformatted[file_name] = {"count": counts[key]}
	for key in counts:
		if(len(key) == 4):
			file_name = '-'.join(key[:3])
			reformatted[file_name][key[3]] = {"count": counts[key]}
		
	for file_name in reformatted:
		f = open('data/stats/%s.json' % file_name, 'w')
		json.dump(reformatted[file_name], f)
		f.close()

if __name__ == '__main__':
	counts = get_counts()
	save_counts(counts)