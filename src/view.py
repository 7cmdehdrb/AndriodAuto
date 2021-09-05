#! /usr/bin/env python
"""
Copyright (C) 2012  Diego Torres Milano
Created on Feb 3, 2012
  
@author: diego
"""


import sys
import os

try:
    sys.path.insert(0, os.path.join(os.environ["ANDROID_VIEW_CLIENT_HOME"], "src"))
except:
    pass

from com.dtmilano.android.viewclient import ViewClient

vc = ViewClient(*ViewClient.connectToDeviceOrExit())

vc.traverse()

vc.findViewById(
    "android.widget.LinearLayout com.kakao.talk:id/ii_message_edit_text"
).touch()
