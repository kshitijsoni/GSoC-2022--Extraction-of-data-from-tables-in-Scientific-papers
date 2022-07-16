

## How to run the extractor:

This repository contains an extractor model that is made using the [Streamlit](https://streamlit.io/) library. To run the model, go to the repo directory in the terminal and run the following line of code:

    streamlit run model.py
This will start the streamlit server in your local machine and you can then use it. All you need to do is *upload the image in the .bmp format* and it will show you the images of the the table mask, the column masks and the extracted table from the image. Below that, it will also show you the text extracted from the table using OCR.<br> 

## Prerequisites for running the model:

The code was tested with `tensorflow 2.6.0, python 3.7.11 and pytesseract 0.3.8` and  using `Streamlit 0.86.0`.<br> For the pre-trained model weights, download them from [here](https://drive.google.com/file/d/1cGjpOWmNoqT94QhyA4AD9iuvw-r-JrUG/view?usp=sharing) and rename the file to **DenseNet21.h5** and keep it in the same directory as the webapp script. 

## Dataset

The dataset contains images of all the tables that are extracted from the PDFs shared by Magdalena. The dataset contains images of all the tables that are extracted from the PDFs shared by Magdalena. All the images are in “.bmp” format and we need to just upload an image to test the model. Download them from [here](https://drive.google.com/drive/folders/1VTvs9sSa9oReGLlYdgRwwZeOvQK0aMs4?usp=sharing)




