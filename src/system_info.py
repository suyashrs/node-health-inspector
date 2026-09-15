import socket
import platform 

class SystemInfoCollector:
        
    def __init__(self):
        pass

    def get_hostname(self):
        return socket.gethostname()
        

    def get_operating_system(self):
        return platform.system()
        pass

    def get_os_version(self):
        if (self.get_operating_system() == 'Darwin'):
            ver = platform.mac_ver()
            release, ver_info, machine = ver
            return release
        else:
            return None

    def get_cpu_architecture(self):
        pass

    def get_total_memory(self):
        pass

    def get_disk_capacity(self):
        pass

    def get_uptime(self):
        pass

    def get_local_ip(self):
        pass

