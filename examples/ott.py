from pod_base import APIException, PodException

from pod_common import PodCommon
from examples.config import *


try:
    pod_common = PodCommon(API_TOKEN, server_type=SERVER_MODE)
    print("One Time Token :", pod_common.get_ott())

    # OUTPUT
    # One Time Token : d9b8d0b815925db
except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e)
