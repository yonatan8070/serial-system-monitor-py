class Data:
    def __init__(self,
                 cpuTemp,
                 cpuUsage,
                 gpuTemp,
                 gpuUsage):
        self.cpuTemp = cpuTemp
        self.cpuUsage = cpuUsage
        self.gpuTemp = gpuTemp
        self.gpuUsage = gpuUsage

    def serialize(self):
        result  = b'ct ' + str(int(self.cpuTemp)).encode() + b'\n'   # ct represents CPU temperature
        # result += b'cu ' + str(int(self.cpuUsage)).encode() + b'\n'  # cu represents CPU usage
        result += b'gt ' + str(int(self.gpuTemp)).encode() + b'\n'   # gt represents GPU temperature
        # result += b'gu ' + str(int(self.gpuUsage)).encode() + b'\n'  # gu represents GPU usage

        return result
