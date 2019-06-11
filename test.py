from pyobjus import autoclass, protocol
from plyer import gps
class GPS(object):
    '''
    GPS facade.
    '''

    def configure(self, on_location, on_status=None):
        '''
        Configure the GPS object. This method should be called before
        :meth:`start`.
        :param on_location: Function to call when receiving a new location
        :param on_status: Function to call when a status message is received
        :type on_location: callable, multiples keys/value will be passed.
        :type on_status: callable, args are "message-type", "status"
        .. warning::
            The `on_location` and `on_status` callables might be called from
            another thread than the thread used for creating the GPS object.
        '''
        self.on_location = on_location
        self.on_status = on_status
        self._configure()

    def start(self, minTime=1000, minDistance=1):
        '''
        Start the GPS location updates.
        Expects 2 parameters:
            minTime: milliseconds.  (float)
            minDistance: meters. (float)
        '''
        self._start(minTime=minTime, minDistance=minDistance)

    def stop(self):
        '''
        Stop the GPS location updates.
        '''
        self._stop()

    # private

    def _configure(self):
        raise NotImplementedError()

    def _start(self, **kwargs):
        raise NotImplementedError()

    def _stop(self):
        raise NotImplementedError()

GPS.configure(self, on_location, on_status=None)
