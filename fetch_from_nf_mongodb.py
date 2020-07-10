# Requires pymongo 3.6.0+

from pymongo import MongoClient
import pprint

def filter_by_widgetKeyName(widgetKeyName):

	client = MongoClient()
	database = client["floatdb"]
	collection = database["fpPaidWidgetRequestCollection"]

	# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

	pipeline = [
	    {
	        u"$project": {
	            u"_id": 0,
	            u"fpPaidWidgetRequestCollection": u"$$ROOT"
	        }
	    }, 
	    {
	        u"$lookup": {
	            u"localField": u"fpPaidWidgetRequestCollection.fpId",
	            u"from": u"floatingPointInternal",
	            u"foreignField": u"_id",
	            u"as": u"floatingPointInternal"
	        }
	    }, 
	    {
	        u"$unwind": {
	            u"path": u"$floatingPointInternal",
	            u"preserveNullAndEmptyArrays": False
	        }
	    }, 
	    {
	        u"$match": {
	            u"fpPaidWidgetRequestCollection.widgetKey": widgetKeyName
	        }
	    }, 
	    {
	        u"$project": {
	            u"fpPaidWidgetRequestCollection.widgetKey": u"$fpPaidWidgetRequestCollection.widgetKey",
	            u"fpPaidWidgetRequestCollection.discount": u"$fpPaidWidgetRequestCollection.discount",
	            u"fpPaidWidgetRequestCollection.baseAmount": u"$fpPaidWidgetRequestCollection.baseAmount",
	            u"fpPaidWidgetRequestCollection.taxAmount": u"$fpPaidWidgetRequestCollection.taxAmount",
	            u"floatingPointInternal.FloatingPointTag": u"$floatingPointInternal.FloatingPointTag",
	            u"floatingPointInternal.Email": u"$floatingPointInternal.Email",
	            u"_id": 0
	        }
	    }
	]

	cursor = collection.aggregate(
	    pipeline, 
	    allowDiskUse = True
	)
	try:
	    for doc in cursor:
	    	doc['fpPaidWidgetRequestCollection']['widget_price'] = doc['fpPaidWidgetRequestCollection']['baseAmount'] + doc['fpPaidWidgetRequestCollection']['taxAmount']
	    	doc['fpPaidWidgetRequestCollection']['final_price'] = doc['fpPaidWidgetRequestCollection']['widget_price'] - doc['fpPaidWidgetRequestCollection']['discount'] 
	    	pp = pprint.PrettyPrinter(depth=6)
	    	pp.pprint(doc)
			
	finally:
	    client.close()





