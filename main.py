import wmi
from time import sleep

w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
rawSensors = w.Sensor()

sensors = {'Voltage': {},
           'Clock': {},
           'Temperature': {},
           'Load': {},
           'Fan': {},
           'Flow': {},
           'Control': {},
           'Level': {},
           'Data': {},
           'Power': {}}
index = 0

for sensor in rawSensors:
    sensors[sensor.SensorType][sensor.Name] = sensor
    index += 1

print(sensors['Temperature']['CPU Package'])
