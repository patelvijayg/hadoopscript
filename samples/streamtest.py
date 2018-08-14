#from __future__ import print_function

#import sys

#for i in $(cat ~/empstreamdata.txt); do echo $i; sleep 2; done | nc -lk 9999
#.cdspark ; ./bin/spark-submit --master local[4]  $SCRIPT_DIR/samples/streamtest.py

if __name__ == "__main__":
	from pyspark import SparkContext
	from pyspark.streaming import StreamingContext
	from pyspark.sql.types import *
	sc = SparkContext(appName="PythonStreamingNetworkWordCount")
	ssc = StreamingContext(sc, 4)
	inputstream = ssc.socketTextStream("localhost",9999)
	schemaString = "name month salary dept"
	fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
	schema = StructType(fields)
	rdd0=inputstream.map(lambda i: i.split(","))
	rdd1=rdd0.map(lambda i:(i[0],int(i[2])))
	rddwin=rdd1.window(60,12)
	rdd3=rddwin.reduceByKey(lambda c, i : c + i)
	rdd3.pprint(100)
	ssc.start()
		 
	ssc.awaitTermination()

#ssc.stop()