#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
Views for Pyramid frontend
"""
from collections import OrderedDict
from pyramid.view import view_config

from ..common import get_settings_param


@view_config(route_name='sa_home', renderer='/sacrud/home.jinja2',
             permission='pyramid_sacrud_home')
def sa_home(request):
    tables = OrderedDict(get_settings_param(request, 'pyramid_sacrud.models'))
    dashboard_row_len = get_settings_param(request,
                                           'pyramid_sacrud.dashboard_row_len')
    return {'dashboard_row_len': dashboard_row_len or 3, 'tables': tables}
