# GSoC-2022--Extraction-of-data-from-tables-in-Scientific-papers

This project was proposed by Genome Assembly and Annotation as a part of their GSOC 2022 participation. 

# Abstract

The idea was to develop the pipeline to extract the data from the tables in the scientific papers. Wormbase database retrieves all full-text scientific papers about model organisms, and in a largely automated way extracts information from those papers, to add into the database using NER, NN classification and NLP. I contributed a few different ways to programmatically identify tables in PDFs, and correctly extract the table content as text. This is super-tedious, as a lot of the data we want to collect from tables scientific publications is located in tables which do not have visible border lines and nearly more than 90% tables have nested rows and columns, which we currently cannot extract very well. The content of the tables can be symbols or numbers, so the  goal was to propose and develop the methods that should give accurate representation even of table content that are not known words, like for example eat-4 (a gene name). 

# Background 

There are many open source libraries which can extract tabular data like camelot, tabula, pdftoexcel, pdfparser etc. Also there are many commercially available softares like nanonet, docsumo, etc. But open source libraries are highly inefficient and can generate results for specific input and cannot have broad applications. We are here looking for open source so I would not like to comment much on them, but yes they are developed by senior developers and are highly efficient. 

# Proposed Pipelines in this Project 

## I. Table Detection and Structure Recognition 

My proposed pipeline is an automatic table recognition method for interpretation of tabular data in document images. It is an improved deep learning-based end to end approach for solving both problems of table detection and structure recognition using a single Convolution Neural Network (CNN) model. It is is a Cascade mask Region-based CNN High-Resolution Network (Cascade mask R-CNN HRNet) based model that detects the regions of tables and recognizes the structural body cells from the detected tables at the same time. I evaluated my results on ICDAR 2013, ICDAR 2019 and TableBank public datasets. I also attain the highest accuracy results on the ICDAR 2019 table structure recognition dataset. 

Reason for choosing other datasets because the Dataset I chose and complied consisted of only 238 images in total and it was not possible to visualize the accuracy of the model with such small amount of data. 

The primary strategies involved in developing the pipeline: 
1. Using a relatively complex but efficient CNN architecture that attains high accuracy on object detection and segmentation benchmarking datasets as the main component in the approach
2. Using an iterative transfer learning approach to train the CNN model gradually, starting from more general tasks and going towards more specific tasks. Performing
iterations of transfer learning multiple times to extract the needful knowledge effectively from a small amount of data.
3. Strengthening the learning process by applying image transformation techniques to training images for data augmentation

##  Image Augmentation
<img src="https://github.com/kshitijsoni/GSoC-2022--Extraction-of-data-from-tables-in-Scientific-papers/blob/main/TSR/imgs/3imgs.png" width="750"/><br>
Codes: <a href="https://github.com/kshitijsoni/GSoC-2022--Extraction-of-data-from-tables-in-Scientific-papers/blob/main/TSR/Data%20Preparation/Dilation.py">Code for dilation transform</a> <a href="https://github.com/kshitijsoni/GSoC-2022--Extraction-of-data-from-tables-in-Scientific-papers/blob/main/TSR/Data%20Preparation/Smudge.py">Code for smudge transform</a>


# Model Architecture 
<img src="https://github.com/kshitijsoni/GSoC-2022--Extraction-of-data-from-tables-in-Scientific-papers/blob/main/TSR/imgs/model%20arch.png" width="700"/>

# Pipeline
<img src="https://github.com/kshitijsoni/GSoC-2022--Extraction-of-data-from-tables-in-Scientific-papers/blob/main/TSR/Table%20Structure%20Recognition/Pipeline.PNG" width="700"/>


# Results
<img src="https://github.com/kshitijsoni/GSoC-2022--Extraction-of-data-from-tables-in-Scientific-papers/blob/main/TSR/imgs/TSR.png" width="700"/>

## Dataset Preparation
The dataset was manually prepared. The tables and figures were extracted from all the pdfs shared to me. Then it was curated manually. It contains 241 images og the tables from the pdfs in bmp format. THIS DATASET CANNOT SHARED because it has COPYRIGHTED IMAGES and also the PDFS are copyrighted. The dataset has 223 tables with no visible borderlines for rows and columns, 18 tables with visible borderlines for rows and columns and total of 24920 cells.

## II. Tabular Data Extraction
The input image for the model, is first transformed into an RGB image and then, resized to 1024 * 1024 resolution.This modified image is processed using tesseract OCR. Since a single model produces both the output masks for the table and column regions, these two independent outputs have binary target pixel values, depending on whether the pixel region belongs to the table/column region or background respectively. The problem of detecting tables in documents is similar to the problem of detecting objects in real world images. Similar to the generic object detection problem, visual features of the tables can be used to detect tables and columns. The difference is that the tolerance for noise in table/column detection is much smaller than in object detection. Therefore, instead of regressing for the boundaries of tables and columns, I employed a method to predict table and column regions pixel-wise. Recent work on semantic segmentation based on pixel wise prediction, has been very successful. FCN architecture, proposed by Long et al., has demonstrated the accuracy of encoder-decoder network architectures for semantic segmentation.

