# Databricks notebook source
listoffiles={
"categories":"FileStore/tables/categories.csv",
"customers":"FileStore/tables/customers.csv",
"employees":"FileStore/tables/employees.csv",
"employee_territories":"FileStore/tables/employee_territories.csv",
"orders":"FileStore/tables/orders.csv",
"order_details":"FileStore/tables/order_details.csv",
"products":"FileStore/tables/products.csv",
"regions":"FileStore/tables/regions.csv",
"shippers":"FileStore/tables/shippers.csv",
"suppliers":"FileStore/tables/suppliers.csv",
"territories":"FileStore/tables/territories.csv"}
categories=spark.read.format("csv").option("header","true").option("inferSchema","true").option("path",listoffiles["categories"]).load()
customers=spark.read.format("csv").option("header","true").option("inferSchema","true").option("path",listoffiles["customers"]).load()
employees=spark.read.format("csv").option("header","true").option("inferSchema","true").option("path",listoffiles["employees"]).load()
employee_territories=spark.read.format("csv").option("header","true").option("inferSchema","true").option("path",listoffiles["employee_territories"]).load()
orders=spark.read.format("csv").option("header","true").option("inferSchema","true").option("timestampFormat","yyyy-MM-dd'T'HH:mm?:ss").option("path",listoffiles["orders"]).load()
order_details=spark.read.format("csv").option("header","true").option("inferSchema","true").option("timestampFormat","yyyy-MM-dd'T'HH:mm?:ss").option("path",listoffiles["order_details"]).load()
products=spark.read.format("csv").option("header","true").option("inferSchema","true").option("path",listoffiles["products"]).load()
regions=spark.read.format("csv").option("header","true").option("inferSchema","true").option("path",listoffiles["regions"]).load()
shippers=spark.read.format("csv").option("header","true").option("inferSchema","true").option("path",listoffiles["shippers"]).load()
suppliers=spark.read.format("csv").option("header","true").option("inferSchema","true").option("path",listoffiles["suppliers"]).load()
territories=spark.read.format("csv").option("header","true").option("inferSchema","true").option("path",listoffiles["territories"]).load()
orders.cache()
order_details.cache()
orders.printSchema()
order_details.printSchema()

# COMMAND ----------

orddtl=orders.join(order_details,orders["orderID"]==order_details["orderID"])
orddtlselect=orddtl.select(orders["orderID"],orders["shipCity"],orders["customerID"],orders["shippedDate"],order_details["productID"],order_details["unitPrice"],order_details["quantity"],order_details["discount"],(order_details["unitPrice"]*order_details["quantity"]-order_details["discount"]).alias("amount"))
#orddtlselect.where("shipCity like 'S%'")
#orddtlselect.show()
orddtlselect.cache()

# COMMAND ----------

import pyspark.sql.functions as func
orddatechnaged = orddtlselect.selectExpr("orderID","shipCity","customerID","cast(shippedDate as timestamp) dt","productID","unitPrice","quantity","discount","round(amount,2) as amount")
#orddatechnaged.groupBy("shipCity").agg({ "shipCity": "count","amount":"max"}).show()
#orddatechnaged.groupBy("shipCity").agg(func.count("shipCity").alias("orders"),func.sum("amount").alias("totalamt")).where("orders>50").show()
orddatechnaged.groupBy("shipCity").agg( func.sum("amount").alias("totalamt") ).where("totalamt>50").show()
#orddatechnaged.show()


# COMMAND ----------

import pyspark.sql.functions as func
windf=orddatechnaged.select("orderID","shipCity","customerID","dt","amount")
#windf.groupBy(func.window("dt","1 week").alias("week")).agg(func.count("shipCity")).orderBy("week",ascending=False).show()
windf.where("shipcity=='London' and dt>'1998-03-01'").groupBy("shipCity",func.window("dt","1 week","1 week", "2 days").alias("week")).agg(func.count("orderID").alias("orders")).show()

# COMMAND ----------

import pyspark.sql.functions as func
from pyspark.sql import Row
from datetime import datetime
import time

row =Row("id", "date_field", "value")
df = sc.parallelize([
row(1, "2017-05-23", 5.0),
row(1, "2017-05-26", 10.0),
row(1, "2017-05-29", 4.0),
row(1, "2017-06-10", 3.0),]).toDF()

start_date = datetime(2017, 5, 21, 19, 0, 0)
days_since_1970_to_start_date =int(time.mktime(start_date.timetuple())/86400)
offset_days = days_since_1970_to_start_date % 7

w = func.window("date_field", "4 days", startTime='{} days'.format(offset_days))

df.groupby("id", w).agg(func.sum("value")).orderBy("window.start").show(10, False)
