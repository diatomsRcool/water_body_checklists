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
		mpolygon = sea['geometry']['coordinates']
		y = 0
		for polygon in mpolygon:
			polygon = polygon[0]
			y = y + len(polygon)
		#print(y)
		if y > 2499:
			for n,polygon in enumerate(mpolygon):
				polygon2 = polygon[0]
				if len(polygon2) > 36:
					polygon2 = polygon2[0::9]
					polygon2.append(polygon2[0])
					polygon[0] = polygon2
					mpolygon[n] = polygon
				else:
					polygon[0] = []
					mpolygon[n] = polygon
		if y > 1999:
			for n,polygon in enumerate(mpolygon):
				polygon2 = polygon[0]
				if len(polygon2) > 25:
					polygon2 = polygon2[0::8]
					polygon2.append(polygon2[0])
					polygon[0] = polygon2
					mpolygon[n] = polygon
				else:
					polygon[0] = []
					mpolygon[n] = polygon
		if y > 1299:
			for n,polygon in enumerate(mpolygon):
				polygon2 = polygon[0]
				if len(polygon2) > 25:
					polygon2 = polygon2[0::7]
					polygon2.append(polygon2[0])
					polygon[0] = polygon2
					mpolygon[n] = polygon
				else:
					polygon[0] = []
					mpolygon[n] = polygon
		elif y > 1199:
			for n,polygon in enumerate(mpolygon):
				polygon2 = polygon[0]
				if len(polygon2) > 20:
					print('small polygon')
					polygon2 = polygon2[0::6]
					polygon2.append(polygon2[0])
					polygon[0] = polygon2
					mpolygon[n] = polygon
				else:
					polygon[0] = []
					mpolygon[n] = polygon
		elif y > 399:
			for n,polygon in enumerate(mpolygon):
				polygon2 = polygon[0]
				if len(polygon2) > 15:
					polygon2 = polygon2[0::5]
					polygon2.append(polygon2[0])
					polygon[0] = polygon2
					mpolygon[n] = polygon
				else:
					polygon[0] = []
					mpolygon[n] = polygon
		elif y > 299:
			print('bigger than 299')
			for n,polygon in enumerate(mpolygon):
				polygon2 = polygon[0]
				if len(polygon2) > 15:
					print('small polygon')
					polygon2 = polygon2[0::4]
					polygon2.append(polygon2[0])
					polygon[0] = polygon2
					mpolygon[n] = polygon
				else:
					polygon[0] = []
					mpolygon[n] = polygon
		elif y > 199:
			for n,polygon in enumerate(mpolygon):
				polygon2 = polygon[0]
				if len(polygon2) > 5:
					polygon2 = polygon2[0::3]
					polygon2.append(polygon2[0])
					polygon[0] = polygon2
					mpolygon[n] = polygon
				else:
					polygon[0] = []
					mpolygon[n] = polygon
		elif y > 34:
			for n,polygon in enumerate(mpolygon):
				polygon2 = polygon[0]
				if len(polygon2) > 5:
					polygon2 = polygon2[1::2]
					polygon2.append(polygon2[0])
					polygon[0] = polygon2
					mpolygon[n] = polygon
				else:
					polygon[0] = []
					mpolygon[n] = polygon
		else:
			print('short enough already')
		#print(mpolygon)
		#print(len(mpolygon))
		upoly = list(filter(None, mpolygon))
		#print(upoly[0][0])
		#print(len(upoly))
		for z,y in enumerate(upoly):
			for k,u in enumerate(y):
				#print(u)
				for i,coor in enumerate(u):
					#print(coor)
					for j,g in enumerate(coor):
						#print(g)
						coor[j] = round(g, 3)
						#print(coor)
					u[i] = coor
					#print(u)
				y[k] = u
			upoly[z] = y
			#print('upoly')
			#print(upoly)
			#upoly[0][0] = upoly[0]
		sea['geometry']['coordinates'] = upoly
		#print(sea['geometry']['coordinates'])
	else:
		print('error')
#	print(len(polygon))
#	u = polygon[0]
#	for i,coor in enumerate(u):
#		for j,g in enumerate(coor):
#			coor[j] = round(g, 3)
#		u[i] = coor
#	polygon[0] = u
	shapes['features'] = sea
	all_shapes.append(shapes)
	#print(len(all_shapes))
json.dump(all_shapes, out_file)