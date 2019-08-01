from asammdf import MDF
import sys
import time
import numpy as np
from PIL import Image
import io
 
if __name__=='__main__':
        if len(sys.argv) < 5 :
           print("Usage: python extract_image_mdf4.py <MDF4File> <GroupOfImageChannel> <IndexOfImageChannel> <OutputImageName> ")
           print("Sample usage: python extract_image_mdf4.py sampleImage.mf4 0 1 sample.jpg")
        else:  
            mdf4_file_path = sys.argv[1]
            print('mdf4 file path : ', mdf4_file_path)
            image_group = int(sys.argv[2])
            image_index = int(sys.argv[3])
            output_image_name = sys.argv[4]

            mdf4 = MDF(mdf4_file_path)
            print("MDF4 Information")
            print(mdf4.info())
            channel_name = mdf4.get_channel_name(image_group,image_index)
            print("Channel name: ")
            print(channel_name)
            whereis_tuple = mdf4.whereis(channel_name)
            print("Channel Occurrences: ")
            print(whereis_tuple)

            channel_sample_tuple = mdf4.get(name=channel_name,group=image_group,index=image_index,samples_only=True)
            channel_sample_nparray = channel_sample_tuple[0]

            print("Channel Sample NPArray Type:" )
            print(type(channel_sample_nparray))
            print("Channel NP Array Size: ")
            print(channel_sample_nparray.size)
            print("Channel array shape:")
            print(channel_sample_nparray.shape)
            print("Channel Sample NPArray Data: ")
            print(channel_sample_nparray)

            image = Image.fromarray(np.uint8(channel_sample_nparray))
            image.save(output_image_name)


