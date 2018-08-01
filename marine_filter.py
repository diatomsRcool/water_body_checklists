#This code does the actual filter using the marine and non-marine lists
import pickle

p = '4286'

out_file = open('/Volumes/PCCOMP/waterbody_checklist_result/checklist/' + p + '_w.tsv', 'w')
out_file_ = open('2350_check.tsv', 'w')

list = open('/Volumes/PCCOMP/waterbody_checklist_result/checklist/' + p + '.tsv', 'r')
f = open('/Volumes/PCCOMP/waterbody_checklist_result/checklist/marine_taxa.p', 'rb')
worms = pickle.load(f)
f.close()
g = open('/Volumes/PCCOMP/waterbody_checklist_result/checklist/not_marine_taxa.p', 'rb')
not_marine = pickle.load(g)
g.close()

#this function normalizes the length of the pipe-delimited higher classification so the rest of the code will work.
#I noticed in some other lists, instead of having blanks, the higher classifications were different 
#lengths.
def norm_len(hi_class):
	#print(len(hi_class))
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
					out_file_.write(line)
