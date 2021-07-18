from pythonping import ping
from time import sleep
from data_Handling import save, load

#   TODO
#   Make better with Tkinter

failed_List = []
address_List = []
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
        for address in address_List:
            try:
                ping(address.get_Ip_Address(), verbose=True)
                sleep(3)
            except:
                print("Unable to ping: ", address.get_Ip_Address())
                failed_List.append(address)
                address_List.remove(address)
                print("\nRemoved address, trying list again...\n")
                sleep(1)
                IpAddress.ping_IP()

    # Add a new Ip to the list
    @staticmethod
    def create_Object(ip_Address):
        new_Object = IpAddress(ip_Address)
        address_List.append(new_Object)

    # Print a list of IP's in list
    @staticmethod
    def print_List():
        for address in address_List:
            print(address.get_Ip_Address(), '\n')

    @staticmethod
    def clear_List():
        for address in address_List:
            address_List.remove(address)


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


def update_List():
    global address_List
    address_List = load()


def menuGui():
    choice = 0

    print("Hello, what would you like to do?")
    print("Add IP to list - Ping List - show List - Clear list\n - save List - load List\n - Help - Quit")

    while choice != 'quit':
        choice = input(">")

        if choice == 'add':
            input_Ip_Address()
        elif choice == 'ping':
            IpAddress.ping_IP()
            print("Ping Done\n")
            print("Addresses failed: ")
            for address in failed_List:
                print(address.get_Ip_Address())
        elif choice == 'show':
            IpAddress.print_List()
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
