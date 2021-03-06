# -*- coding: utf-8 -*-
"""soft_max.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15t90cr9YI80jBZglVcAiJ40hXZ5a298k

# **SoftMax**
---
> 다중 분류(Multi Classification)문제에서 최종 출력 값을 정규화 하는 함수
* 입력 값을 [0:1]사이의 값으로 정규화 --> 출력 값의 합은 1
* 지수함수(exponential)를 사용하여 연산시 overflow 문제가 발생 가능 --> 입력 값중 최대값을 더해줘서 지수함수 연산을 하여 문제 해결
![SoftMax](https://docs.google.com/uc?export=download&id=1ZHvjiZ4FEJr08rKiWebjiqpoSmoqJEcF)
"""

import numpy as np
import math

def SoftMax(arr):
    max_value = np.max(arr)
    exp_arr = np.exp(arr - max_value)
    sum_arr = np.sum(exp_arr)
    return exp_arr / sum_arr

def SoftMaxUsingList(arr):
    max_value = max(arr)
    exp_arr = [math.exp(i - max_value) for i in arr]
    sum_arr = sum(exp_arr)
    return [(i/sum_arr) for i in exp_arr]

output = [1.22, 1.67, 3.45, 5.23, 2.11, 3.34, 2.33, 0.55, 4.44, 4.1]

output_from_softmax_using_list = SoftMaxUsingList(output)
print("\n\n=========================== SoftMax Using List ==================================")
print("\n".join([str(x) for x in output_from_softmax_using_list]))

output_from_softmax = SoftMax(np.array(output))
print("=========================== SoftMax Using Numpy ==================================")
print("\n".join([str(x) for x in output_from_softmax]))

