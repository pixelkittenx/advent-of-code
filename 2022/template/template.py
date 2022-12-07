import argparse


def main(argv=None):
    # Parse file name from args
    file_name = get_file_name(argv)

    # read in the input from the file
    with open(file_name, 'r') as txt_file:
        data = txt_file.read()


    return 0

def get_file_name(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Input file name")
    args = parser.parse_args(argv)
    return args.filename



if __name__ == "__main__":
    main()