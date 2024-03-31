#!/usr/bin/env python3
"""module for the class Server"""

import csv
from math import ceil
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int]:
    """return a tuple of size two containing a start index and an end index"""
    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        min_idx, max_idx = index_range(page, page_size)
        try:
            return self.dataset()[min_idx:max_idx]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns a dictionary containing information
        """
        total_pages = ceil(len(self.dataset()) / page_size)
        return {
                'page_size': page_size,
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': page + 1 if total_pages > page else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
                }
