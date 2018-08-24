#$KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties &
#$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties &
#$KAFKA_HOME/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic orderdetail
#$KAFKA_HOME/bin/kafka-topics.sh --list --zookeeper localhost:2181
#$KAFKA_HOME/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test1
#$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic orderdetail 

#pyspark --master local[3] --conf spark.ui.port=4050 --conf spark.sql.shuffle.partitions=11 --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.1 $SCRIPT_DIR/samples/kafka_integration.py

#echo '{"order_item_id":1,"order_item_order_id":1,"order_item_product_id":957,"order_item_quantity":1,"order_item_subtotal":299.98,"order_item_product_price":299.98}' | $KAFKA_HOME/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic orderdetail

#from pyspark.streaming import StreamingContext
#from pyspark.streaming.kafka import KafkaUtils
#sc.setLogLevel("TRACE")
from pyspark.sql.types import *
from pyspark.sql.functions import *
spark.conf.set("spark.sql.shuffle.partitions", 11)
orddtlschema=StructType([StructField("order_item_id",IntegerType(),True),StructField("order_item_order_id",IntegerType(),True),StructField("order_item_product_id",IntegerType(),True),StructField("order_item_quantity",DoubleType(),True),StructField("order_item_subtotal",DoubleType(),True),StructField("order_item_product_price",DoubleType(),True)])

#head -15 /tmp/data-master/retail_db/order_items/part-00000  > /tmp/csv/orddtl4.csv
csvdatareader = spark.readStream.schema(orddtlschema).csv("file:///tmp/csv")
streamingDataFrame=csvdatareader.where("order_item_quantity>3")
#streamingDataFrame.writeStream.format("console").start()
streamingDataFrame.selectExpr("CAST('aa' AS STRING) AS key", "to_json(struct(*)) AS value").writeStream.format("kafka").option("topic", "orderdetail").option("kafka.bootstrap.servers", "localhost:9092").option("checkpointLocation", "/cp5/").start()

streamload = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "orderdetail").load()
df1 = streamload.selectExpr("CAST(value AS STRING) as value", "CAST(timestamp AS TIMESTAMP) as tm").select(from_json("value", orddtlschema).alias("data"), "tm").select("data.*", "tm")
df1.writeStream.format("console").start()

