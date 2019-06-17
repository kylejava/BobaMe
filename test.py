
from plyer import gps
class gps():
    def build(self):

        gps.configure(on_location=self.on_location,
                    on_status=self.on_status)

    def start(self, minTime, minDistance):
        gps.start(minTime, minDistance)

    def stop(self):
        gps.stop()


    def on_location(self, **kwargs):
        print kwargs
        self.gps_location = '\n'.join(['{}={}'.format(k, v) for k, v in kwargs.items()])
        print self.gps_location


    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)

    def on_pause(self):
        gps.stop()
        return True

    def on_resume(self):
        gps.start(1000, 0)
        pass
    def show(self):
        gps_location= self.gps_location
        print(gps_location)


def get_loc():
    x = gps()
    x.on_location()
