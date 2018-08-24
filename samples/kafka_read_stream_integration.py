#from __future__ import print_function

#import sys

#$KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties &
#$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties &
#$KAFKA_HOME/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test1
#$KAFKA_HOME/bin/kafka-topics.sh --list --zookeeper localhost:2181
#$KAFKA_HOME/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test1
#$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic test1 

#.cdspark ; ./bin/spark-submit --master local[4]  
#pyspark --master local[3] --conf spark.ui.port=4050 --conf spark.sql.shuffle.partitions=11 --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.1 $SCRIPT_DIR/samples/kafka_integration.py

#echo -e '{"name":"one","age":1} \n {"name":"two","age":2} \n {"name":"three","age":3} \n {"name":"four","age":4}' | $KAFKA_HOME/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test1

#from pyspark.streaming import StreamingContext
#from pyspark.streaming.kafka import KafkaUtils
#sc.setLogLevel("TRACE")
from pyspark.sql.types import *
from pyspark.sql.functions import *
spark.conf.set("spark.sql.shuffle.partitions", 11)
readstream  = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "test1").load()
linesvalue=readstream.selectExpr("CAST(value AS STRING)")
dataschema= StructType([StructField("name", StringType(), True),StructField("age", IntegerType(), True)]) 
datadf1=linesvalue.select(from_json("value",dataschema).alias("jsondata"))
datadf1.groupBy("jsondata.name").count().writeStream.outputMode('complete').format('console').start()
datadf2=datadf1
datadf2.writeStream.format("parquet").option("path","/tmp/d1/").option("checkpointLocation","/cp2/").start()


datadf3.writeStream.format("text").option("path","/tmp/txt/").option("checkpointLocation","/cp3/").start()

datadf1.selectExpr("CAST(jsondata AS STRING) as value").writeStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("topic","output1").outputMode("update").option("checkpointLocation","/cp4/").start()

datadf5=linesvalue.select(from_json("value",dataschema).alias("jsondata")).selectExpr("jsondata.name || '---'|| jsondata.age").where("jsondata.name!='one'")

datadf5.writeStream.format("text").option("path","/tmp/txt1/").option("checkpointLocation","/cp3/").start()


orddtlschema=StructType([StructField("order_item_id",IntegerType(),True),\
						StructField("order_item_order_id",IntegerType(),True),\
						StructField("order_item_product_id",IntegerType(),True),\
						StructField("order_item_quantity",DoubleType(),True),\
						StructField("order_item_subtotal",DoubleType(),True),\
						StructField("order_item_product_price",DoubleType(),True)])
streamload  = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "test1").load()
data1=streamload.selectExpr("cast(value as string) as value").select(from_json(col("value"), orddtlschema))
data1.writeStream.format("console").start();