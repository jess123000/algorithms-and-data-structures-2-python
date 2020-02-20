#!/usr/bin/env python3

# ----------------------------------------------------------------------
# test_AreaCodes.py
# Alex Harris
# 08/24/19

# ----------------------------------------------------------------------

import sys
import os
import unittest

sys.path.insert(0, '..')
from AreaCodes import *

# ----------------------------------------------------------------------

class AreaCodesTest(unittest.TestCase):

    # ------------------------------------------------------------------

    def setUp(self) -> None:
        for f in ("areacodes.csv", "../areacodes.csv", "/Users/dreed/Capital/CS361/src/AreaCodes/areacodes.csv"):
            if os.path.exists(f):
                filename = f

        self.codes = AreaCodes(filename)

    # ------------------------------------------------------------------

    def tearDown(self) -> None:
        del self.codes

    # ------------------------------------------------------------------

    def testRegionForAreaCode(self):
        r = AreaCodes()
        region = r.regionForAreaCode("614")
        self.assertEqual(region, "OH")

    # ------------------------------------------------------------------

    def testAreaCodeForRegion(self):
        r = AreaCodes()
        areaCodes = r.areaCodesForRegion("OH")
        self.assertEqual(areaCodes, ("216", "220", "234", "283", "330", "380", "419", "440", "513", "567", "614", "740", "937"))
        areaCodes = r.areaCodesForRegion("ASIA")
        self.assertEqual(areaCodes, ())

    # ------------------------------------------------------------------

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
