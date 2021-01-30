#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import pytest
import yaml

sys.path.append('..')
print(sys.path)
from pythoncode.Calculator import Calculator


def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    return (datas['add']['datas'], datas['add']['ids'])


def get_MultiDatas():
    with open("./datas/calc.yml") as f:
        multiDatas = yaml.safe_load(f)
        return (multiDatas['Multi']['datas'], multiDatas['Multi']['ids'])


def get_DivDatas():
    with open("./datas/calc.yml") as f:
        divDatas = yaml.safe_load(f)
        return (divDatas['Div']['datas'], divDatas['Div']['ids'])

# yaml json excel csv xml
# 测试类
class TestCalc:
    datas: list = get_datas()

    Multi_datas = get_MultiDatas()
    Div_datas = get_DivDatas()

    # 前置条件
    def setup(self):
        print("方法开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown(self):
        print("方法结束计算")

    @pytest.mark.parametrize("a, b, result", datas[0], ids=datas[1])
    def test_add(self, a, b, result):
        print(f"a={a} , b ={b} ,result={result}")
        assert result == self.calc.add(a, b)

    def test_add1(self):
        datas = [[1, 1, 2], [100, 200, 300], [1, 0, 1]]
        for data in datas:
            print(data)
            assert data[2] == self.calc.add(data[0], data[1])

    @pytest.mark.parametrize("a, b, result", Multi_datas[0], ids=Multi_datas[1])
    def test_Multi(self, a, b, result):
        print(f"Test muti function: first one is : {a}, the second one is : {b}")
        assert result == self.calc.Multi(a, b)

    @pytest.mark.parametrize("a, b, result", Div_datas[0], ids=Div_datas[1])
    def test_div(self, a, b, result):
        print(f"Test div function: first num is : {a}, the second num is : {b}")
        assert result == self.calc.div(a, b)
