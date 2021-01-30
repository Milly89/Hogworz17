#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 被测类：计算器
class Calculator:
    def add(self, a, b):
        return a + b

    def Multi(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            print("分母为0，输入不合法！")
        else:
            return a / b
