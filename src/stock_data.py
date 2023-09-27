# -*- coding: utf-8 -*-
# @Author: 昵称有六个字
# @Date:   2023-09-27 12:56:43
# @Last Modified by:   昵称有六个字
# @Last Modified time: 2023-09-27 13:44:27
"""This is a `StockData` class."""

import sys
from pathlib import Path

import baostock as bs  # http://baostock.com/baostock/index.php/A股K线数据
import pandas as pd
import pretty_errors  # This package is used to generate pretty errors, so just keep it here
from icecream import ic  # Use `ic` to print info instead of using `print`
from tqdm import (  # If you need to get more than two stocks' info, try this package to add a progress bar
    tqdm,
    trange,
)

ic.configureOutput(prefix="")
sys.path.append(str(Path.cwd()))
from src.cache import Cache


class StockData(object):
    """
    Stock Return Data
    ------

    Args:
    ------
        names: list, default=['贵州茅台', '五粮液']
        start_date: str, default='2019-12-01'
        end_date: str, default='2020-12-31'
        frequency: str, default='d'
        adjustflag: str, default='3'

    Usages:
    ------
        ```python
        >>> stock_data = StockData(
        ...         names=["贵州茅台", "五粮液"],
        ...         start_date="2019-12-01",
        ...         end_date="2020-12-31",
        ...         frequency="d",
        ...         adjustflag="3"
        ...         )
        >>> stock_info: dict = stock_data.stock_info()
        >>> df_ret: pd.DataFrame = stock_data.stock_data()
        ```
    """

    def __init__(
        self,
        names: list[str] = ["贵州茅台", "五粮液"],
        start_date: str = "2019-12-01",
        end_date: str = "2020-12-31",
        frequency: str = "d",  # d:日线 w:周线 m:月线
        adjustflag: str = "3",  # 1:后复权 2:前复权 3:不复权
    ) -> None:
        self.names: list[str] = names
        self.start_date: str = start_date
        self.end_date: str = end_date
        self.frequency: str = frequency
        self.adjustflag: str = adjustflag

    def stock_info(self) -> dict[str, dict[str, str]]:
        """
        Use `bs.query_stock_basic` API to get stocks' codes and ipo dates from their names

        Return a dict like this:
        ```python
            {
            '贵州茅台': {'code': 'sh.600519', 'ipoDate': '2001-08-27'},
            '隆基股份': {'code': 'sh.601012', 'ipoDate': '2012-04-11'},
            ...
            }
        ```

        `code` is to get price data, and `ipoDate` is to check whether the stock is listed before `start_date`
        """
        ...

    @Cache(file_path="stock_return.csv", test=False)
    def stock_data(self) -> pd.DataFrame:
        """
        Return a DataFrame containing all the stocks data
        What you need is `date,code,pctChg`
        """
        stock_info: dict[str, dict[str, str]] = self.stock_info()
        ...
        return pd.DataFrame()


if __name__ == "__main__":
    # You can test your code here ⬇️
    stock_data = StockData()
    # stock_data.stock_info()
    df_ret = stock_data.stock_data()
