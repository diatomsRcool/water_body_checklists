import json

shape_file = open('low_res_sea_4.json','r')
shapes = json.load(shape_file)
out_file = open('wkt_string_4.tsv', 'w')

#print(shapes[0])

for sea in shapes:
	#print(sea)
	polygons = sea['features']
	geoid = polygons['properties']['mrgid']
	print(geoid)
	shape_type = polygons['geometry']['type']
	print(shape_type)
	if shape_type == 'Polygon': #some water body polygons are multiple polygons. Need a different procedure
		p = []
		wkt = polygons['geometry']['coordinates']
		for i in wkt:
			z = []
			lat = i[1]
			lon = i[0]
			z.append(str(lon))
			z.append(str(lat))
			m = '%20'.join(z)
			p.append(str(m))
		q = '%2C%20'.join(p)
		#url = 'http://api.effechecka.org/checklist.tsv?traitSelector=&wktString=POLYGON((' + str(q) + '))'
		z = 'POLYGON((' + str(q) + '))'
	elif shape_type == 'MultiPolygon':
		q = ''
		#url = 'http://api.effechecka.org/checklist.tsv?traitSelector=&wktString=GEOMETRYCOLLECTION%28POLYGON%20%28%28'
		wkt = polygons['geometry']['coordinates']
		print(len(wkt))
		#print(wkt)
		for k in wkt:
			#k = k[0]
			#print(k)
			if len(k) == 0: #the process of shortening the polygons left a lot of blank coordinates. They get removed here.
				continue
			p = []
			for i in k:
				z = []
				lat = i[0]
				lon = i[1]
				z.append(str(lon))
				z.append(str(lat))
				m = '%20'.join(z)
				p.append(str(m))
			q = q + '%2C%20'.join(p) + '%29%29%2CPOLYGON%20%28%28'
		#url = url + q
		#url = url.strip('%2CPOLYGON%20%28%28')
		#url = url + '%29'
		z = 'GEOMETRYCOLLECTION%28POLYGON%20%28%28' + q.strip('%2CPOLYGON%20%28%28')
		z = z + '%29'
	out_file.write(str(geoid) + '\t' + z + '\n')
print('complete') #make sure the code gets to the end