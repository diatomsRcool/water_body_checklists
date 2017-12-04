
# coding: utf-8

# In[214]:

import json

shape_file = open('shapes_simplified_low.json','r')
out_file = open('low_res_countries.json', 'w')
data = shape_file.read()

shapes = json.loads(data)


# In[215]:

countries = shapes['features']
for country in countries:
    shape_type = country['geometry']['type']
    geonamesid = country['properties']['geoNameId']
    print geonamesid
    if shape_type == 'Polygon':
        polygon = country['geometry']['coordinates'][0]
        if len(polygon) > 200:
            polygon = polygon[0::2]
            polygon.append(polygon[0])
            country['geometry']['coordinates'][0] = polygon
        if len(polygon) > 34:
            polygon = polygon[1::2]
            polygon.append(polygon[0])
            country['geometry']['coordinates'][0] = polygon
    elif shape_type == 'MultiPolygon':
        mpolygon = country['geometry']['coordinates']
        y = 0
        for polygon in mpolygon:
            polygon = polygon[0]
            y = y + len(polygon)
        print y
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
                    print 'small polygon'
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
            print 'bigger than 299'
            for n,polygon in enumerate(mpolygon):
                polygon2 = polygon[0]
                if len(polygon2) > 15:
                    print 'small polygon'
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
            print 'short enough already'
        print mpolygon
        print len(mpolygon)
        upoly = filter(None, mpolygon)
        print upoly
        print len(upoly)
        country['geometry']['coordinates'] = upoly
        print country['geometry']['coordinates']
    else:
        print 'error'
shapes['features'] = countries
json.dump(shapes, out_file)

