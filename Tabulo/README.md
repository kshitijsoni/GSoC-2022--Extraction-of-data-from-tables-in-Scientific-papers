

### Table of Contents
1. **[Installation Instructions](#1-installation-instructions)**<br>
2. **[Avaiable API's](#2-avaiable-apis)**<br>
3. **[Working with pretrained Models](#3-working-with-pretrained-models)**<br>
4. **[Runnning Tabulo](#4-runnning-tabulo)**<br>
5. **[Runnning Tabulo As Service](#5-runnning-tabulo-as-service)**<br>
6. **[Supported models ](#6-supported-models)**<br>
7. **[Usage](#7-usage)**<br>
8. **[Working with datasets](#8-working-with-datasets)**<br>
9. **[Training](#9-training)**<br>
10. **[LICENSE](#10-license)**<br>
## 1. Installation Instructions
Tabulo currently supports Python 2.7 and 3.4–3.6. 

### 1.1 Pre-requisites

To use Tabulo, [TensorFlow](https://www.tensorflow.org/install/) must be installed beforehand. If you want **GPU support**, you should install the GPU version of TensorFlow with `pip install tensorflow-gpu`, or else you can use the CPU version using `pip install tensorflow`.

We are using tesseract to extract data from table so you have to install tesseract also. [Follow this link to install tessersact](https://interviewbubble.com/install-tesseract-on-mac-linux-windows-centos/)

### 1.2 Installing Tabulo

First, clone the repo on your machine and then install with `pip`:

```bash
git clone https://github.com/interviewBubble/Tabulo.git
cd tabulo
pip install -e .
```


### 1.3 Check that the installation worked

Simply run `tabulo --help`.

## 2. Avaiable API's
* `localhost:5000/api/fasterrcnn/predict/`   - To detect table in the image
* `localhost:5000/api/fasterrcnn/extract/`   - Extract table content from detected tables

## 3. Working with pretrained Models:
* DOWNLOAD pretrained model from [Google drive](https://drive.google.com/drive/folders/1aUh9RfGn2XGgG2EtpKFh7P6PmcC3Q48z?usp=sharing)
* Unzip and Copy downloaded luminoth folder inside ```luminoth/utils/pretrained_models``` folder
* Hit this command to list all check points: ```tabulo checkpoint list```
* You will get output like this:
![Checkpoints](https://github.com/interviewBubble/Tabulo/raw/master/docs/images/Checkpoints.png)
* Now run server using this command: ```tabulo server web --checkpoint 6aac7a1e8a8e```

## 4. Runnning Tabulo

### 4.1 Running Tabulo as Web Server:
![Running Tabulo](https://github.com/interviewBubble/Tabulo/blob/master/docs/images/tabulo_server.png)

### 4.2 Example of Table Detection with Faster R-CNN By Tabulo:
![Example of Table Detection with Faster R-CNN By Tabulo](https://github.com/interviewBubble/Tabulo/blob/master/docs/images/table_detect.png)

### 4.3 Example of Table Data Extraction with tesseract By Tabulo:
![Example of Table Data Extraction with tesseract By Tabulo](https://github.com/interviewBubble/Tabulo/blob/master/docs/images/table_data_extract.png)

## 5. Runnning Tabulo As Service:

### 5.1 Using Curl command
```Curl command to detect tabel
curl -X POST \
  http://localhost:5000/api/fasterrcnn/predict/ \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: 70478bd2-e1e8-442f-b0bf-ea5ecf7bf4d8' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F image=@/path/to/image/page_8-min.jpg
``` 
### 5.2 With PostMan
#### Header Section:
![Table Detection using Postman](https://github.com/interviewBubble/Tabulo/blob/master/docs/images/tabulo_resquest_header.png)

#### Data Section:
![Table Detection using Postman](https://github.com/interviewBubble/Tabulo/raw/master/docs/images/table_detect_API.png)

## 6. Supported models

Currently, we support the following models:

* **Object Detection**
  * [Faster R-CNN](https://arxiv.org/abs/1506.01497)
  * [SSD](https://arxiv.org/abs/1512.02325)

We also provide **pre-trained checkpoints** for the above models trained on popular datasets such as [COCO](http://cocodataset.org/) and [Pascal](http://host.robots.ox.ac.uk/pascal/VOC/).

## 7. Usage

There is one main command line interface which you can use with the `tabulo` command. Whenever you are confused on how you are supposed to do something just type:

`tabulo --help` or `tabulo <subcommand> --help`

and a list of available options with descriptions will show up.

