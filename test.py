from pythonping import ping
from time import sleep

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


def menuGui():
    choice = 0

    print("Hello, what would you like to do?")

    while choice != 5:
        print("1 - Add IP to list")
        print("2 - Clear list")
        print("3 - Ping List")
        print("4 - show List")
        print("5 - Quit")
        choice = int(input(">"))

        if choice == 1:
            input_Ip_Address()
        elif choice == 2:
            IpAddress.clear_List()
        elif choice == 3:
            IpAddress.ping_IP()
        elif choice == 4:
            IpAddress.print_List()
        elif choice == 5:
            exit()
        else:
            print("Invalid choice...")


def main():
    menuGui()


if __name__ == '__main__':
    main()
