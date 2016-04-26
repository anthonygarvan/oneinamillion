import csv
from math import sqrt, ceil
import json
from statistics import median, mean, stdev

fields = ["OCCP", #job
		  "SCHL", #education
		  "RAC1P", #race
		  "SEX"] #sex
target = "WAGP"

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
			wage = row[header.index(target)]
			job = row[header.index('OCCP')]
			if wage.isnumeric() and job:
				wage = float(wage)
				key = tuple(keys)
				yield key, wage

		if i % 100000 == 0:
			print('Reading line %d' % i)

		if debug and i == 10:
			break

	f.close()

def get_counts():
	result = {}
	for key, wage in read_pums():
		for i in range(0,5):
			sub_key = key[0:i]
			if sub_key not in result:
				result[sub_key] = [wage]
			else:
				result[sub_key].append(wage)
	return result

def get_summary(wages):
	summary = {}
	summary['mean'] = mean(wages)
	if len(wages) > 1:
		summary['stdev'] = stdev(wages)
	summary['median'] = median(wages)
	summary['count'] = len(wages)
	summary['total'] = sum(wages)

	return summary

def get_stats(counts):
	stats = {}
	all_wages = []
	for key in counts:
		stats[key] = get_summary(counts[key])

	return stats

def save_stats(stats):
	reformatted = {}
	for key in stats:
		for i, field in enumerate(fields):
			file_name = key[0] if len(key) > 0 else 'Total'
			sub_key = '-'.join(key)
			if file_name not in reformatted:
				reformatted[file_name] = {sub_key: stats[key]}
			else:
				reformatted[file_name][sub_key] = stats[key]
		
	for file_name in reformatted:
		f = open('data/stats/job%s.json' % file_name, 'w')
		json.dump(reformatted[file_name], f)
		f.close()

if __name__ == '__main__':
	counts = get_counts()
	stats = get_stats(counts)
	save_stats(stats)