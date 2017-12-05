import json
import itertools
import pickle

files = ['adriatic','aegean','alboran','andaman','arabian','arafura','arctic','azov','baffin','balearic','bali','baltic','banda','barents','bass','beaufort','bengal','bering','biscay','bismarck','black','bristol','caribbean','celebes','celtic','ceram','chukchi','coral','davis','east_siberian','eastern_china','english_channel','flores','fundy','goaden','goalaska','goaqaba','goboni','gobothnia','gocalifornia','gofinland','goguinea','gomexico','gooman','goriga','gostlawrence','gosuez','gothailand','gotomini','great_australian_bight','greenland','halmahera','hudsonbay','hudsonstrait','indianocean','inlandsea','ionian','irishsea','japansea','javasea','karasea','kattegat','labrador','laccadive','laptev','ligurian','lincoln','makassar','malacca','marmara','mediterranean','molukka','mozambiquechannel','northatlantic','northpacific','northsea','norwegiansea','nwpassage','okhotsk','persiangulf','philippinesea','redsea','riodelaplata','savusea','singaporestrait','skagerrak','solomonsea','southatlantic','southchina','southernocean','southpacific','straitgibraltar','sulusea','tasmansea','timorsea','tyrrheniansea','westscotland','whitesea','yellowsea']
out_file = open('low_res_sea.json', 'w')

all_shapes = []

for file in files:
	shape_file = open(file + '.json','r')
	data = shape_file.read()
	shapes = json.loads(data)
	sea = shapes['features'][0]
	#print(sea)
	shape_type = sea['geometry']['type']
	print(sea['properties']['name'])
	if shape_type == 'Polygon':
		polygon = sea['geometry']['coordinates'][0]
		if len(polygon) > 200:
			polygon = polygon[0::2]
			polygon.append(polygon[0])
			sea['geometry']['coordinates'][0] = polygon
		if len(polygon) > 34:
			polygon = polygon[1::2]
			polygon.append(polygon[0])
			sea['geometry']['coordinates'][0] = polygon
	elif shape_type == 'MultiPolygon':
		mpolygon = sea['geometry']['coordinates'][0]
		print('number of polygons ' + str(len(mpolygon)))
		y = 0
		for polygon in mpolygon:
			y = y + len(polygon)
		print('total number of coordinates ' + str(y))
		if y > 500000:
			print(len(mpolygon))
			for n,polygon in enumerate(mpolygon):
				if len(polygon) > 100000:
					polygon = polygon[0::50000]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				elif len(polygon) > 10000:
					polygon = polygon[0::1000]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				elif len(polygon) > 1000:
					polygon = polygon[0::100]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				elif len(polygon) > 100:
					polygon = polygon[0::10]
					polygon.append(polygon[0])	
					mpolygon[n] = polygon
				elif len(polygon) > 50:
					polygon = polygon[0::9]
					polygon.append(polygon[0])	
					mpolygon[n] = polygon
				elif len(polygon) < 10:
					polygon = []
					mpolygon[n] = polygon					
				else:
					mpolygon[n] = polygon
		elif y > 100000:
			for n,polygon in enumerate(mpolygon):
				if len(polygon) > 10000:
					polygon = polygon[0::1000]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				elif len(polygon) > 1000:
					polygon = polygon[0::100]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				elif len(polygon) > 100:
					polygon = polygon[0::10]
					polygon.append(polygon[0])	
					#polygon[0] = polygon2
					mpolygon[n] = polygon
				elif len(polygon) > 50:
					polygon = polygon[0::9]
					polygon.append(polygon[0])	
					mpolygon[n] = polygon
				elif len(polygon) < 10:
					polygon = []
					mpolygon[n] = polygon
				else:
					mpolygon[n] = polygon
		elif y > 50000:
			for n,polygon in enumerate(mpolygon):
				#print('number of coordinates ' + str(len(polygon)))
				if len(polygon) > 5000:
					polygon = polygon[0::500]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				elif len(polygon) > 1000:
					polygon = polygon[0::500]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				elif len(polygon) > 100:
					polygon = polygon[0::50]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				elif len(polygon) < 100:
					polygon = []
					mpolygon[n] = polygon
				else:
					mpolygon[n] = polygon
				#print('number of coordinates ' + str(len(polygon)))
				#print('\n')
		elif y > 10000:
			for n,polygon in enumerate(mpolygon):
				#print('number of coordinates ' + str(len(polygon)))
				if len(polygon) > 5000:
					polygon = polygon[0::500]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				elif len(polygon) > 1000:
					polygon = polygon[0::100]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				elif len(polygon) > 100:
					polygon = polygon[0::10]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				elif len(polygon) < 10:
					polygon = []
					mpolygon[n] = polygon
				else:
					mpolygon[n] = polygon
				#print('number of coordinates ' + str(len(polygon)))
				#print('\n')
		elif y > 2499:
			for n,polygon in enumerate(mpolygon):
				if len(polygon) > 36:
					polygon = polygon[0::9]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				else:
					mpolygon[n] = polygon
		elif y > 1999:
			for n,polygon in enumerate(mpolygon):
				if len(polygon) > 25:
					polygon = polygon[0::8]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				else:
					mpolygon[n] = polygon
		elif y > 1299:
			for n,polygon in enumerate(mpolygon):
				if len(polygon) > 25:
					polygon = polygon[0::7]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				else:
					mpolygon[n] = polygon
		elif y > 1199:
			for n,polygon in enumerate(mpolygon):
				if len(polygon) > 20:
					print('small polygon')
					polygon = polygon[0::6]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				else:
					mpolygon[n] = polygon
		elif y > 399:
			for n,polygon in enumerate(mpolygon):
				if len(polygon) > 15:
					polygon = polygon[0::5]
					polygon.append(polygon[0])
					mpolygon[n] = polygon
				else:
					mpolygon[n] = polygon
		else:
			print('short enough already')
		y = 0
		for polygon in mpolygon:
			y = y + len(polygon)
		print('total number of coordinates ' + str(y))
		#print('number of polygons ' + str(len(mpolygon)))
		upoly = list(filter(None, mpolygon))
		for z,y in enumerate(upoly):
			for k,u in enumerate(y):
				for j,g in enumerate(u):
					u[j] = round(g, 3)
				y[k] = u
			upoly[z] = y
		sea['geometry']['coordinates'] = upoly
	else:
		print('error')
	shapes['features'] = sea
	all_shapes.append(shapes)
json.dump(all_shapes, out_file)