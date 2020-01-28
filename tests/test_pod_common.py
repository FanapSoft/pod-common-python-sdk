# coding=utf-8
from __future__ import unicode_literals

import unittest

from pod_base import InvalidDataException

from pod_common import PodCommon
from datetime import datetime
from tests.config import *


class TestPodVoucher(unittest.TestCase):
    __slots__ = "__common"

    def setUp(self):
        self.__common = PodCommon(api_token=API_TOKEN, server_type=SERVER_MODE)

    def test_01_get_ott(self):
        result = self.__common.get_ott()
        self.assertIsInstance(result, str)

    def test_02_currency_list(self):
        result = self.__common.currency_list()
        self.assertIsInstance(result, list, msg="currency list : check instance")

    def test_03_guild_list(self):
        result = self.__common.guild_list()
        self.assertIsInstance(result, list, msg="guild list : check instance")

    def test_03_guild_list_name(self):
        result = self.__common.guild_list(name="آرایش")
        self.assertIsInstance(result, list, msg="guild list : check instance")

    def test_04_add_tag_tree_category(self):
        category_name = "Category {0}".format(datetime.now().__format__("%Y_%m_%d_%H_%M_%S"))
        result = self.__common.add_tag_tree_category(name=category_name)
        self.assertIsInstance(result, dict, msg="add tag tree category : check instance")
        self.assertEqual(result["name"], category_name, msg="add tag tree category : check name")

    def test_04_add_tag_tree_category_all_params(self):
        category_name = "Category {0}".format(datetime.now().__format__("%Y_%m_%d_%H_%M_%S"))
        result = self.__common.add_tag_tree_category(name=category_name, desc="this is a test")
        self.assertIsInstance(result, dict, msg="add tag tree category (all params) : check instance")
        self.assertEqual(result["name"], category_name, msg="add tag tree category (all params) : check name")

    def test_04_add_tag_tree_category_required_params(self):
        with self.assertRaises(TypeError, msg="add tag tree category : required param"):
            self.__common.add_tag_tree_category()

    def test_04_add_tag_tree_category_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="add tag tree category : validation error"):
            self.__common.add_tag_tree_category(name="")

    def __add_tag_tree_category(self):
        category_name = "Category {0}".format(datetime.now().__format__("%Y_%m_%d_%H_%M_%S"))
        return self.__common.add_tag_tree_category(name=category_name, desc="this is a test")

    def test_05_update_tag_tree_category(self):
        category = self.__add_tag_tree_category()
        category_name = "Update Category {0}".format(datetime.now().__format__("%Y_%m_%d_%H_%M_%S"))
        desc = "Updated description"
        result = self.__common.update_tag_tree_category(category_id=category["id"], name=category_name, desc=desc,
                                                        enable=False)
        self.assertIsInstance(result, dict, msg="update tag tree category : check instance")
        self.assertEqual(result["name"], category_name, msg="update tag tree category : check name")
        self.assertEqual(result["description"], desc, msg="update tag tree category : check description")
        self.assertEqual(result["enable"], False, msg="update tag tree category : check status")

    def test_05_update_tag_tree_category_validation_error(self):
        category_name = ""
        desc = "Updated description"
        with self.assertRaises(InvalidDataException, msg="update tag tree category : validation error"):
            self.__common.update_tag_tree_category(category_id="123", name=category_name, desc=desc, enable="False")

    def test_05_update_tag_tree_category_required_param(self):
        with self.assertRaises(TypeError, msg="update tag tree category : required params"):
            self.__common.update_tag_tree_category()

    def test_06_get_tag_tree_category_list(self):
        result = self.__common.get_tag_tree_category_list()
        self.assertIsInstance(result, list, msg="get tag tree category list : check instance")

    def test_06_get_tag_tree_category_list_validation_error(self):
        params = {"id": "123"}
        with self.assertRaises(InvalidDataException, msg="get tag tree category list : validation error"):
            self.__common.get_tag_tree_category_list(params=params)

    def test_07_add_tag_tree(self):
        category_name = "Tag {0}".format(datetime.now().__format__("%Y_%m_%d_%H_%M_%S"))
        category = self.__add_tag_tree_category()
        code = "code_{}".format(datetime.now().__format__("%Y%m%d%H%M%S"))
        result = self.__common.add_tag_tree(name=category_name, code=code, category_id=category["id"], parent_id=0)
        self.assertIsInstance(result, dict, msg="add tag tree : check instance")
        self.assertEqual(result["name"], category_name, msg="add tag tree : check name")
        self.assertEqual(result["category"]["id"], category["id"], msg="add tag tree : check category id")
        self.assertEqual(result["code"], code, msg="add tag tree : check code")

    def test_07_add_tag_tree_required_params(self):
        with self.assertRaises(TypeError, msg="add tag tree : required param"):
            self.__common.add_tag_tree()

    def test_07_add_tag_tree_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="add tag tree : validation error"):
            self.__common.add_tag_tree(name="", code="", category_id="123", parent_id=0)

    def __add_tag_tree(self):
        category_name = "Tag {0}".format(datetime.now().__format__("%Y_%m_%d_%H_%M_%S"))
        category = self.__add_tag_tree_category()
        code = "code_{}".format(datetime.now().__format__("%Y%m%d%H%M%S"))
        return self.__common.add_tag_tree(name=category_name, code=code, category_id=category["id"], parent_id=0)

    def test_08_update_tag_tree_category(self):
        tag = self.__add_tag_tree()
        tag_name = "Update Tag {0}".format(datetime.now().__format__("%Y_%m_%d_%H_%M_%S"))
        result = self.__common.update_tag_tree(tag_tree_id=tag["id"], name=tag_name, enable=False)
        self.assertIsInstance(result, dict, msg="update tag tree : check instance")
        self.assertEqual(result["name"], tag_name, msg="update tag tree : check name")
        self.assertEqual(result["enable"], False, msg="update tag tree : check status")

    def test_08_update_tag_tree_validation_error(self):
        tag_name = ""
        with self.assertRaises(InvalidDataException, msg="update tag tree : validation error"):
            self.__common.update_tag_tree(tag_tree_id="123", name=tag_name, parent_id="0", enable="False")

    def test_08_update_tag_tree_required_param(self):
        with self.assertRaises(TypeError, msg="update tag tree : required params"):
            self.__common.update_tag_tree()

    def test_09_get_tag_tree_list(self):
        category_list = self.__common.get_tag_tree_category_list()
        if len(category_list):
            result = self.__common.get_tag_tree_list(category_id=category_list[0]["id"])
            self.assertIsInstance(result, list, msg="get tag tree list : check instance")

    def test_09_get_tag_tree_list_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="get tag tree list : validation error"):
            self.__common.get_tag_tree_list(category_id="123", level_count="2")
