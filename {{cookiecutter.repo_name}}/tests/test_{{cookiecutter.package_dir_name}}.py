#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.package_dir_name }}
----------------------------------

Tests for `{{ cookiecutter.package_dir_name }}` module.
"""

import unittest

import {{ cookiecutter.package_dir_name }}


class Test{{ cookiecutter.package_dir_name|capitalize }}(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert({{ cookiecutter.package_dir_name}}.__version__)

    def tearDown(self):
        pass
