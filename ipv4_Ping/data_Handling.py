import pickle


# Save list
def save(List):
    FILE_NAME = input("Please enter file name: ")
    again = True
    output_file = open(FILE_NAME, 'wb')

    while again:
        pickle.dump(List, output_file)
        again = False

    output_file.close()
    print("Data was written to ", FILE_NAME)


# Load file
def load():
    FILE_NAME = input("Please enter file name: ")
    end_of_file = False
    List = None
    input_file = open(FILE_NAME, 'rb')

    while not end_of_file:
        try:
            List = pickle.load(input_file)
        except EOFError:
            end_of_file = True

    input_file.close()
    return List
