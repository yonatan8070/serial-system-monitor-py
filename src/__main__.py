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

    for data in temps.values():
        print(data)

    arduinoData = Data(cpuTemp=temps['CPU Package'].Value,
                       cpuUsage=usage['CPU Total'].Value,
                       gpuTemp=temps['GPU Core'].Value,
                       gpuUsage=usage['GPU Core'].Value)

    port = findSerialPort()

    try:
        ser = serial.Serial(port=port, baudrate=9600)
        sleep(5)
        print(arduinoData.serialize())
        ser.write(arduinoData.serialize())
        ser.close()
    except:
        print('Something went wrong while writing to the serial port')

def findSerialPort():
    ports = ['COM%s' % (i + 1) for i in range(256)]

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass

    return result[0]

if __name__ == '__main__':
    main()
