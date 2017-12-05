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
	mpolygon = sea['geometry']['coordinates'][0]
	print('number of polygons ' + str(len(mpolygon)))
	y = 0
	for polygon in mpolygon:
		y = y + len(polygon)
	print('total number of coordinates ' + str(y))
	if y > 300:
		h = 0
		t = 0
		for n,polygon in enumerate(mpolygon):
			#print(n)
			if len(polygon) > h:
				h = len(polygon)
				t = n
			else:
				continue
		#print(t)
		max_polygon = mpolygon[t]
		print('largest polygon before reduction ' + str(len(max_polygon)))
		if len(max_polygon) > 300000:
			max_polygon = max_polygon[0::20000]
			max_polygon.append(max_polygon[0])
		elif len(max_polygon) > 100000:
			max_polygon = max_polygon[0::2000]
			max_polygon.append(max_polygon[0])
		elif len(max_polygon) > 80000:
			max_polygon = max_polygon[0::9000]
			max_polygon.append(max_polygon[0])
		elif len(max_polygon) > 30000:
			max_polygon = max_polygon[0::1000]
			max_polygon.append(max_polygon[0])
		elif len(max_polygon) > 9000:
			max_polygon = max_polygon[0::900]
			max_polygon.append(max_polygon[0])
		elif len(max_polygon) > 1000:
			max_polygon = max_polygon[0::100]
			max_polygon.append(max_polygon[0])
		elif len(max_polygon) > 300:
			max_polygon = max_polygon[0::30]
			max_polygon.append(max_polygon[0])	
		else:
			print('polygon is small enough already')
		print('largest polygon after reduction ' + str(len(max_polygon)))
	else:
		print('polygon is small enough already')
	for z,y in enumerate(max_polygon):
		#print(y)
		for k,u in enumerate(y):
			#print(u)
			y[k] = round(u, 3)
		max_polygon[z] = y
		#print(upoly[z])
	sea['geometry']['coordinates'] = max_polygon
	sea['geometry']['type'] = 'Polygon'
	shapes['features'] = sea
	all_shapes.append(shapes)
json.dump(all_shapes, out_file)