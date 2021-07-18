from pythonping import ping
from time import sleep
from data_Handling import save, load

#   TODO
#   Make better with Tkinter

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
            ping(address.get_Ip_Address(), verbose=True)
            sleep(3)

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

    while choice != 7:
        print("1 - Add IP to list")
        print("2 - Ping List")
        print("3 - show List")
        print("4 - save List")
        print("5 - load List")
        print("6 - Clear list")
        print("7 - Quit")
        choice = int(input(">"))

        if choice == 1:
            input_Ip_Address()
        elif choice == 2:
            IpAddress.ping_IP()
        elif choice == 3:
            IpAddress.print_List()
        elif choice == 4:
            save(address_List)
        elif choice == 5:
            update_List()
        elif choice == 6:
            IpAddress.clear_List()
        elif choice == 7:
            exit()
        else:
            print("Invalid choice...")


def main():
    menuGui()


if __name__ == '__main__':
    main()
