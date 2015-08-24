#!/usr/bin/env python

import sys

from brome import Brome

from model.selector import selector_dict
from browser_config.main_config import browsers_config
from model.test_dict import test_dict

if __name__ == '__main__':

    brome = Brome(
        config_path = "",
        selector_dict = selector_dict,
        test_dict = test_dict,
        browsers_config = browsers_config
    )

    brome.execute(sys.argv)
