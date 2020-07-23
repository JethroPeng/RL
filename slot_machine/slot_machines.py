# -*- coding:utf-8 -*-
# Python实现老虎机
import numpy as np
import math
import random

class slot_machine:
    u = []
    sig = []
    def __init__(self,k,u=[],sig=[]):
        # 不传默认第k个壁的均值为k
        self.k = k
        if (len(u)==k)&(len(sig)==k):
            self.u = u[:]
            self.sig = sig[:]
        else:
            for i in range(k):
                self.u.append(i+1)
                self.sig.append(10)
    def setu(self,u,k=0):
        if (k==0):
            self.u = u
        else:
            self.u[k-1] = u
    def setsig(self,sig,k=0):
        if (k==0):
            self.sig = sig[:]
        else:
            self.sig[k - 1] = sig
    def randomNum(self,k):
        return random.gauss(self.u[k-1],self.sig[k-1])