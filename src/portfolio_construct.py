# -*- coding: utf-8 -*-
# @Author: 昵称有六个字
# @Date:   2023-09-27 12:57:01
# @Last Modified by:   昵称有六个字
# @Last Modified time: 2023-09-27 14:01:36
"""Markovitz Portfolio"""

import math
from pathlib import Path
import random
import sys
import time
from functools import reduce
from itertools import combinations, product

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from icecream import ic
import pretty_errors
import scipy.optimize as sco
from tqdm import tqdm, trange

ic.configureOutput(prefix="")

sys.path.append(str(Path.cwd()))
from src.cache import Cache

plt.rcParams["font.sans-serif"] = ["FangSong"]
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
plt.rcParams["font.size"] = 13


class Markovitz(object):
    """
    Markovitz Portfolio
    ------
    1. Construct portfolios by generating random weights and choose the best one with the highest `Sharpe Ratio`.
    2. Plot the `Efficient Frontier` and the `CML`.
    3. Optimize the portfolio by using `scipy.optimize.minimize`, and compare it to the result by generating random weights.
    4. Since stocks require an integer number of shares, how could you fix this problem with your fund? i.e. 10,000,000 yuan
    """

    def __init__(
        self,
        names=["比亚迪", "阳光电源", "璞泰来", "紫光国微", "盛新锂能"],
        start_date="2021-05-01",
        end_date="2021-11-01",
        frequency="d",
        rfr=0.023467,
        funds=10000000,
    ):
        self.names = names
        self.lens = len(names)
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency
        self.rfr = (rfr * 100) / {"d": 365, "w": 52, "m": 30}[frequency]
        self.funds = funds

    ...


if __name__ == "__main__":
    # Test your code here
    ...
