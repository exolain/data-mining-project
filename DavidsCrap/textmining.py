# import textminer
import pymongo

db = pymongo.MongoClient().datamining

# print dir("textmining")

# tdm = textminer.TermDocumentMatrix()

# for doc in db.tweets.find():
# 	tdm.add_doc(doc["text"])

# tdm.write_csv('matrix.csv', cutoff=1)
# for row in tdm.rows(cutoff=1)[:10]:
#         print row

f = open('workfile', 'w+')
for doc in db.tweets.find():
	try:
		f.write('%s%s' % (doc["text"].replace(" ", ","), ',\n'))
	except:
		pass

