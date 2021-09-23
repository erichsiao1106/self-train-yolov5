# 一.安裝配置

## 1.安裝torch
https://pytorch.org/get-started/locally/

## 2.下載labelmg

[https://github.com/tzutalin/labelImg](https://github.com/tzutalin/labelImg)

```bash
git clone https://github.com/tzutalin/labelImg
```

## 3.下載yolo5
```bash
git clone https://github.com/ultralytics/yolov5
```

## 4.安裝requirement.txt (在yolov5下面的目錄)

```bash
pip install -r requirements.txt
```

# 二.訓練

## 1.使用takepic.py製作自己的影像資料集

## 2.pip install

```bash
pip install pyQt5
```

```bash
pip install lxml
```

## 3.移動到 labelimg 資料夾

```bash
pyrcc5 -o libs/resources.py resources.qrc
```

## 4.使用labelimg
找到labelimg/data 內的檔案predefines_classes.txt
修改成你自訂的類別
再執行
```bash
python labelImg.py
```
## 5.dataset.yaml(在yolov5自己內建)

```bash
# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: ../data
train: images
val: images 

# Classes
nc: 4  # number of classes
names: ['glass','phone','mask','clean_face']  # class names
```

## 6.開始訓練
```bash
python train.py --img 320 --batch 16 --epochs 5 --data dataset2.yaml --weights yolov5s.pt
```
