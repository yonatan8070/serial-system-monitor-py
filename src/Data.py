class Data:
    cpuTemp: int
    cpuUsage: list
    cpuTotal: int
    gpuTemp: int

    def __init__(self,
                 cpuTemp,
                 cpuUsage,
                 cpuTotal,
                 gpuTemp):
        self.cpuTemp = cpuTemp
        self.cpuUsage = cpuUsage
        self.cpuTotal = cpuTotal
        self.gpuTemp = gpuTemp

    def serialize(self):
        result  = b'ct ' + str(int(self.cpuTemp)).encode() + b'\n'   # ct represents CPU temperature
        result += b'cu ' + str(self.cpuTotal).encode() + b'\n'
        result += b'cc '  # cc represents per core CPU usage
        for i in self.cpuUsage:
            result += str(int(i)).encode() + b" "

        result += b'gt ' + str(int(self.gpuTemp)).encode() + b'\n'   # gt represents GPU temperature

        return result
