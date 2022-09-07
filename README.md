# GSoC-2022--Extraction-of-data-from-tables-in-Scientific-papers

This project was proposed by Genome Assembly and Annotation as a part of their GSOC 2022 participation. 

# Abstract

The idea was to develop the pipeline to extract the data from the tables in the scientific papers. Wormbase database retrieves all full-text scientific papers about model organisms, and in a largely automated way extracts information from those papers, to add into the database using NER, NN classification and NLP. I contributed a few different ways to programmatically identify tables in PDFs, and correctly extract the table content as text. This is super-tedious, as a lot of the data we want to collect from tables scientific publications is located in tables which do not have visible border lines and nearly more than 90% tables have nested rows and columns, which we currently cannot extract very well. The content of the tables can be symbols or numbers, so the  goal was to propose and develop the methods that should give accurate representation even of table content that are not known words, like for example eat-4 (a gene name). 

# Background 

There are many open source libraries which can extract tabular data like camelot, tabula, pdftoexcel, pdfparser etc. Also there are many commercially available softares like nanonet, docsumo, etc. But open source libraries are highly inefficient and can generate results for specific input and cannot have broad applications. We are here looking for open source so I would not like to comment much on them, but yes they are developed by senior developers and are highly efficient. 

# Proposed Pipelines in this Project 

1. Table Detection and Structure Recognition 

My proposed pipeline is an automatic table recognition method for interpretation of tabular data in document images. It is an improved deep learning-based end to end approach for solving both problems of table detection and structure recognition using a single Convolution Neural Network (CNN) model. It is is a Cascade mask Region-based CNN High-Resolution Network (Cascade mask R-CNN HRNet) based model that detects the regions of tables and recognizes the structural body cells from the detected tables at the same time. I evaluated my results on ICDAR 2013, ICDAR 2019 and TableBank public datasets. I also attain the highest accuracy results on the ICDAR 2019 table structure recognition dataset. 

Reason for choosing other datasets because the Dataset I chose and complied consisted of only 238 images in total and it was not possible to visualize the accuracy of the model with such small amount of data. 

The primary strategies involved in developing the pipeline: 
1. Using a relatively complex but efficient CNN architecture that attains high accuracy on object detection and segmentation benchmarking datasets as the main component in the approach
2. Using an iterative transfer learning approach to train the CNN model gradually, starting from more general tasks and going towards more specific tasks. Performing
iterations of transfer learning multiple times to extract the needful knowledge effectively from a small amount of data.
3. Strengthening the learning process by applying image transformation techniques to training images for data augmentation

Model Architecture 
<img src="imgs/model arch.png" width="550"/>

Pipeline


