# -*- coding: utf-8 -*-
# Copyright 2009-2010
# Santhosh Thottingal <santhosh.thottingal@gmail.com>
# This code is part of Silpa project.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import os
class SilpaModule:
    def __init__(self):
        self.template=None
        self.request=None
    def get_errormessage(self):
        return None
    def get_successmessage(self):
        return None
    def get_module_name(self):
        return "Untitled Silpa Module"
    def get_info(self):
        return     "Module description"
    def process(self,object):
        return     "Not Implemented"
    def get_form(self,templatefile='template.html'):
        return open(self.template,'r').read()
    def set_request(self,request):
        self.request=request
    
    def set_start_response(self,start_response):
        """
        TODO Add the implementaion here
        """
        return    
    def get_json_result(self):
        return ""
    def is_self_serve(self) :       
        return False
    def get_mimetype(self):
        return "text/html"
        
def ServiceMethod(fn):
    fn.IsServiceMethod = True
    return fn
