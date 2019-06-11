from pyobjus import autoclass, protocol
from pyobjus.dylib_manager import load_framework
from plyer.facades import GPS
from kivy.properties import StringProperty

from kivy.lang import Builder
from plyer import gps
from kivy.app import App
from kivy.properties import StringProperty
from kivy.clock import Clock, mainthread
load_framework('/System/Library/Frameworks/CoreLocation.framework')
CLLocationManager = autoclass('CLLocationManager')



def build(self):
    try:
        gps.configure(on_location=self.on_location,
                      on_status=self.on_status)
    except NotImplementedError:
        import traceback
        traceback.print_exc()
        self.gps_status = 'GPS is not implemented for your platform'
    return on_location
x = build(self)
print(x)
