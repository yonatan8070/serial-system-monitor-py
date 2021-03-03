import wmi
from time import sleep
def main():
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
            'Power': {},
            'SmallData': {}}
    index = 0

    for sensor in rawSensors:
        sensors[sensor.SensorType][sensor.Name] = sensor
        index += 1

    del index

    temps = sensors['Temperature']
    usage = sensors['Load']

    for data in temps.values():
        print(data)

if __name__ == '__main__':
    main()
