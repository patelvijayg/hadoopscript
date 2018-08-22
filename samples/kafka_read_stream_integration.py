#from __future__ import print_function

#import sys

#$KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties &
#$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties &
#$KAFKA_HOME/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test1
#$KAFKA_HOME/bin/kafka-topics.sh --list --zookeeper localhost:2181
#$KAFKA_HOME/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test1
#$KAFKA_HOME/bin/kafka-console-consumer.sh --broker-list localhost:9092 --from-beginning --topic test1 

#.cdspark ; ./bin/spark-submit --master local[4]  
#pyspark --master local[2] --conf spark.ui.port=4050 --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.2.0 $SCRIPT_DIR/samples/kafka_integration.py


#from pyspark.streaming import StreamingContext
#from pyspark.streaming.kafka import KafkaUtils
#from pyspark.sql.types import *
from pyspark.sql.functions import *
sc.setLogLevel("TRACE")
lines  = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "test1").load().selectExpr("CAST(value AS STRING)")
words = lines.select(explode(split(lines.value, ' ')).alias('word'))
wordCounts = words.groupBy('word').count()
query = wordCounts.writeStream.outputMode('complete').format('console').start()
query.awaitTermination()