from pyspark import SparkContext
from pyspark.sql import SparkSession
from asammdf import MDF
import io
import sys

spark = SparkSession\
        .builder\
        .appName("mdf4")\
        .getOrCreate()

sc = spark.sparkContext

def decodeBinary(val):
    file_stream = io.BytesIO(val)
    mdf = MDF(file_stream)
    location = mdf.whereis(channel_name)
    return location

if len(sys.argv) < 4 :
   print("Usage: spark-submit mdf4_spark_example.py <InputMDF4File> <ChannelName> <OutputMDF4FileNameiWithLocalOrHDFSPath>")
   print("Sample usage: spark-submit mdf4_spark_example.py hdfs://demo:8020/user/demouser/input Sample_Image_Frame hdfs://demo:8020/user/demouser/output --master yarn --deploy-mode cluster --num-executors 2 --executor-cores 2")
else:
    input_hdfs_path_to_mdf4 = sys.argv[1]
    channel_name = sys.argv[2]
    local_or_hdfs_output_path = sys.argv[3]

    raw_binary = sc.binaryFiles(input_hdfs_path_to_mdf4)

    decoded_binary = raw_binary.map(lambda r: r[1]).map(decodeBinary)
    decoded_binary.saveAsTextFile(local_or_hdfs_output_path)
    print(decoded_binary)
