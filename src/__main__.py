from time import sleep
from Data import Data
import wmi
import serial


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

    temps = sensors['Temperature']
    usage = sensors['Load']

    # for data in temps.values():
    #     print(data)

    arduinoData = Data(cpuTemp=temps['CPU Package'].Value,
                       cpuUsage=usage['CPU Total'].Value,
                       gpuTemp=temps['GPU Core'].Value,
                       gpuUsage=usage['GPU Core'].Value)

    print(arduinoData.serialize())

    ser = serial.Serial(port='COM1', baudrate=115200)

if __name__ == '__main__':
    main()
