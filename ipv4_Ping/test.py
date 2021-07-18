from pythonping import ping
from time import sleep
from data_Handling import save, load

# Lists
response_List = []
failed_List = []
address_List = []
ping_List = []
outputList = []


# Class for IP addresses
class IpAddress:
    def __init__(self, ip_Address):
        self.__ip_Address = ip_Address

        # Ip Address setter method
    def set_Ip_Address(self, ip_Address):
        self.__ip_Address = ip_Address

        # Ip address getter method
    def get_Ip_Address(self):
        return self.__ip_Address

    # Ping IP
    @staticmethod
    def ping_IP():
        for address in ping_List:
            try:
                response = ping(address.get_Ip_Address(), verbose=True)
                response_List.append(response)
                ping_List.remove(address)
                sleep(3)
            except:
                print("Unable to ping: ", address.get_Ip_Address())
                failed_List.append(address)
                ping_List.remove(address)
                print("\nRemoved address, continuing...\n")
                sleep(1)
                IpAddress.ping_IP()

    # Add a new Ip to the list
    @staticmethod
    def create_Object(ip_Address):
        new_Object = IpAddress(ip_Address)
        address_List.append(new_Object)
        print("Done\n")

    # Print a list of IP's in list
    @staticmethod
    def print_List():
        for address in address_List:
            print(address.get_Ip_Address(), '\n')
        print("Done\n")

    @staticmethod
    def clear_List():
        for address in address_List:
            address_List.remove(address)
        print("Done\n")

    @staticmethod
    def show_Failed():
        print("Addresses failed: ")
        for address in failed_List:
            print(address.get_Ip_Address())
        print("Done\n")


def input_Ip_Address():
    address = input("Please enter an IPV4 Address")
    IpAddress.create_Object(address)
    choice = input("Would you like to add another? y/n")

    if choice.lower() == 'y':
        input_Ip_Address()
    elif choice.lower() == 'n':
        return
    else:
        while choice != 'y' or choice != 'n':
            choice = input("Invalid option please try again")
        else:
            if choice.lower() == 'y':
                input_Ip_Address()
            elif choice.lower() == 'n':
                return


def iterate_List(List):
    for item in List:
        print(item)


def update_List():
    global address_List
    address_List = load()
    print("Done\n")


def menuGui():
    choice = 0

    print("Hello, what would you like to do?")
    print("Add IP to list - Ping List - show List - Clear list\n - save List - load List\n - Help - "
          "Quit")

    while choice != 'quit':
        choice = input(">")

        if choice == 'add':
            input_Ip_Address()
        elif choice == 'ping':
            for item in address_List:
                ping_List.append(item)
            IpAddress.ping_IP()
            print("Ping Done\n")
            IpAddress.show_Failed()
        elif choice == 'show':
            IpAddress.print_List()
            iterate_List(response_List)
        elif choice == 'save':
            save(address_List)
        elif choice == 'load':
            update_List()
        elif choice == 'clear':
            IpAddress.clear_List()
        elif choice == 'quit':
            exit()
        elif choice == 'help':
            print("- Add IP to list: 'add'")
            print("- Ping List: 'ping'")
            print("- show List: 'show'")
            print("- save List: 'save'")
            print("- load List: 'load'")
            print("- Clear list: 'clear'")
            print("- Quit: 'quit'")
        else:
            print("Invalid choice...")


def main():
    menuGui()


if __name__ == '__main__':
    main()
