#from __future__ import print_function

#import sys

#$KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties &
#$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties &
#$KAFKA_HOME/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test1
#$KAFKA_HOME/bin/kafka-topics.sh --list --zookeeper localhost:2181
#$KAFKA_HOME/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test1
#$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic test1 

#.cdspark ; ./bin/spark-submit --master local[4]  
#pyspark --master local[2] --conf spark.ui.port=4050 --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.1.1 $SCRIPT_DIR/samples/kafka_integration.py


from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.types import *
from pyspark.sql.functions import *
topiclist=["test1"]
brokermap={"metadata.broker.list": "localhost:9092"}
collectioninteval=5
#{"order_item_id":1,"order_item_order_id":1,"order_item_product_id":957,"order_item_quantity":1,"order_item_subtotal":299.98,"order_item_product_price":299.98}

orddtlschema=StructType([StructField("order_item_id",IntegerType(),True),\
						StructField("order_item_order_id",IntegerType(),True),\
						StructField("order_item_product_id",IntegerType(),True),\
						StructField("order_item_quantity",DoubleType(),True),\
						StructField("order_item_subtotal",DoubleType(),True),\
						StructField("order_item_product_price",DoubleType(),True)])
#StringType TimestampType DoubleType IntegerType LongType

ssc = StreamingContext(sc, collectioninteval) #collect every interval-seconds
kvs = KafkaUtils.createDirectStream(ssc, topiclist, brokermap)
#kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {"test1": 1})
lines = kvs.map(lambda x: x[1])
counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
counts.pprint()
ssc.start()
ssc.awaitTermination()

#ssc.stop()