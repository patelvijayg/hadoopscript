from __future__ import print_function
from pyspark.sql import SparkSession
if __name__ == "__main__":
	spark = SparkSession.builder.appName("unittesting1").getOrCreate()
	df1=spark.read.json ("file:///tmp/data-master/retail_db_json/orders")
	df1.show (2, False)
	spark.stop()
	print("now program has been stopped")