## 软件环境
1. Windows 11 22H2
2. WSL2 Kernel version:5.15.79.1
2. MindSpore 2.0.0-rc1 
2. cuda11.6
3. python 3.8.10
## 硬件环境
1. Core i5 13500
2. 64GB
2. RTX 3060ti
## MindSpore安装
`pip install https://ms-release.obs.cn-north-4.myhuaweicloud.com/2.0.0rc1/MindSpore/unified/x86_64/mindspore-2.0.0rc1-cp38-cp38-linux_x86_64.whl --trusted-host ms-release.obs.cn-north-4.myhuaweicloud.com -i https://pypi.tuna.tsinghua.edu.cn/simple`
## 目录树
```
.
├── data
│   ├── mindrecord
│   ├── test
│   └── train
├── src
│   ├── config.py
│   ├── dataset.py
│   ├── utils.py
│   └── yolov3.py
├── 7. 前沿网络案例-YOLOV3.ipynb
├── README.md
├── predict.py
└── train.py
```