from src.system_info import SystemInfoCollector

def main():
    collector = SystemInfoCollector()

    print("Node Health Inspector")
    print("---------------------")
    print(collector)
    print(collector.get_hostname())
    print(collector.get_operating_system())
    print(collector.get_os_version())


if __name__ == "__main__":
    main()
