import cv2 as cv
import sys
import glob
import numpy as np

def apply_filter(filter_type, input_image, kernal_size=3):

    # Create a kernal with the given kernal size.
    mask_array = []
    for a in range(kernal_size):
        mask_array_row = []
        for b in range(kernal_size):
            mask_array_row.append(1)
        mask_array.append(mask_array_row)

    output_image = []
    kernal_half = len(mask_array) // 2
    kernal_size = len(mask_array)
    rows_count = len(input_image)
    columns_count = len(input_image[0])

    # Wrap the image for the edge pixels.
    image_copy = input_image.copy().copy()
    for i in range(rows_count):
      for j in range(kernal_half): 
        image_copy[i].insert(0, input_image[i][-1-(2*j)])
        image_copy[i].append(input_image[i][1+(2*j)])
    for i in range(kernal_half):
        image_copy.append(input_image[i].copy())
        image_copy.insert(0, input_image[-1-i].copy())

    # Apply filtering
    new_rows_count = len(image_copy)
    new_columns_count = len(image_copy[0])

    for i in range(kernal_half, new_rows_count - kernal_half):
        output_row = []
        for j in range(kernal_half, new_columns_count - kernal_half):

            # Implementation of Mean filter
            if (filter_type=="Mean"):
                sum = [0, 0, 0]
                for x in range(len(mask_array)):
                    for y in range(len(mask_array)):
                        x1 = i + x - kernal_half
                        y1 = j + y - kernal_half
                        value = [element * mask_array[x][y] for element in image_copy[x1][y1]]
                        sum_list = []
                        for (item1, item2) in zip(sum, value):
                            sum_list.append(item1 + item2)
                        sum = sum_list
                sum = [round(element * (1/(kernal_size * kernal_size))) for element in sum]        
                output_row.append(sum)

            # Implementation of Median filter
            elif (filter_type=="Median"):
                r_channel = []
                g_channel = []
                b_channel = []
                for x in range(len(mask_array)):
                    for y in range(len(mask_array)):
                        x1 = i + x - kernal_half
                        y1 = j + y - kernal_half
                        value = image_copy[x1][y1]
                        r_channel.append(value[0])
                        g_channel.append(value[1])
                        b_channel.append(value[2])
                r_channel.sort()
                g_channel.sort()
                b_channel.sort()    
                mid = len(r_channel) // 2
                output_row.append([r_channel[mid], g_channel[mid], b_channel[mid]])

            # Implementation of Midpoint filter
            elif (filter_type=="MidPoint"):
                r_channel = []
                g_channel = []
                b_channel = []
                for x in range(len(mask_array)):
                    for y in range(len(mask_array)):
                        x1 = i + x - kernal_half
                        y1 = j + y - kernal_half
                        value = image_copy[x1][y1]
                        r_channel.append(value[0])
                        g_channel.append(value[1])
                        b_channel.append(value[2])
                r_channel.sort()
                g_channel.sort()
                b_channel.sort()    
                output_row.append([round((r_channel[0]+r_channel[-1])/2), round((g_channel[0]+g_channel[-1])/2), round((b_channel[0]+b_channel[-1])/2)])

            # Handle Invalid Filter Types
            else:
                sys.exit("Invalid Filter Name")  

        output_image.append(output_row)

    return output_image

# Get Filtered Images
def get_filtered_images(kernal_size=3):
    filter_type_array = ["Mean", "Median", "MidPoint"]
    image_files = glob.glob("*.jpg")
    image_files += glob.glob("*.jpeg")
    for image_name in image_files:
        print(image_name)
        image = cv.imread(cv.samples.findFile(image_name))
        image_name_arr = image_name.split(".")
        if image is None:
            sys.exit("Could not read the image.")
        for filter_type in filter_type_array:
            output_image = apply_filter(filter_type, image.tolist())
            cv.imwrite(image_name_arr[0] + "_" + filter_type + "." + image_name_arr[-1], np.array(output_image))


get_filtered_images() # Give a kernal_size as an argument. Otherwise default kernal_size is 3.