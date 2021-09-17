# Filtering & Noise Removal
> Implementation of Linear Filtering &amp; Noise Filtering.

### Linear Filtering
Contains a function that implements a 3x3 linear filter on a grey-scale image of NxM pixels. The function takes the following as inputs.
* The filter 3x3 filter mask as a 3x3 integer array
* Input image
* A parameter specifying how the edge pixels should be treated
  * O- omit edge pixels
  * S- shrink filter at edges
  * P-pad the image with black white coloured pixels
  * R-replicate edge rows
  * W-wrap the image

### Noise Filtering
Contains following noise filters. Used image wrapping for the edge pixels. Programme automatically read all JPG/JPEG files in the directory and produce filtered image.
* Mean filter
* Median filter
* Mid-point filter
 
### Implementation Details
* Open CV library only for read/write the image file.
* Python as the programming language.
