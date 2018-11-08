# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from RtMonSys.models import models_common


def get_all_models():
    models = models_common.get_config('BDP')
    # test_list = []
    # qw_list = []
    # jp_list = []
    # cn_list = []
    # for item in models:
    #     if(item["MODEL"] == "QW"):
    #         qw_list = item["CASE"]
    #     if (item["MODEL"] == "JP"):
    #         jp_list = item["CASE"]
    #     if (item["MODEL"] == "CN"):
    #         cn_list = item["CASE"]
    return models


