#!/usr/bin/env python3

# ----------------------------------------------------------------------
# test_DListCursor.py
# Alex Harris
# 09/14/19

# ----------------------------------------------------------------------

import sys
import unittest
import copy

sys.path.insert(0, '..')
from DListCursor import *

# ----------------------------------------------------------------------

class DListCursorTest(unittest.TestCase):

    # ------------------------------------------------------------------

    def checkList(self, items, array, cursorValue = None):

        # check length
        self.assertEqual(len(items), len(array))

        # check forward iterator
        values = [x for x in items]
        self.assertEqual(values, array)
        # check reverse iterator
        values = [x for x in items.reverseIter()]
        self.assertEqual(values, list(reversed(array)))

        # test get item operator
        for i in range(len(array)):
            self.assertEqual(items[i], array[i])

        # check cursor value
        if len(items) > 0 and cursorValue is not None:
            self.assertEqual(items.itemAtCursor(), cursorValue)

        # check same string representation
        self.assertEqual(str(items), str(array))

        # check cursor methods
        if len(items) > 1:
            newList = copy.copy(items)
            if cursorValue is not None:
                self.assertEqual(newList.itemAtCursor(), cursorValue, "copy does not set cursor")
            newList.cursorToHead()
            self.assertTrue(newList.isCursorAtHead())
            self.assertFalse(newList.isCursorAtTail())
            self.assertEqual(newList.itemAtCursor(), array[0])
            newList.cursorToTail()
            self.assertTrue(newList.isCursorAtTail())
            self.assertFalse(newList.isCursorAtHead())
            self.assertEqual(newList.itemAtCursor(), array[-1])

    # ------------------------------------------------------------------

    def testEmpty(self):
        items = DListCursor()
        array = []
        self.checkList(items, array)

    # ------------------------------------------------------------------

    def testAppendOneValue(self):
        items = DListCursor()
        items.append(42)
        self.checkList(items, [42], 42)

    # ------------------------------------------------------------------

    def testItemAtAndAppend(self):
        items = DListCursor()
        items.append(12)
        self.assertEqual(items.itemAtCursor(), 12)
        self.assertEqual(items.itemAtHead(), 12)
        self.assertEqual(items.itemAtTail(), 12)
        items.append(24)
        items.append(32)
        items.append(45)
        items.append(65)
        self.assertEqual(items.itemAtHead(), 12)
        self.assertEqual(items.itemAtCursor(), 12)
        self.assertEqual(items.itemAtTail(), 65)

    # ------------------------------------------------------------------

    def testGetItemAndSetItem(self):
        items = DListCursor()
        for i in range(10):
            items.append(i)
        for i in range(10):
            self.assertEqual(items[i], i)
        for i in range(10):
            items[i] = i+10
        for i in range(10):
            self.assertEqual(items[i], i+10)

# ----------------------------------------------------------------------

    def testCopy(self):
        items = DListCursor()
        for i in range(5):
            items.append(i)
        items.cursorForward()
        items.cursorForward()
        items2 = items.__copy__()
        for i in items:
            self.assertEqual(items[i], items2[i])
        self.assertEqual(items.itemAtHead(), items2.itemAtHead())
        self.assertEqual(items.itemAtCursor(), items2.itemAtCursor())
        self.assertEqual(items.itemAtTail(), items2.itemAtTail())

# ----------------------------------------------------------------------

    def testString(self):
        items = DListCursor()
        for i in range(5):
            items.append(i)
        itemsCorrect = []
        for i in range(5):
            itemsCorrect.append(i)
        self.assertEqual(str(items), str(itemsCorrect))

# ----------------------------------------------------------------------

    def testInsertAtHead(self):
        items = DListCursor()
        for i in range(5):
            items.insertAtHead(i)
        self.assertEqual(items[0], 4)
        self.assertEqual(items[1], 3)
        self.assertEqual(items[2], 2)
        self.assertEqual(items[3], 1)
        self.assertEqual(items[4], 0)
        self.assertEqual(items.itemAtHead(), 4)
        self.assertEqual(items.itemAtCursor(), 0)
        self.assertEqual(items.itemAtTail(), 0)

# ----------------------------------------------------------------------

    def testRemoveAtHead(self):
        items = DListCursor()
        for i in range(5):
            items.append(i)
        items.removeAtHead()
        self.assertEqual(items.itemAtHead(), 1)
        items.removeAtHead()
        self.assertEqual(items.itemAtHead(), 2)
        items.removeAtHead()
        self.assertEqual(items.itemAtHead(), 3)
        items.removeAtHead()
        self.assertEqual(items.itemAtHead(), 4)
        items.removeAtHead()
        self.assertEqual(len(items), 0)

# ----------------------------------------------------------------------

    def testPop(self):
        items = DListCursor()
        for i in range(5):
            items.append(i)
        for i in range(4):
            items.cursorForward()
        item = items.pop()
        self.assertEqual(item, 4)
        self.assertEqual(items.itemAtTail(), 3)
        self.assertEqual(items.itemAtCursor(), 3)
        for i in range(2):
            items.cursorBackward()
        item = items.pop()
        self.assertEqual(item, 3)
        self.assertEqual(items.itemAtTail(), 2)
        item = items.pop()
        self.assertEqual(item, 2)
        self.assertEqual(items.itemAtTail(), 1)
        item = items.pop()
        self.assertEqual(item, 1)
        self.assertEqual(items.itemAtTail(), 0)
        self.assertEqual(items.itemAtCursor(), 0)
        item = items.pop()
        self.assertEqual(item, 0)
        self.assertEqual(len(items), 0)


# ----------------------------------------------------------------------

    def testInsertBeforeAndAfterCursor(self):
        items = DListCursor()
        items.insertAfterCursor(3)
        items.insertBeforeCursor(1)
        items.insertAfterCursor(4)
        items.cursorBackward()
        items.insertAfterCursor(2)
        for i in range(3):
            items.cursorForward()
        items.insertAfterCursor(5)
        items2 = []
        for i in range(1, 6):
            items2.append(i)
        self.assertEqual(str(items), str(items2))
        self.assertEqual(items.itemAtHead(), "1")
        self.assertEqual(items.itemAtTail(), "5")

# ----------------------------------------------------------------------

    def testRemoveCursor(self):
        items = DListCursor()
        for i in range(5):
            items.append(i)
        items.removeCursor()
        self.assertEqual(items.itemAtCursor(), 1)
        for i in range(3):
            items.cursorForward()
        items.removeCursor()
        self.assertEqual(items.itemAtCursor(), 3)
        items.cursorBackward()
        items.removeCursor()
        self.assertEqual(items.itemAtCursor(), 3)
        items.removeCursor()
        self.assertEqual(items.itemAtCursor(), 1)
        items.removeCursor()
        self.assertEqual(len(items), 0)

# ----------------------------------------------------------------------


def main(argv):
    try:
        unittest.main()
    except SystemExit as inst:
        # raised by sys.exit(True) when tests failed
        if inst.args[0] is True:
            raise


# ----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
