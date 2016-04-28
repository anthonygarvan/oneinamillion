import json
from math import floor, ceil

def get_state(part):
	return part.split('/')[0].strip('.')

def get_job(part):
	if '-' in part:
		job = part.split('-', maxsplit=1)[1].strip() \
				.replace('And ', 'or ') \
				.replace ('Coaches', "Coach") \
				.replace('Waitresses', "Waitress ") \
				.rstrip('**') \
				.replace('ies', 'y') \
				.replace('ists ', 'ist ') \
				.replace('ers ', 'er ') \
				.replace('ors ', 'or ') \
				.replace('ants ', 'ant ') \
				.replace('ics ', 'ic ') \
				.replace('ents ', 'ent ') \
				.replace('s,', ',') \
				.rstrip('s') 
	else:
		job = part.strip('.') \
				.strip() \
				.rstrip('**')
	return job

def get_state(part):
	return part.split('/')[0].strip('.').strip()

def get_name_default(part):
	return part.strip('.').strip()

def get_codes_for_field(field_name, file_name, get_name=get_name_default):
	f = open('data/raw/codes.txt')
	codes = []
	block_start = False
	for lineNo, line in enumerate(f):
		if field_name in line:
			block_start = lineNo
		if block_start and lineNo >= block_start + 2:
			if line.isspace():
				break
			parts = line.split(' ', maxsplit=1)
			code = parts[0]
			name = get_name(parts[1])
			codes.append({"code": code, "name": name})
	f.close()

	f = open('data/codes/%s.json' % file_name, 'w')
	json.dump(codes, f)
	f.close()

def get_codes_for_age():
	codes = []
	for i in range(10):
		lower = 10*i
		upper = 10*(i + 1)
		codes.append({"code": upper, "name": '%d-%d' % (lower, upper)}) 

	f = open('data/codes/age.json', 'w')
	json.dump(codes, f)
	f.close()

if __name__ == '__main__':
	get_codes_for_field('RAC1P 1', 'race')
	get_codes_for_field('SEX 1', 'sex')
	get_codes_for_field('SCHL 2', 'education')
	get_codes_for_field('SOCP12 6', 'job', get_job)
	get_codes_for_field('ST 2', 'state', get_state)
	#get_codes_for_age()
	