# python script to fetch data from the remote DB (MongoDB hosted on MongoDb Atlas) with query

import pymongo

client = pymongo.MongoClient("mongodb+srv://gatij:9nncz40BasoM5mmu@democluster.3tqjv.azure.mongodb.net/<BookstoreDb>?retryWrites=true&w=majority")
mydb = client["BookstoreDb"]
mycol = mydb["Books"]
myquery = {"Category" : "Computers"}
mydoc = mycol.find(myquery)
for x in mydoc:
	print(x)