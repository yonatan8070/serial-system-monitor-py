import wmi
from time import sleep

w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
sensors = w.Sensor()
# for sensor in temperature_infos:
#     if sensor.SensorType == u'Temperature':
#         print(sensor.Value)

for sensor in sensors:
    print(sensor)
