import pickle
import re

p_file = open('wkt_string.tsv', 'r')

p_dict = {}

for line in p_file:
	line = line.strip('\n')
	row = line.split('\t')
	id = row[0]
	polygon = row[1]
	p_dict[id] = polygon
pickle.dump(p_dict, open('polygon_dict.p', 'wb'))

w_file = open('list_results.tsv')
w_dict = {}

for line in w_file:
	line = line.strip('\n')
	row = line.split('\t')
	id = row[1]
	body = re.sub(' ', '_', row[0].lower())
	w_dict[id] = body
pickle.dump(w_dict, open('water_dict.p', 'wb'))
	
