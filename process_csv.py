import pyspark
from pyspark.sql import SparkSession

from pyspark.sql.functions import spark_partition_id, asc, desc

from pyspark.sql.types import IntegerType


spark = (
    SparkSession.builder.master("spark://192.168.1.103:7077")
    .config("spark.executor.cores", "5")
    .config("spark.executor.memory", "512m")
    .appName("SparkByExamples.com")
    .getOrCreate()
)

flightData2015 = (
    spark.read.option("inferSchema", "true")
    .option("header", "true")
    .csv("2015_summary.csv")
)

numbersList = list(range(10000))

# flightData2015.repartition(5, "count", "ORIGIN_COUNTRY_NAME")

numbersDf = spark.createDataFrame(numbersList, IntegerType())


print(numbersDf)

numbersDf.repartition(5)

# print("partitions count is " + str(flightData2015.rdd.getNumPartitions()))

numbersDf.withColumn("partitionId", spark_partition_id()).groupBy(
    "partitionId"
).count().show()


# print(flightData2015.sort("count").take(2))
