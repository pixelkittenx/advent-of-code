import argparse


def main(argv=None):
    # Parse file name from args
    file_name = get_file_name(argv)

    #read in the input from the file
    with open(file_name, 'r') as txt_file:
        data = txt_file.read()

    chars = []

    # For Part 1
    #packet_length = 4
    
    # For Part 2
    packet_length = 14
    for i, char in enumerate(data):
        if len(chars) < packet_length:
            chars.append(char)
        
        if len(chars) == packet_length:
            if len(chars) == len(set(chars)):
                start_of_packet = i + 1
                break
            else:
                chars.pop(0)

    print(f'Start of packet {start_of_packet}')
    return 0

def get_file_name(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Input file name")
    args = parser.parse_args(argv)
    return args.filename



if __name__ == "__main__":
    main()