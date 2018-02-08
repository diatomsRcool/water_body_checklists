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
	
