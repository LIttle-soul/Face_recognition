<h1>Face_recognition</h1>

* <h3>采用模块</h2>
> <p>Anaconda: 安装python3.6</p>
> <p>python3.6</p>
> <p>opencv-python,skimage: 图像处理库</p>
> <p>csv: 存入表格</p>
> <p>numpy,pandas: 数据处理库</p>
> <p>pyttsx3: 语音库</p>
* <h3>目录结构</h3>
> <p>csv: 人脸特征值存储，表格格式</p>
> <p>FaceInfomation: 人脸训练模型存放，请勿删除</p>
> <p>Image: 人脸照片数据存放，计算特征值用，请勿删除</p>
> <p>modules: 部署环境时使用，请勿删除</p>
> <p>visitor: 访客信息存放</p>
> > <p>know: 已知成员访客头像</p>
> > <p>unknow: 未知成员访客头像</p>
* <h3> 环境安装</h3>
<p style="color: chocolate">以下操作基于Anaconda3环境，并且在Windows10 X64上测试。</p>

#### 1. 克隆代码
```
$ git clone url
$ cd Face_recognition
```
#### 2. 创建Python虚拟环境
```
$ conda create -n opencv python=3.6
$ activate opencv
```
#### 3. 安装OpenCV
```
$ cd modules
$ pip install install opencv_python-3.4.1+contrib-cp36-cp36m-win_amd64.whl
```
#### 4. 安装dlib
```
$ pip install dlib-19.8.1-cp36-cp36m-win_amd64.whl
```
#### 5. 安装其他依赖包
```
$ pip install -r requirements.txt
```
* ### 接口调用
```
Face_Collect: 人脸采集
Face_Dirll: 人脸训练
Face_Recognition: 人脸识别
Word_Speech: 文字播报
```