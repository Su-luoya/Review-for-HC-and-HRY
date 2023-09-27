# -*- coding: utf-8 -*-
# @Author: 昵称有六个字
# @Date:   2023-09-27 13:23:46
# @Last Modified by:   昵称有六个字
# @Last Modified time: 2023-09-27 13:41:46
"""First of all, you may need a `Data Cache Wrapper` for your project."""

import sys
from pathlib import Path
from typing import Callable

import pandas as pd
import pretty_errors  # This package is used to generate pretty errors, so just keep it here
from icecream import ic  # Use `ic` to print info instead of using `print`

ic.configureOutput(prefix="")

sys.path.append(str(Path.cwd()))
from src.setting import Setting


class Cache(object):
    """
    Data Cache Wrapper.
    --------
    1. If argument "test" is True, execute the given function/method without reading or saving data.
    2. If the cache exists, load data from the file.
    3. If the cache does not exist, call the function/method and save return data to the file.
    4. Prevent duplicate cache reads.

    Args:
    --------
        file_path (str): The relative path of the csv file.
        test (bool, optional): If True, do not read or cache data. Defaults to True.
        func (Callable[..., pd.DataFrame]): The function/method to be executed.

    Usages:
    -------
        ```python
        >>> from pandas import DataFrame
        >>> @Cache(file_path="test/test.csv", test=False)
        >>> def func(*args, **kwargs) -> DataFrame:
        >>>     ...
        >>>     return df
        >>> df: DataFrame = func(*args, **kwargs)
        ```
    """

    # Prevent repeat cache reads.
    path_dict: dict[Path, pd.DataFrame] = {}

    def __init__(self, file_path: str, test: bool = True) -> None:
        self.file_path: str = file_path  # File's path
        self.cache_path: Path = Path(
            f"{Setting.data_path}/{file_path}"
        ).resolve()  # Absolute path
        self.test: bool = test
        self.file_type: str | None = None

    def __call__(
        self, func: Callable[..., pd.DataFrame]
    ) -> Callable[..., pd.DataFrame | None]:
        def wrapper(*args, **kwargs) -> pd.DataFrame | None:
            # If argument "test" is True.
            if self.test:
                ...
                # Execute the given function/method without reading or saving data.
                df = pd.DataFrame()
            # Prevent duplicate cache reads.
            if self.cache_path in self.path_dict:
                return self.path_dict[self.cache_path]
            # Check file existence.
            if self.cache_path.exists():
                # The cache exists, load data from the file.
                ...
                df = pd.DataFrame()
            else:
                # The cache does not exist,
                # call the function/method and save return data to the file.
                ...
                df = pd.DataFrame()
            # Record data that has been read.
            self.path_dict[self.cache_path] = df
            return df

        return wrapper

    def read_file(self) -> pd.DataFrame:
        """Read data from a csv file."""
        ...
        return pd.DataFrame()

    def save_file(self, df: pd.DataFrame) -> pd.DataFrame:
        """Save data into a csv or excel file."""
        # Directory generator.
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        # Read cache file.
        ...
        return pd.DataFrame()


class TestCacheData:
    """Test DataFrame"""

    @Cache(file_path="cache/test1.csv", test=False)
    def test_df1(self) -> pd.DataFrame:
        return pd.DataFrame(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            columns=["A", "B", "C"],
        )

    @Cache(file_path="test/test1.csv", test=False)
    def test_df2(self) -> pd.DataFrame:
        return pd.DataFrame(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 10],
            ],
            columns=["D", "E", "F"],
        )


if __name__ == "__main__":
    # You can test your code here ⬇️
    test = TestCacheData()
    ic(test.test_df1())
    ic(test.test_df2())
