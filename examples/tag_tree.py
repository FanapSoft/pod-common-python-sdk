# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from datetime import datetime
from pod_common import PodCommon
from examples.config import *

try:
    pod_common = PodCommon(API_TOKEN, server_type=SERVER_MODE)

    categories = pod_common.get_tag_tree_category_list()
    if len(categories) == 0:
        print("Please Create new Tag Tree Category")
        exit()

    category_id = categories[0]["id"]
    tag_name = "Tag {0}".format(datetime.now().__format__("%Y_%m_%d_%H_%M_%S"))
    code = tag_name.replace(" ", "_")
    tag = pod_common.add_tag_tree(name=tag_name, category_id=category_id, code=code)
    print("New Tag :\n", tag)
    # OUTPUT
    # New Tag :
    #  {'id': 3268, 'name': 'Tag 2019_12_24_17_39_16', 'level': 0, 'category': {'id': 421, 'name': 'hi', ...}

    updated_tag_name = "Updated {0}".format(tag_name)

    updated = pod_common.update_tag_tree(tag["id"], name=updated_tag_name, parent_id=0, enable=False)
    print("Updated Tag :\n", updated)
    # OUTPUT
    # Updated Tag :
    #  {'id': 3268, 'name': 'Updated Tag 2019_12_24_17_39_16', 'level': 0, 'category': {'id': 421, 'name': 'hi', ...}

    tags = pod_common.get_tag_tree_list(category_id=category_id)
    print("Tags:\n", tags)
    print("Total Tags : ", pod_common.total_items())
    # OUTPUT
    # Tags:
    #  [{'id': 1101, 'name': 'تگ اول', 'code': '1101', 'level': 0, 'category': {'id': 421, 'name': 'hi', ... },
    #  {'id': 3270, 'name': 'Updated Tag 2019_12_24_17_39_44', 'code': '3270', 'level': 0, 'category': { ... },
    #  {'id': 3269, 'name': 'Updated Tag 2019_12_24_17_39_16', 'code': '3269', 'level': 0, 'category': { ...}]
    # Total Tags :  11

    get_tag_by_id = pod_common.get_tag_tree(tag["id"])
    print("Get Tag By Id:\n", get_tag_by_id)
    # OUTPUT
    # Get Tag By Id:
    #  {'id': 3268, 'name': 'Updated Tag 2019_12_24_17_39_16', 'level': 0, 'category': {'id': 421, 'name': 'hi', ...}
except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e)
