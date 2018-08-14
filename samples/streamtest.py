#from __future__ import print_function

#import sys

#if __name__ == "__main__":
#sc = SparkContext(appName="PythonStreamingNetworkWordCount")


from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql.types import *
ssc = StreamingContext(sc, 8)
inputstream = ssc.socketTextStream("localhost",9999)
#counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
schemaString = "name month salary dept"
fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
schema = StructType(fields)
rdd0=inputstream.map(lambda i: i.split(","))
rdd1=rdd0.map(lambda i:(i[0],int(i[2])) )
#rdd2=rdd1.filter(lambda f: f[0]!='')
rddwin=rdd1.window(16,16)
rdd3=rddwin.reduceByKey(lambda c, i : c + i)
rdd3.pprint()
ssc.start()	 
ssc.awaitTermination()

ssc.stop()