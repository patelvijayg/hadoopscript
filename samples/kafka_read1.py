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


#/home/jupyterlab/spark-2.3.1/jars; wget http://central.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.11/2.3.1/spark-sql-kafka-0-10_2.11-2.3.1.jar
#/home/jupyterlab/spark-2.3.1/jars; http://central.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10-assembly_2.11/2.3.1/spark-streaming-kafka-0-10-assembly_2.11-2.3.1.jar

To remove following
#iop-bi-master.imdemocloud.com
#iop-bi-master.imdemocloud.com:2181
echo '{"order_item_id":1,"order_item_order_id":1,"order_item_product_id":957,"order_item_quantity":1,"order_item_subtotal":299.98,"order_item_product_price":299.98}' | kafka-console-producer.sh --broker-list iiop-bi-master.imdemocloud.com:6667 --topic orderdetail
echo '{"order_item_id":1,"order_item_order_id":1,"order_item_product_id":957,"order_item_quantity":1,"order_item_subtotal":299.98,"order_item_product_price":299.98}' | kafka-console-producer.sh --broker-list localhost:6667 --topic orderdetail
listeners=PLAINTEXT://iiop-bi-master.imdemocloud.com:6667,PLAINTEXT://iop-bi-master.imdemocloud.com:6667


$KAFKA_HOME/bin/kafka-console-producer.sh --broker-list iop-bi-master.imdemocloud.com:6667 --topic mytopic2


kafka-topics.sh --describe --zookeeper localhost:2181 --topic orderdetail
kafka-console-consumer.sh --zookeeper localhost:2181 --from-beginning --topic orderdetail


echo '{"test":"test"}' | $KAFKA_HOME/bin/kafka-console-producer.sh --broker-list localhost:6667 --topic mytopic2

/kafka-console-consumer.sh --zookeeper iop-bi-master.imdemocloud.com:6667 --from-beginning --topic mytopic2


bin/kafka-topics.sh --zookeeper iop-bi-master.imdemocloud.com:2181 --delete --topic orderdetail
kafka-topics.sh --create --zookeeper iop-bi-master.imdemocloud.com:2181 --replication-factor 1 --partitions 2 --topic orderdetail
kafka-topics.sh --list --zookeeper iop-bi-master.imdemocloud.com:2181 | grep orderdetail

docker run -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=127.0.0.1 --env ADVERTISED_PORT=9092 spotify/kafka


--packages com.databricks:spark-csv_2.10:1.3.0


"--packages" "org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.1"

os.environ['PYSPARK_SUBMIT_ARGS']


PYSPARK_SUBMIT_ARGS='"--packages" "org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.1" "--name" "PySparkShell" "pyspark-shell"'



.quorum.QuorumPeerMain /usr/iop/current/zookeeper-client/conf/zoo.cfg
2.10*.jar kafka.Kafka /usr/iop/current/kafka-broker/config/server.properties
lume.conf --name agent
.only=false org.apache.zookeeper.server.quorum.QuorumPeerMain /usr/iop/current/zookeeper-client/conf/zoo.cfg
ar:/usr/iop/current/kafka-broker/bin/../core/build/libs/kafka_2.10*.jar kafka.Kafka /usr/iop/current/kafka-broker/config/server.properties
