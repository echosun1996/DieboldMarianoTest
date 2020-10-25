# Diebold Mariano Test 工具包

![Python package](https://github.com/echosun1996/DieboldMarianoTest/workflows/Python%20package/badge.svg)
![PyPI version](https://badge.fury.io/py/diebold-mariano-test.svg)
![Python](https://img.shields.io/pypi/pyversions/diebold-mariano-test.svg?style=plastic)

## 特点
通过DM检验的结果，可以判别任意两类算法的预测结果是否存在差异性。

## 安装

```bash
pip install diebold-mariano-test
```

## 更新

```bash
pip install --upgrade diebold-mariano-test
```

## 使用说明

```bash
>>> # 导入包
>>> from diebold_mariano_test import *

>>> ori_list = [3, 5, 4, 1]  # 原始时间序列数据
>>> a1_list = [2, 3, 4, 2]  # 预测算法一得到的时间序列数据
>>> a2_list = [3, 2, 2, 4]  # 预测算法二得到的时间序列数据

>>> # 使用MSE方法计算 Diebold-Mariano Test.
>>> d_t_list = cul_d_t(MSE, ori_list, a1_list, a2_list)
>>> print(d_t_list)  # 输出中间变量d_t的数值。 
[1, -4, -8, -16]
>>> cul_DM(d_t_list)  # 输出结果
-2.254898764780173
>>> cul_P(d_t_list) # 输出伴随的P值
0.024139683878213303

>>> # 使用MAE方法计算 Diebold-Mariano Test.
>>> d_t_list = cul_d_t(MAE, ori_list, a1_list, a2_list)
>>> print(d_t_list)  # 输出中间变量d_t的数值。 
[1, 0, -2, -4]
>>> cul_DM(d_t_list)  # 输出结果
-1.4213381090374029
>>> cul_P(d_t_list) # 输出伴随的P值
0.155218489684684
``` 

## 说明

项目发布于PyPI：[单击访问](https://pypi.org/project/diebold-mariano-test/) 

本模块尚不完善，有任何相关问题或建议，欢迎在本项目的github页面中提交issue: [单击访问](https://github.com/echosun1996/DieboldMarianoTest)

# License
GNU General Public License v3.0