#!/usr/bin/env python3
"""
Calculate the start and end indices for pagination.

Parameters:
- page: Current page number.
- per_page: Number of items to display per page.

Returns:
A tuple of size two containing the start and end indices.
"""


def index_range(page, page_size):
    """Calculate the start and end indices for pagination."""
    start = (page - 1) * page_size
    end = start + page_size

    return start, end
