# MDF4Wrapper
Parallel processing and images extraction from MDF4 files.

************************************************************************************************
This repository code is broadly divided into two parts.

1. Create an MDF4 file and embed an image in it using ASAM MDf4 library. Decode the image embedded in the MDF4 file and save it to local disk.
2. Sample code that proves multiple MDF4 files can be processed using Spark and ASAM MDF4 library.

********mdf_Image_Frame_Generator.py************
This Python code embeds a given image into a new MDF4 file.

*******extract_image_mdf4.py********************
This Python code extracts the image present in the previously generated MDF4 file.

*******mdf4_spark_example.py********************
This PySpark code processes multiple MDF4 files present in HDFS(Hadoop Distributed File System) and stores the result either on local disk or HDFS based on the user preference.

References:
https://www.asam.net/standards/detail/mdf/

https://github.com/danielhrisca/asammdf

https://asammdf.readthedocs.io/en/latest/api.html

Disclaimer:
This is not an official HCL ERS project.
This is only a proof of concept.