# Architecture
<img src="https://github.com/kshitijsoni/GSoC-2022--Extraction-of-data-from-tables-in-Scientific-papers/blob/main/TSR/imgs/architecture.png" width="1200"/>

After processing the documents using my model, masks for table and column regions are generated. These masks are used to filter out the table and its column regions from the image. Since, all word positions of the document are already known (using Tesseract OCR), only the word patches lying inside table and column regions are filtered out. Now, using these filtered words, a row can be defined as the collection of words from multiple columns, which are at the similar horizontal
level. However, a row is not necessarily confined to a single line, and depending upon the content of a column or line demarcations, a row can span multiple lines. Therefore, to cover the different possibilities, we formulate three rules for row segmentation:

• In tables for which line demarcations are present, the lines segment the rows in each column. To detect the possible line demarcation (for rows), every space between
two vertically placed words in a column is tested for the presence of lines via a Radon transform. The presence of horizontal line demarcation clearly segments out the row.\
• In case a row spans multiple lines, the rows of the table which have maximum non-blank entries is marked as the starting point for a new row. For example in a multicolumn table, some of the columns can have entries spanning just one line (like quantity, etc), while others can have multi-line entries (like description, etc). Thus, each new row begins when all the entities in each column are filled.\
• In tables, where all the columns are completely filled and there are no line demarcations, each line (level) can be seen as a unique row.\

The different experiments performed on the dataset. The model performance is evaluated based on the Recall, Precision & F1- score. These measures are computed for each document and their average is taken across all the documents.

## (a) Table Detection: 
Completeness and Purity are the two standard measures used in page segmentation. A region is complete if it includes all sub-objects present in the ground-truth. A region is pure if it does not include any sub-objects which are not in the ground-truth. Subobjects are created by dividing the given region into meaningful parts like heading of a table, body of a table etc. But these measures do not discriminate between minor and major errors. So, individual characters in each region are treated as sub-objects. Precision and recall measures are calculated on these sub-objects in each region and the average is taken across all the regions in a given document.

## (b) Table Data Extraction: 
Each entry inside a table is defined as a cell. For each cell, adjacency relations are generated with the nearest horizontal and vertical neighbours. Thus, adjacency relations of a given cell is a 1D-tuple containing the text information of its neighboring cells. The content in each cell was normalized; white spaces were removed, special characters were replaced with underscores and lowercase letters with uppercase. This 1D-tuple can then be compared with the ground truth by using precision and recall.

Model requires both table and structure annotated data for training. I used my data and manually annotated the structure information. There are a total of 147 documents containing tables. The proposed deep model has been implemented in Tensorflow and implemented on a system with AMD Ryzen 5 RAM 16 GB 4 GB NVIDIA 3060 Graphics. There are two computation graphs which require training. Each training sample is a tuple of a document image, table mask and column mask. With each training tuple, the two graphs are computed at-least twice. In the initial phase of training, the table branch and column branch are computed in the ratio of 2:1. With each training tuple, the table branch of the computational graph is computed twice, and then the column branch of the model is computed. It is worth noting that, although the table branch and column branch are different, the encoder is the same for both. During initial iterations of training, the learning is more focused on training the model to generate big active tabular regions which on subsequent training specializes to column regions. After around 500 iterations with a batch size of 2, when train loss of both table and column detectors are comparable, this training scheme is modified. However, it should be noted that the table classifier at this stage must exhibit a converging trend (otherwise, training is extended with the same 2:1 scheme). The model is then trained in the ratio of 1:1 for both branches until convergence. Using the same training pattern, the model is trained for 5000 iterations with a batch size of 2 and learning rate of 0.0001. The Adam optimizer is used for improving and optimizing training with parameters beta1=0.9, beta2=0.999 and epsilon=1e-08. The convergence and overfitting behavior was monitored by observing the performance over the validation set . During testing, 0.99 is taken as the threshold probability for pixel-wise prediction. 

# Results

The primary contributions made in this project are as follows:
1) Aa novel end-to-end deep multi task architecture for both table detection and structure recognition yielding state of the art performance on our datasets.

2) Demonstrated that adding additional spatial semantic features during training further boosts model performance.

3) Using a pre-trained model and fine tuning it on an another new dataset will boost thenperformance of the model on the new dataset, thereby allowing for transfer learning.

4) I have manually annotated the dataset for table data extraction and will release the model to community.

# Acknowledgements

## Mentors
Magdalena Zarowiecki\ 
Andres Becerra
