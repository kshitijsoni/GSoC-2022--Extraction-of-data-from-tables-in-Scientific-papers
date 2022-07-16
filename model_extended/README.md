


To training or predict, you should first install the requirements by running the following code:

```bash
pip install -r requirements.txt
```

To train is only needed the `train.py` file which can be configured as wanted.
`marmot.py` and `extractor.py` are inheritance of Pytorch Lighting modules: `LightningDataModule` and `LightningModule`, respectively.



```bash
 python predict.py --model_weights='<weights path>' --image_path='<image path>'
```

or simply:
```bash
 python predict.py
```


