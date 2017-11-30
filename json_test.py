import pickle
import json

in_file = open('low_res_sea.json', 'rb')

m = json.load(in_file)
print(m)

