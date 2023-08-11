# 运行配置
## 1.下载anaconda,配置一个pytorch的环境
包的版本如下

```
 Name                    Version                   Build  Channel  
absl-py                   1.3.0                    pypi_0    pypi  
alembic                   1.7.7                    pypi_0    pypi  
asgiref                   3.4.1                    pypi_0    pypi  
automium                  0.2.6                    pypi_0    pypi  
automium-web              0.1.1                    pypi_0    pypi  
backcall                  0.2.0                    pypi_0    pypi  
ca-certificates           2023.01.10           haa95532_0  
cachetools                4.2.4                    pypi_0    pypi  
certifi                   2021.5.30        py36haa95532_0  
cffi                      1.15.1                   pypi_0    pypi  
charset-normalizer        2.0.12                   pypi_0    pypi  
click                     8.0.4                    pypi_0    pypi  
colorama                  0.4.5                    pypi_0    pypi  
cryptography              40.0.1                   pypi_0    pypi  
cycler                    0.11.0                   pypi_0    pypi  
dataclasses               0.8                      pypi_0    pypi  
decorator                 5.1.1                    pypi_0    pypi  
django                    3.2.17                   pypi_0    pypi  
flask                     2.0.3                    pypi_0    pypi  
flask-migrate             4.0.1                    pypi_0    pypi  
flask-sqlalchemy          2.5.1                    pypi_0    pypi  
gitdb                     4.0.9                    pypi_0    pypi  
gitpython                 3.1.18                   pypi_0    pypi  
google-auth               2.15.0                   pypi_0    pypi  
google-auth-oauthlib      0.4.6                    pypi_0    pypi  
greenlet                  2.0.1                    pypi_0    pypi  
grpcio                    1.48.2                   pypi_0    pypi  
idna                      3.4                      pypi_0    pypi  
importlib-metadata        4.8.3                    pypi_0    pypi  
importlib-resources       5.4.0                    pypi_0    pypi  
ipython                   7.16.3                   pypi_0    pypi  
ipython-genutils          0.2.0                    pypi_0    pypi  
itsdangerous              2.0.1                    pypi_0    pypi  
jedi                      0.17.2                   pypi_0    pypi  
jinja2                    3.0.3                    pypi_0    pypi  
kiwisolver                1.3.1                    pypi_0    pypi  
legacy                    0.1.6                    pypi_0    pypi  
mako                      1.1.6                    pypi_0    pypi  
markdown                  3.3.7                    pypi_0    pypi  
markupsafe                2.0.1                    pypi_0    pypi  
matplotlib                3.3.4                    pypi_0    pypi  
mss                       7.0.1                    pypi_0    pypi  
numpy                     1.19.5                   pypi_0    pypi  
oauthlib                  3.2.2                    pypi_0    pypi  
opencv-python             4.1.2.30                 pypi_0    pypi  
openssl                   1.1.1t               h2bbff1b_0  
pandas                    1.1.5                    pypi_0    pypi  
parso                     0.7.1                    pypi_0    pypi  
pickleshare               0.7.5                    pypi_0    pypi  
pillow                    8.4.0                    pypi_0    pypi  
pip                       21.3.1                   pypi_0    pypi  
prompt-toolkit            3.0.36                   pypi_0    pypi  
protobuf                  3.19.6                   pypi_0    pypi  
psutil                    5.9.4                    pypi_0    pypi  
pyasn1                    0.4.8                    pypi_0    pypi  
pyasn1-modules            0.2.8                    pypi_0    pypi  
pycocotools               2.0.6                    pypi_0    pypi  
pycparser                 2.21                     pypi_0    pypi  
pygments                  2.14.0                   pypi_0    pypi  
pymysql                   1.0.2                    pypi_0    pypi  
pyparsing                 3.0.9                    pypi_0    pypi  
python                    3.6.13               h3758d61_0  
python-dateutil           2.8.2                    pypi_0    pypi  
pytz                      2022.7                   pypi_0    pypi  
pyyaml                    6.0                      pypi_0    pypi  
requests                  2.27.1                   pypi_0    pypi  
requests-oauthlib         1.3.1                    pypi_0    pypi  
rsa                       4.9                      pypi_0    pypi  
scipy                     1.5.4                    pypi_0    pypi  
seaborn                   0.11.2                   pypi_0    pypi  
setuptools                58.0.4           py36haa95532_0  
six                       1.16.0                   pypi_0    pypi  
typing-extensions         4.1.1                    pypi_0    pypi  
urllib3                   1.26.13                  pypi_0    pypi  
vc                        14.2                 h21ff451_1  
vs2015_runtime            14.27.29016          h5e58377_2  
wcwidth                   0.2.5                    pypi_0    pypi  
werkzeug                  2.0.3                    pypi_0    pypi  
wheel                     0.37.1             pyhd3eb1b0_0  
wincertstore              0.2              py36h7fe50ca_0  
zipp                      3.6.0                    pypi_0    pypi  
```
## 2.分别打开两个工程,并激活相应的环境
yolov5工程在pytorch环境下运行detect.py,前端工程运行以下指令
```
conda activate pytorch
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```
记得修改数据集的路径
yolov5.7/detcet.py/95行
修改前端引用yolov5的路径
djangoPtoject/appo1/views.py/141行
## 3.后续想起来再补.......
