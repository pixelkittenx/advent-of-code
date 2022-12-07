import argparse
import json

folder_sizes = {}

def main(argv=None):
    
    # Parse file name from args
    file_name = get_file_name(argv)

    # These probably don't need to be two separate steps, but I was worried I'd need the full file structure for Part 2

    # Build the file structure
    file_structure = build_file_structure(file_name)

    # Calculate the sizes
    calculate_folder_sizes(file_structure)

    # For Part 1
    max_size = 100000
    answer = sum([ v for k, v in folder_sizes.items() if v <= max_size])
    print(f'Part 1 - Answer: {answer}')

    # For Part 2
    answer = get_smallest_dir_to_delete(folder_sizes)
    print(f'Part 2 - Answer: {answer}')

    return 0

def build_file_structure(file_name):
    
    file_structure = {} # Dict to hold the file structure
    current_directory = None # Current directory
    current_path = [] # Use list to track path as easy to move backwards
    currently_listing = False # Tracks if currently iterating through a directory listing

    # vars for each of the commands
    cd_root = '$ cd /'
    cd_up = '$ cd ..'
    cd = '$ cd'
    ls = '$ ls'
    dir = 'dir'

    # read in the input from the file
    with open(file_name, 'r') as txt_file:
        data = txt_file.readlines()

    for line in data:
        line = line.strip()

        # Check if directory listing is complete
        if currently_listing and line.startswith('$'):
            currently_listing = False

        if not currently_listing:
            if line == cd_root:
                # Set the current directory to root of the dictionary
                current_directory = file_structure
                current_path = []
            elif line == cd_up:
                # remove current directory from the path
                current_path.pop()
                # set current directory up
                current_directory = get_dir(current_path, file_structure)
            elif cd in line:
                target_dir = line.split()[2]
                # this line might not be necessary...
                # if target_dir not in current_directory:
                #     current_directory[target_dir] = {}
                # move to the new dir
                current_directory = current_directory[target_dir]
                current_path.append(target_dir)
            elif line == ls:
                currently_listing = True
        else:
            x = line.split()[0]
            name = line.split()[1]
            
            if x == dir: # Current line is for a directory
                if name in current_directory:
                    raise (f'This dir already exists... {name}.')
                current_directory[name] = {}
            else: # Current line is for a file
                if name in current_directory:
                    raise (f'This file already exists... {name}.')
                current_directory[name] = int(x)

    return file_structure

def get_dir(current_path, file_structure):
    dir = file_structure
    for folder in current_path:
        dir = dir[folder]
    return dir

def calculate_folder_sizes(file_structure):

    get_folder_size(file_structure, 'root')
    return folder_sizes

def get_folder_size(item, current_path):
    # New folder, set to 0
    if current_path not in folder_sizes:
        folder_sizes[current_path] = 0

    for key, value in item.items():
        if isinstance(value, int):
            # Found a file, add to the total
            folder_sizes[current_path] += value
        else:
            # Found a folder - recursion time!
            # Folder names are NOT unique, need to keep full path
            folder_sizes[current_path] += get_folder_size(value, f'{current_path}.{key}')
    return folder_sizes[current_path]

def get_smallest_dir_to_delete(folder_totals):
    current_free_space = 70000000 - folder_totals['root']
    space_to_free_up = 30000000 - current_free_space

    current_smallest_dir = folder_totals['root']
    for key, value in folder_totals.items():
        if value > space_to_free_up and value < current_smallest_dir:
            current_smallest_dir = value
    return current_smallest_dir

def get_file_name(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Input file name")
    args = parser.parse_args(argv)
    return args.filename

if __name__ == "__main__":
    main()