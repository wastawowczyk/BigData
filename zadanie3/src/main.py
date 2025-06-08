from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os

def load_data(spark):
    return spark.read.option("header", True).csv("../data/dane.csv")

def transform_data(df):
    return df.withColumn("reduced_price", col("price").cast("int") - 25)

def save_data(df):
    df.write.mode("overwrite").option("header", True).csv("../output")

if __name__ == "__main__":


    spark = SparkSession.builder \
        .appName("PySpark CSV Example") \
        .master("local[*]") \
        .getOrCreate()

    df = load_data(spark)
    transformed = transform_data(df)
    save_data(transformed)

    spark.stop()