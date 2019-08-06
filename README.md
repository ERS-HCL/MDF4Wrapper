# MDF4Wrapper
Parallel processing and images extraction from MDF4 files.

Setup:
No particular setup is required. Clone or download the repository and you can run with Python installed on any Linux System.

Prerequisites:

To run the Python files mdf_Image_Frame_Generator.py and extract_image_mdf4.py:

Python with version 3.6

Required Python packages:

asammdf
PIL
numpy

To run mdf4_spark_example.py:

Apache Spark 2.0
Python with version 3.6

Required Python packages:

asammdf
pyspark 

How to run? :

1) To embed a given image into a new MDF4 file:

   python mdf_Image_Frame_Generator.py ImagePath NoOfCyclesInImage OutputMDF4FileName
   
   where ImagePath refers to any vald JPEG image 
         NoOfCyclesInImage refers to Number of pixels for the input image
         OutputMDF4FileName refers to a new MDF4 file with mf4 as extension.
         
   Example usage: python mdf_Image_Frame_Generator.py sample.jpg 347 output.mf4
  
2) To extract the image saved in the MDF4 file generated in previous step:

   python extract_image_mdf4.py MDF4File GroupOfImageChannel IndexOfImageChannel OutputImageName
   
   where MDF4File refers to the MDF4 file generated in the previous step i.e, output.mf4
         GroupOfImageChannel refers to the channel group number of the embedded image. In this case it is 0.
         IndexOfImageChannel refers to the channel index of the embedded image. In this case it is 1.
         OutputImageName refers to a new JPEG image name with jpg extension. For e.g: aaa.jpg
         
   Example usage: python extract_image_mdf4.py output.mf4 0 1 sample.jpg
            
3) To process multiple MDF4 files using Spark:

   spark-submit mdf4_spark_example.py InputMDF4File ChannelName OutputMDF4FileNameWithLocalOrHDFSPath
   
   where InputMDF4File refers to HDFS path with valid MDF4 file based on the ASAM MDF standards.
         ChannelName refers to a valid channel name present in the input MDF4 file.
         OutputMDF4FileNameWithLocalOrHDFSPath Either Local path or HDFS path to store the output.
         
   Example usage: spark-submit mdf4_spark_example.py hdfs://demo:8020/user/demouser/input Sample_Image_Frame hdfs://demo:8020/user/demouser/output --master yarn --deploy-mode cluster --num-executors 2 --executor-cores 2
   Note: Two ASAM valid MDF4 files are placed in the folder: MDF4Wrapper/sample_mdf4_files/
   
    


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
