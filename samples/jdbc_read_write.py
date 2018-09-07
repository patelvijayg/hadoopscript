#/var/lib/pgsql/9.6/data	pg_hba.conf
#local   all             all                                     trust
#psql -U postgres -h localhost -p5432
#ALTER ROLE vagrant WITH SUPERUSER
#CREATE TABLE t1 (col1 int,col2 varchar(10));
#PGPASSWORD=postgres;PGDATABASE=sparkDB; PGUSER=postgres;PGPORT=5432;PGHOST=localhost; psql -U postgres -h localhost -p5432 -d sparkDB -c "select * from t1"

#pyspark --master local[3] --conf spark.ui.port=4050 --conf spark.sql.shuffle.partitions=11 --packages org.postgresql:postgresql:9.4.1212

from pyspark.sql.types import *
from pyspark.sql.functions import *
dataschema= StructType([StructField("col1", IntegerType(), True),StructField("col2", StringType(), True)]) 
df = spark.read.format("csv").option("header","false").schema(dataschema).option("mode","DROPMALFORMED").load("file:///tmp/table1.csv")
df.write.format("jdbc").mode("overwrite").option("driver", "org.postgresql.Driver").option("url", "jdbc:postgresql://localhost:5432/sparkDB").option("dbtable", "t1").option("user", "postgres").option("password","postgres").save()
