#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 10:30 PM
# @Author  : w8ay
# @File    : __init__.py.py
import copy

from lib.core.option import init
from lib.helper.function import isJavaObjectDeserialization, isPHPObjectDeserialization, isPythonObjectDeserialization
from lib.core.plugins import PluginBase
from lib.core.output import output, ResultObject
from lib.core.enums import WEB_PLATFORM, PLACE, HTTPMETHOD, VulType
from lib.core.data import conf, KB, path, logger
from lib.core.common import paramsCombination, generateResponse
from lib.parse.parse_request import FakeReq
from lib.parse.parse_responnse import FakeResp
from w13scan import modulePath
import requests

__all__ = [
    'isJavaObjectDeserialization', 'isPHPObjectDeserialization', 'isPythonObjectDeserialization',
    'PluginBase', 'output', 'ResultObject', 'WEB_PLATFORM', 'conf', 'KB',
    'path', 'logger', 'PLACE', 'HTTPMETHOD', 'paramsCombination', 'VulType', 'generateResponse'
]


def scan(url, module_name):
    root = modulePath()
    cmdline = {
        "level": 5
    }
    init(root, cmdline)
    r = requests.get(url)
    req = FakeReq(url, {}, HTTPMETHOD.GET)
    resp = FakeResp(r.status_code, r.content, r.headers)

    poc_module = copy.deepcopy(KB["registered"][module_name])
    poc_module.execute(req, resp)
