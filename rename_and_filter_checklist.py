#this code changes the file names from mrgid to water body name
#it creates a directory for each water body and places the tsv file in that directory
#the water body name is all lower case with underscores for spaces
#be sure to change the file paths for your local machine

import os
import pickle
import re
import shutil

f = open('water_dict.p', 'rb')

water_ids = pickle.load(f)

oceans = ['1904','1906','1907','1908','1910','1912','1914']

for filename in os.listdir('/Volumes/PCCOMP/waterbody_checklist_results/checklist'): #this path needs to point to the unzipped effechecka output
	if not filename.startswith('.'): #ignores hidden files. I'm not sure why they are there
		print(filename)
		mrgid = re.sub('.tsv', '', filename)
		print(mrgid)
		water = water_ids[mrgid]
		#print('done step 1')
		if mrgid in oceans:
			if not os.path.exists('/Volumes/PCCOMP/waterbody_checklist_results/' + water + '/'):
				os.makedirs('/Volumes/PCCOMP/waterbody_checklist_results/' + water + '/')
			shutil.copy('/Volumes/PCCOMP/waterbody_checklist_results/checklist/' + filename, '/Volumes/PCCOMP/waterbody_checklist_results/' + water + '/' + water + '.tsv')
			#print('done step 2')
		else:
			if not os.path.exists('/Volumes/PCCOMP/waterbody_checklist_results/' + water + '/'):
				os.makedirs('/Volumes/PCCOMP/waterbody_checklist_results/' + water + '/')
		
			out_file = open('/Volumes/PCCOMP/waterbody_checklist_results/' + water + '/' + water + '.tsv', 'w')

			list = open('/Volumes/PCCOMP/waterbody_checklist_results/checklist/' + filename, 'r')
			f = open('marine_taxa.p', 'rb')
			worms = pickle.load(f)
			f.close()
			g = open('not_marine_taxa.p', 'rb')
			not_marine = pickle.load(g)
			g.close()

			#this function normalizes the length of the pipe-delimited higher classification so the rest of the code will work.
			#I noticed in some other lists, instead of having blanks, the higher classifications were different 
			#lengths.
			#In addition to filtering out the non-marine taxa, this code will filter out data for
			#higher level taxa - we want species only
			def norm_len(hi_class):
				skip = False
				if len(hi_class) == 1:
					skip = True
				elif len(hi_class) < 3:
					hi_class.insert(3, '')
					hi_class.insert(4, '')
					hi_class.insert(5, '')
					hi_class.insert(6, '')
					hi_class.insert(7, '')
				elif len(hi_class) < 4:
					hi_class.insert(4, '')
					hi_class.insert(5, '')
					hi_class.insert(6, '')
					hi_class.insert(7, '')
				elif len(hi_class) < 6:
					hi_class.insert(5, '')
					hi_class.insert(6, '')
					hi_class.insert(7, '')
				elif len(hi_class) < 7:
					hi_class.insert(3, '')
					name = hi_class[5].split(' ')
					if len(name) < 2:
						skip = True
					else:
						genus = name[0]
						spec = name[1]
						hi_class.insert(5, genus)
						hi_class.insert(6, spec)
				elif len(hi_class) < 8:
					name = hi_class[6].split(' ')
					if len(name) < 2:
						skip = True
					else:
						spec = name[1]
						hi_class.insert(6, spec)
				else:
					pass
				return hi_class, skip
			counter = 0
			next(list)
			for line in list:
				row = line.split('\t')
				taxon_string = row[1].split('|') #the json result includes a pipe-delimited higher classification
				taxon_string, r = norm_len(taxon_string) #using the function to normalize lengths
				if r == True:
					continue
				else:
					genus = taxon_string[5].title()
					species = taxon_string[6]
					if genus == '' or species == '':
						continue
					else:
						name = genus + ' ' + species
						if name in worms:
							out_file.write(line)
						else:
							if name in not_marine:
								continue
							else:
								print(name)
								counter = counter + 1
								out_file_ = open('/Volumes/PCCOMP/waterbody_checklist_results/' + water + '/' + water + '_check.tsv', 'a')
								out_file_.write(line)
			print(mrgid + ' has ' + str(counter) + ' unchecked names')
	else:
		os.remove('/Volumes/PCCOMP/waterbody_checklist_results/checklist/' + filename) #this removes the hidden files

