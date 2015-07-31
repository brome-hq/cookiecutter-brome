#! -*- coding: utf-8 -*-

from brome.core.model.utils import *

from model.basetest import BaseTest
from model.user import User

class Test(BaseTest):

    name = 'Test'

    def create_state(self):
        self.user = User(pdriver = self.pdriver, username = 'test')
        self.integer = 1
        self.float_ = 1.0

    def run(self, **kwargs):

        self.info_log("Running...")

        #TEST
