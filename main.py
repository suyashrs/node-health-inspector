from src.system_info import SystemInfoCollector

def main():
    collector = SystemInfoCollector()

    print("Node Health Inspector")
    print("---------------------")
    print(collector)

if __name__ == "__main__":
    main()
