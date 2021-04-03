from time import sleep

import psutil
import serial

from Data import Data


def main():
    psutil.cpu_percent(percpu=True)

    # temp = psutil.sensors_temperatures()
    # temp = temp["coretemp"][0][1]

    # print(temp)

    for i in range(5):
        cpuUsage = psutil.cpu_percent(percpu=True)
        arduinoData = Data(cpuTemp=psutil.sensors_temperatures()["coretemp"][0][1],
                           cpuUsage=[int(x) for x in cpuUsage],
                           cpuTotal=psutil.cpu_percent(),
                           gpuTemp=psutil.sensors_temperatures()["amdgpu"][0][1])

        serialized = arduinoData.serialize()

        print(serialized)
        sleep(0.5)


    # port = findSerialPort()

    # try:
    #     ser = serial.Serial(port=port, baudrate=9600)
    #     sleep(5)
    #     print(arduinoData.serialize())
    #     ser.write(arduinoData.serialize())
    #     ser.close()
    # except:
    #     print('Something went wrong while writing to the serial port')


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


def getSystemInfo():
    result = ""

    result += "cc" + psutil.cpu_count(logical=False) + "\n"
    result += "mt" + psutil.virtual_memory().total / 1000000 + "\n"

    return result


if __name__ == '__main__':
    main()
