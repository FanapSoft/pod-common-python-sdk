# coding=utf-8
from pod_base import APIException, PodException
from datetime import datetime

from pod_common import PodCommon
from examples.config import *


try:
    pod_common = PodCommon(API_TOKEN, server_type=SERVER_MODE)

    category_name = "Category {0}".format(datetime.now().__format__("%Y_%m_%d_%H_%M_%S"))
    category = pod_common.add_tag_tree_category(category_name, "Create category with Python")
    print("New Tag Tree Category :\n", category)
    # OUTPUT
    # New Tag Tree Category :
    #  {'id': 1749, 'name': 'Category 2019_12_24_17_27_15', 'description': 'Create category with Python', ...}
    #
    category_name = "Updated " + category_name
    updated = pod_common.update_tag_tree_category(category_id=category['id'], name=category_name,
                                                  desc=category['description'], enable=True)
    print("Updated Tag Tree Category :\n", updated)
    # OUTPUT
    # Updated Tag Tree Category :
    #  {'id': 1753, 'name': 'Updated Category 2019_12_24_17_30_15', 'description': 'Create category with Python', ...}

    categories = pod_common.get_tag_tree_category_list()
    print(categories)
    print("Total Category : ", pod_common.total_items())
    # OUTPUT
    # [{'id': 421, 'name': 'hi', 'description': 'توضیحات دسته بندی کلی', ... },
    # {'id': 441, 'name': 'محصولات دیجیتال', ... },
    # {'id': 442, 'name': 'دسته بندی کلی15', ...}
    # ... ]
    # Total Category :  326

except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e)
