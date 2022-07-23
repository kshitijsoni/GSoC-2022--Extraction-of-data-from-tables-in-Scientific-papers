# Table Structure Recognition

### Code for Bordered and Borderless tables is released. I will update the readme soon for Borderless tables.


## Bordered Pipeline
For bordered table images, the most important feature is that it contains lines to segregate rows and columns due to which a human can easily understand the structure and its information. So, I took advantage of this feature and used line detection methods to detect the lines in an image by which it was easy to separate the rows and columns of the table. For this I divided the Bordered Pipeline into 3 Steps: 
            
            1. Line Detection
                i.  Horizontal lines
                ii. Vertical lines
            2. Cell Formation
                i.  Find Intersection points in lines
                ii. Identify cells from points
            3. Text Detection in cells 


### 1. Line Detection
** In order to get better line detection results it is required to keep a gap of 15 pixels from the border of the table. If the table is located to close to the border of the page this will result in negative values of the table. It is favourable to pad the whole image with 10 pixels before passing it through the pipeline.**

Refer this Documentation for Line Detection : https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html

#### Preprocessing  
```
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 1)
bw = cv2.bitwise_not(bw)
```


#### Horizontal Lines
Before moving towards line detection, it is nercessary to highlight horizontal lines in the image to make horizontal line detection easier. In order to do that, some morphological operation are applied to the image.

```
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 1))

horizontal = cv2.erode(bw, horizontalStructure)
horizontal = cv2.dilate(horizontal, horizontalStructure)

horizontal = cv2.dilate(horizontal, (1,1), iterations=5)
horizontal = cv2.erode(horizontal, (1,1), iterations=5)
```

#### Vertical Lines
Similar morphological operations need to be performed on the image for Vertical lines.

```
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 1))

horizontal = cv2.erode(bw, horizontalStructure)
horizontal = cv2.dilate(horizontal, horizontalStructure)

horizontal = cv2.dilate(horizontal, (1,1), iterations=5)
horizontal = cv2.erode(horizontal, (1,1), iterations=5)
```


#### Lines Detected 


As we can observe the lines are very well detected but multiples lines are detected at the same location.So, further postprocessing is applied to remove the detection of multiple lines.

### 3. Text Detection
Will update soon 
