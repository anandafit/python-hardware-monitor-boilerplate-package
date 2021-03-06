from monitor.event import DeviceMonitorEvent
from monitor.monitor_listener import MonitorListener

from monitor.operation import DeviceMonitorOperation

from monitor.monitor import device_monitor
my_device_monitor = device_monitor()
'''
WhoAsk need would be Pulse client
'''
class WhoAsk( MonitorListener ):
    """
    First class which ask who is listening to it
    """
    def __init__(self):
        self._device_monitor = my_device_monitor
        self._device_monitor.add_event_listener(self)
        
    def monitor_via_specialist_one(self):
        my_operation = DeviceMonitorOperation("specialist_one", "monitor_via_specialist_one")
        self._device_monitor.dispatch_operation(self, my_operation)

    def monitor_via_specialist_two(self):
        my_operation = DeviceMonitorOperation("specialist_two", "monitor_via_specialist_two")
        self._device_monitor.dispatch_operation(self, my_operation)    
   
    def on_answer_event(self, event):
        """
        Event handler for the RESPOND event type
        """
        operation = event.data
        print("<<< Thank you instance {0}".format( operation.data ))


class WhoAsk2( MonitorListener ):
    """
    First class which ask who is listening to it
    """
    def __init__(self):
        self._device_monitor = my_device_monitor
        self._device_monitor.add_event_listener(self)

    def monitor_via_specialist_one(self):
        my_operation = DeviceMonitorOperation("specialist_one", "monitor_via_specialist_one1")
        self._device_monitor.dispatch_operation(self, my_operation)

    def monitor_via_specialist_two(self):
        my_operation = DeviceMonitorOperation("specialist_two", "monitor_via_specialist_two2")
        self._device_monitor.dispatch_operation(self, my_operation)    
           
   
    def on_answer_event(self, event):
        """
        Event handler for the RESPOND event type
        """
        operation = event.data
        print("<<< Thank you instance 2 {0}".format( operation.data ))        
      