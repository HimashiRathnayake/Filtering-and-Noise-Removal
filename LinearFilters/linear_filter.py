def linearFilter(mask_array, input_image, edgeType):

    output_image = []
    kernal_half = len(mask_array) // 2
    kernal_size = len(mask_array)
    rows_count = len(input_image)
    columns_count = len(input_image[0])
    
    if (edgeType=="O"):
        fixed_image = input_image

    elif (edgeType=="S"):
        fixed_image = input_image
        #TO DO
        

    elif (edgeType=="P"):
        fixed_image = input_image
        empty_array = []
        for i in range(0, rows_count):
            fixed_image[i].insert(0, 0)
            fixed_image[i].insert(len(fixed_image[i]), 0)
        for j in range(0, columns_count+2):
            empty_array.append(0)
        fixed_image.insert(0, empty_array)
        fixed_image.append(empty_array)

    elif (edgeType=="R"):
        fixed_image = input_image
        for i in range(0, rows_count):
            fixed_image[i].insert(0, input_image[i][0])
            fixed_image[i].append(input_image[i][columns_count])
        fixed_image.insert(0, input_image[0])
        fixed_image.append(input_image[rows_count])

    elif (edgeType=="W"):
        fixed_image = input_image
        for i in range(0, rows_count):
            fixed_image[i].insert(0, input_image[i][-1])
            fixed_image[i].append(input_image[i][1])
        fixed_image.insert(0, input_image[-1])
        fixed_image.append(input_image[1])

    # apply filtering
    new_rows_count = len(fixed_image)
    new_columns_count = len(fixed_image[0])

    for i in range(kernal_half, new_rows_count - kernal_half):
        output_row = []
        for j in range(kernal_half, new_columns_count - kernal_half):
            sum = 0
            for x in range(len(mask_array)):
                for y in range(len(mask_array)):
                    x1 = i + x - kernal_half
                    y1 = j + y - kernal_half
                    sum += fixed_image[x1][y1] * mask_array[x][y]
            output_row.append(sum)
        output_image.append(output_row)

    return output_image
