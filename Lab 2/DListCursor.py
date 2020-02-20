#!/usr/bin/env python3

# ----------------------------------------------------------------------
# DListCursor.py
# Alex Harris
# 09/10/2019
# ----------------------------------------------------------------------

from __future__ import annotations
from DListNode import DListNode

class DListCursor:

    """
    double linked list with invariant that size indicates number of items in the list and
    if list is empty, head, cursor, and tail cursor are None
    if list not empty, head points to first DListNode, tail points to last DListNode, cursor points to some DListNode
    inserting does not change the cursor unless the list was empty in which case cursor points to new node
    deleting does not change cursor unless cursor is the node being deleted
    if the cursor is the node being deleted, if there is a node after the cursor, it is set to that node; if the cursor
    is deleted and there is not a node after the cursor, the cursor is set to the node before it; if the list is now
    empty the cursor is set to None
    """

    # ------------------------------------------------------------------

    def __init__(self):
        self.head = self.cursor = self.tail = None
        self.size = 0

    # ------------------------------------------------------------------

    def __iter__(self):
        """
        forward iterator for list
        """
        node = self.head
        while node is not None:
            yield node.item
            node = node.next

    # ------------------------------------------------------------------

    def reverseIter(self):
        """
        reverse iterator for list
        """
        node = self.tail
        while node is not None:
            yield node.item
            node = node.prev

    # ------------------------------------------------------------------

    def __copy__(self) -> DListCursor:
        """
        shallow copy of list; note: cursor in copy must point to node at same position in new list as cursor in original list
        :return: a new DListCursor with new nodes for each item (but does not make a deep copy of item stored at node)
        """
        # create a new list
        newList = DListCursor()
        # initial node to the head of the original list
        node = self.head
        # append every node with i being a node
        for i in self:
            newList.append(i)
        # reinitialize node to head of original
        node = self.head
        # for every node
        for i in range(self.size):
            # check if the node is the cursor
            if node == self.cursor:
                # if the node is the cursor, i is the index of the cursor
                index = i
                break
            # else move the node to the next node
            else:
                node = node.next
        # reinitialize node to the head of the new list
        node = newList.head
        # step through till we get to the cursor to be
        for i in range(index):
            node = node.next
        # make node the cursor
        newList.cursor = node
        return newList

    # ------------------------------------------------------------------

    def __len__(self) -> int:
        """
        :return: number of items in the list
        """
        return self.size

    # ------------------------------------------------------------------

    def __str__(self):
        """
        :return: string representation of the list (works same as str representation of a built-in list)
        """
        if self.size == 0:
            return "[]"
        else:
            # turn all node items into strings
            node = self.head
            for i in range(self.size):
                node.item = str(node.item)
                node = node.next
            node = self.head
            # create a list to store the strings
            output = []
            # append the beginning bracket
            output.append("[")
            # for every node except the last one append the printed list structure
            while node.next is not None:
                if node.item is str:
                    output.append("'")
                    output.append(node.item)
                    output.append("', ")
                else:
                    output.append(node.item)
                    output.append(", ")
                node = node.next
            # for the last node append the item and the end bracket
            output.append(node.item)
            if node.item is str:
                output.append("'")
            output.append("]")
            # join the strings together to create our beautiful string
            final = "".join(output)
            return final

    # ------------------------------------------------------------------

    def __getitem__(self, position):
        """
        return the value at specified position in the list
        :param position: location in list 0 to size - 1
        :post: raises an error if position is not a valid index
        :return: value at specified location in list
        """
        # if the list is empty or the position is too high raise an error
        if (self.size == 0) or (position > self.size - 1):
            raise IndexError("Invalid index")
        else:
            # else find the node at the position and return the item of it
            return self._find(position).item

    # ------------------------------------------------------------------

    def __setitem__(self, position, value) -> None:
        """
        set the value at the specified position in the list
        :param position: position: location in list 0 to size - 1
        :param value: new value for specified position
        :post: raises an error if position is not a valid index
        :return: None
        """
        # if the list is empty or the position is too high raise an error
        if (self.size == 0) or (position > self.size - 1):
            raise IndexError("Invalid index")
        else:
            # else find the node and change the value of it
            self._find(position).item = value

    # ------------------------------------------------------------------

    def itemAtHead(self):
        """
        :post: raises an error if list empty
        :return: item at first location in list
        """
        # if the size is zero the list is empty and an error is raised
        if self.size == 0:
            raise ValueError("List is empty.")
        else:
            # else return the item at the head
            return self.head.item

    # ------------------------------------------------------------------

    def itemAtCursor(self):
        """
        :post: raises an error if list empty
        :return: item at cursor location in list
        """
        # if the size is zero the list is empty and an error is raised
        if self.size == 0:
            raise ValueError("List is empty.")
        else:
            # else return the item at the cursor
            return self.cursor.item

    # ------------------------------------------------------------------

    def itemAtTail(self):
        """
        :post: raises an error if list empty
        :return: item at last location in list
        """
        # if the size is zero the list is empty and an error is raised
        if self.size == 0:
            raise ValueError("List is empty.")
        else:
            # else return the item at the tail
            return self.tail.item

    # ------------------------------------------------------------------

    def cursorToHead(self) -> None:
        """
        moves cursor to head of list
        :return: None
        """
        # if the list is empty it isn't possible to move it to the head
        if self.size == 0:
            return
        else:
            # else move it there
            self.cursor = self.head

    # ------------------------------------------------------------------

    def cursorToTail(self) -> None:
        """
        moves cursor to tail end of list
        :return: None
        """
        # if the list is empty it isn't possible to move it to the tail
        if self.size == 0:
            return
        else:
            # else move it there
            self.cursor = self.tail

    # ------------------------------------------------------------------

    def isCursorAtHead(self) -> bool:
        """
        :return: True if cursor at head of list or list empty, False otherwise
        """
        # if the list is empty False
        if self.size == 0:
            return False
        # else if the cursor is the head True
        elif self.cursor == self.head:
            return True

    # ------------------------------------------------------------------

    def isCursorAtTail(self) -> bool:
        """
        :return: True if cursor at tail end of list or list empty, False otherwise
        """
        # if the list is empty False
        if self.size == 0:
            return False
        # else if the cursor is the tail True
        elif self.cursor == self.tail:
            return True

    # ------------------------------------------------------------------

    def cursorForward(self) -> bool:
        """
        moves cursor forward one node if cursor not at end of list and list not empty
        :return: True if cursor moved, false, otherwise
        """
        # if the list is empty, or the cursor's at the end False
        if self.size == 0 or self.cursor == self.tail:
            return False
        else:
            # else move it forward
            self.cursor = self.cursor.next
            return True

    # ------------------------------------------------------------------

    def cursorBackward(self) -> bool:
        """
        moves cursor backward one node if cursor not at beginning of list and list not empty
        :return: True if cursor moved, false, otherwise
        """
        # if the list is empty, or the cursor's at the beginning False
        if self.size == 0 or self.cursor == self.head:
            return False
        else:
            # else move it backward
            self.cursor = self.cursor.prev
            return True

    # ------------------------------------------------------------------

    def insertAtHead(self, item) -> None:
        """
        insert item at beginning of list
        :param item: value to insert
        :return: None
        """
        # if the list is empty append it normally
        if self.size == 0:
            self.append(item)
        else:
            # else create a new node
            node = DListNode(item)
            # make the current head's previous the new node
            self.head.prev = node
            # make the new node's next the current head
            node.next = self.head
            # change the head to the new node
            self.head = node
            # increase the size
            self.size += 1

    # ------------------------------------------------------------------

    def removeAtHead(self):
        """
        remove item at beginning of list and return it
        :post: raises an assertion error if list empty
        :return: the value that was first in the list
        """
        # if the list is empty raise an error
        if self.size == 0:
            raise AssertionError("List is empty.")
        # else if the list has one item in it, return the list back to it's initialized state
        elif self.size == 1:
            # save the node to return
            node = self.head
            self.head = self.cursor = self.tail = None
            self.size = 0
            return node.item
        else:
            # save the node to return
            node = self.head
            # mode the head to the new head
            self.head = self.head.next
            # make the old head's next None
            self.head.prev.next = None
            # make the new head's previous None
            self.head.prev = None
            # if the old head was the cursor, move the cursor to the new head
            if node == self.cursor:
                self.cursor = self.head
            # decrease the size
            self.size -= 1
            return node.item

    # ------------------------------------------------------------------

    def append(self, item) -> None:
        """
        insert item at end of list
        :param item: value to insert
        :return: None
        """
        # create the new node
        node = DListNode(item)
        # if the list is empty, set everything to that node
        if self.size == 0:
            self.head = self.cursor = self.tail = node
        else:
            # the previous node of the new node should be the current tail
            node.prev = self.tail
            # the current tail's next node needs to be the new node
            self.tail.next = node
            # the tail needs to be updated to the new node
            self.tail = node
        # increase the size
        self.size += 1

    # ------------------------------------------------------------------

    def pop(self):
        """
        remove item at end of list and return it
        :post: raises an assertion error if list empty
        :return: the value that was last in the list
        """
        # if the list is empty, raise error
        if self.size == 0:
            raise AssertionError("List is empty.")
        # else if the tail is the head there is only one node
        elif self.tail == self.head:
            # for return
            node = self.tail
            # reinitialize the node and the list and return
            self.head = self.cursor = self.tail = None
            self.size = 0
            return node.item
        # else if the tail is the cursor
        elif self.tail == self.cursor:
            # for return
            node = self.tail
            # nothing after the cursor so the cursor becomes the prev node
            self.cursor = self.tail.prev
            # make the new cursor not point to the tail being deleted
            self.cursor.next = None
            # make the tail being deleted not point to anything
            self.tail.prev = None
            # make the new tail the new cursor
            self.tail = self.cursor
            # decrease the size and return
            self.size -= 1
            return node.item
        else:
            # for return
            node = self.tail
            # make the new tail the previous node of the current tail
            self.tail = self.tail.prev
            # make the new tail's next not point to the old tail and return
            self.tail.next = None
            self.size -= 1
            return node.item

    # ------------------------------------------------------------------

    def insertBeforeCursor(self, item) -> None:
        """
        insert item before the cursor node; if list empty, inserts the item as the only value in the list
        :param item: value to insert
        :return: None
        """
        # if the cursor is the head call insert at head
        if self.cursor == self.head:
            self.insertAtHead(item)
        # else if the list is empty, append normally
        elif self.size == 0:
            self.append(item)
        else:
            node = DListNode()
            # make the new node and cursor's previous point to each other
            self.cursor.prev.next = node
            node.prev = self.cursor.prev
            # make the new node and the cursor point to each other
            self.cursor.prev = node
            node.next = self.cursor
            self.size += 1

    # ------------------------------------------------------------------

    def insertAfterCursor(self, item):
        """
        insert item after the cursor node; if list empty, inserts the value as the only item in the list
        :param item: value to insert
        :return: None
        """
        # if the cursor is the tail or if the list is empty, append normally
        if (self.cursor == self.tail) or (self.size == 0):
            self.append(item)
        else:
            node = DListNode(item)
            # make the new node and the cursor's next point to each other
            self.cursor.next.prev = node
            node.next = self.cursor.next
            # make the new node and the cursor point to each other
            self.cursor.next = node
            node.prev = self.cursor
            self.size += 1

    # ------------------------------------------------------------------

    def removeCursor(self):
        """
        removes and returns the value at the cursor
        see the invariant for how to update the cursor
        :return: the value at the cursor
        """
        # if the cursor is the head, remove the head normally
        if self.cursor == self.head:
            self.removeAtHead()
        # if the cursor is the tail, pop the tail normally
        elif self.cursor == self.tail:
            self.pop()
        else:
            # for return
            node = self.cursor
            # make the cursor's next point and the cursor's previous point to each other
            self.cursor.next.prev = self.cursor.prev
            self.cursor.prev.next = self.cursor.next
            # set the new cursor to the current cursor's next node
            self.cursor = node.next
            self.size -= 1

    # ------------------------------------------------------------------

    def _find(self, position) -> DListNode:
        """
        private helper method to return the node at the specified position
        :param position: index of the node to return
        :return: node at the specified position
        """
        # initialize the find
        node = self.head
        # if the position of the node in question is 0 then it's the current node
        if position == 0:
            return node
        else:
            # step through until the node in question is found
            for i in range(position):
                node = node.next
            # return the node we want
            return node

    # ------------------------------------------------------------------

# ----------------------------------------------------------------------