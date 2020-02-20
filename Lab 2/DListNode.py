#!/usr/bin/env python3

# ----------------------------------------------------------------------
# DListNode.py
# Dave Reed
# 06/11/2019
# ----------------------------------------------------------------------

from __future__ import annotations

class DListNode:

    """
    node class for storing a value and references to previous and next nodes
    """

    # ------------------------------------------------------------------

    def __init__(self, item, prev: DListNode = None, next: DListNode = None):
        self.item = item
        self.prev = prev
        self.next = next

    # ------------------------------------------------------------------

# ----------------------------------------------------------------------
