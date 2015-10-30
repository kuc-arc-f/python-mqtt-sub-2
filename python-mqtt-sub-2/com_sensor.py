# -*- coding: utf-8 -*- 
import MySQLdb
import com_appConst
#define


#com_sensor
class sensorClass:

    def __init__(self):
        print ""
        

    def saveSensor(self, topic, payload):
    	ret=False
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	cursor = connection.cursor()
    	sSql=u"INSERT INTO t_sensor ( topic, payload,created)"
    	sSql=sSql+" values ("
    	sSql=sSql+"'"+topic +"'"
    	sSql=sSql+","+ payload
    	sSql=sSql+",now() );"
    	#print sSql
    	cursor.execute(sSql)
    	connection.commit()
    	cursor.close()
    	connection.close()
    	ret=True
    	return ret
