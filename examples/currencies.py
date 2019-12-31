# coding=utf-8
from pod_base import APIException, PodException

from pod_common import PodCommon
from examples.config import *


try:
    pod_common = PodCommon(API_TOKEN, server_type=SERVER_MODE)
    print(pod_common.currency_list())

    # OUTPUT
    # [{'name': 'فرانک سويس', 'code': 'CHF'}, {'name': 'ريال قطر', 'code': 'QAR'}, ...]
except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
