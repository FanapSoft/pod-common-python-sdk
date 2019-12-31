# coding=utf-8
from pod_base import APIException, PodException
from pod_common import PodCommon
from examples.config import *

try:
    pod_common = PodCommon(API_TOKEN, server_type=SERVER_MODE)
    print("Guilds :", pod_common.guild_list())
    print("Total Guilds :", pod_common.total_items())
    # OUTPUT
    # Guilds : [{'id': 44, 'name': 'آرایش و زیبایی', 'code': 'TOILETRIES_GUILD'},
    # {'id': 45, 'name': 'بهداشت و درمان', 'code': 'HEALTH_GUILD'},
    # {'id': 46, 'name': 'آموزش و پژوهش', 'code': 'EDUCATION_GUILD'},
    # {'id': 47, 'name': 'فناوری اطلاعات', 'code': 'INFORMATION_TECHNOLOGY_GUILD'}, ...]
    # Total Guilds : 93

    print("Get Page 3 and Size 20")
    print("Guilds :", pod_common.guild_list(page=3, size=20))
    print("Total Guilds :", pod_common.total_items())
    # OUTPUT
    # Get Page 3 and Size 20
    # Guilds : [{'id': 682, 'name': 'گل و گیاه', 'code': 'FLOWER_GUILD'},
    # {'id': 721, 'name': 'سایر', 'code': 'OTHER_GUILD'},
    # {'id': 881, 'name': 'سوپرمارکت و خواروبارفروشی', 'code': 'SUPERMARKET_GUILD'},
    # {'id': 1041, 'name': 'حساب 001', 'code': 'DIMENSION_001'}, ...]
    # Total Guilds : 93

    print("********************************************")
    print("Search آرایش")
    print("Guilds :", pod_common.guild_list(name="آرایش"))
    # OUTPUT
    # Search آرایش
    # Guilds : [{'id': 44, 'name': 'آرایش و زیبایی', 'code': 'TOILETRIES_GUILD'}]
except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e)
