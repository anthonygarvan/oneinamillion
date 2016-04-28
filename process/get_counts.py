import csv
from math import sqrt, ceil
import json
from statistics import median, mean, stdev

fields = ['SEX',
		  'RAC1P',
		  'HISP',
		  'SCHL',
		  'ST',
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

		if debug and i == 1000000:
			break

	f.close()

def get_counts():
	result = {}
	for key in read_pums():
		for i in range(0,len(fields) + 1):
			sub_key = key[0:i]
			if sub_key not in result:
				result[sub_key] = 1
			else:
				result[sub_key] += 1
	return result

def get_rare_stats(counts):
	total = 0
	for key in counts:
		if len(key) == len(fields):
			total += counts[key]

	thresholds = (10**3, 10**4, 10**5, 10**6)
	total_rare = dict.fromkeys(thresholds, 0)
	for key in counts:
		if len(key) == len(fields):
			for threshold in thresholds:
				if (total / counts[key]) > threshold:
					total_rare[threshold] += counts[key]

	formatted = []
	for threshold in total_rare:
		formatted.append({"threshold": threshold, "count": total_rare[threshold], 
			"percentage": total_rare[threshold] / total})
	
	f = open('data/stats/totalRare.json', 'w')
	json.dump(formatted, f)
	f.close()

def save_counts(counts):
	reformatted = {}
	for key in counts:
		file_name = '-'.join(key[:(len(fields) -1)]) if len(key) > 0 else 'total'
		if file_name not in reformatted:
			if len(key) < len(fields):
				reformatted[file_name] = {"count": counts[key]}
	for key in counts:
		if(len(key) == len(fields)):
			file_name = '-'.join(key[:(len(fields) - 1)])
			reformatted[file_name][key[(len(fields)-1)]] = {"count": counts[key]}
		
	for file_name in reformatted:
		f = open('data/stats/%s.json' % file_name, 'w')
		json.dump(reformatted[file_name], f)
		f.close()

if __name__ == '__main__':
	counts = get_counts()
	save_counts(counts)
	get_rare_stats(counts)