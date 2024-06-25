
import json
import sys
import os
from datetime import datetime

# Global variables
json_file = 'structure.json'
current_directory = os.getcwd()

# Load directory structure from JSON file
def load_directory_structure():
    with open(json_file, 'r') as f:
        return json.load(f)

# Format timestamp to specified format
def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%b %d %H:%M')

# Convert size to human readable format
def human_readable_size(size):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f"{size:.1f}{units[index]}"

# Print file details
def print_file_details(file, human_readable):
    formatted_time = format_time(file['time_modified'])
    size = human_readable_size(file['size']) if human_readable else file['size']
    print(f"{file['permissions']} {size} {formatted_time} {file['name']}")

# Print the directory listing
def print_ls(directory, show_all=False, vertical=False, reverse=False, sort_by_time=False, filter_option=None, human_readable=False):
    if 'contents' not in directory:
        print_file_details(directory, human_readable)
        return
    
    contents = directory['contents']
    
    # Filter hidden files
    if not show_all:
        contents = [item for item in contents if not item['name'].startswith('.')]

    # Apply file/directory filter if specified
    if filter_option:
        if filter_option == 'file':
            contents = [item for item in contents if not item['permissions'].startswith('d')]
        elif filter_option == 'dir':
            contents = [item for item in contents if item['permissions'].startswith('d')]
        else:
            print(f"error: '{filter_option}' is not a valid filter criteria. Available filters are 'dir' and 'file'")
            return

    # Sort by time if specified
    if sort_by_time:
        contents = sorted(contents, key=lambda x: x['time_modified'])

    # Reverse order if specified
    if reverse:
        contents.reverse()

    # Print in long format if specified
    if vertical:
        for item in contents:
            print_file_details(item, human_readable)
    else:
        for item in contents:
            print(item['name'])

# Show help message
def print_help():
    print("Usage: python -m pyls [OPTIONS] [PATH]")
    print("Options:")
    print("  -A               show all files")
    print("  -l               use a long listing format")
    print("  -r               reverse order")
    print("  -t               sort by time modified")
    print("  -h               display sizes in human readable format")
    print("  --filter=TYPE    filter by 'dir' or 'file'")
    print("  --help           display this help and exit")

# Main function
def main():
    global json_file

    # Check if a specific path is provided
    if len(sys.argv) > 1 and not sys.argv[1].startswith('-'):
        path = sys.argv[1]
        
        # Construct full path
        json_file = os.path.join(current_directory, path)
        
        # Check if the path exists
        if not os.path.exists(json_file):
            print(f"error: cannot access '{path}': No such file or directory")
            sys.exit(1)

    directory = load_directory_structure()

    # Handle the case where a path is specified after options
    if len(sys.argv) > 2 and not sys.argv[2].startswith('-'):
        path = sys.argv[2]

        # Split the path to handle relative paths correctly
        if path.startswith('./'):
            path = path[2:]
        elif path == '.':
            path = ''
        
        # Traverse the directory structure to find the requested path
        path_parts = path.split('/')
        for part in path_parts[:-1]:  # Traverse until the parent directory
            found = False
            for item in directory['contents']:
                if item['name'] == part and item['permissions'].startswith('d'):
                    directory = item
                    found = True
                    break
            if not found:
                print(f"error: cannot access '{sys.argv[2]}': No such file or directory")
                sys.exit(1)
        
        # Check if the last part is a file or directory
        target_name = path_parts[-1]
        found = False
        for item in directory['contents']:
            if item['name'] == target_name:
                directory = item
                found = True
                break
        if not found:
            print(f"error: cannot access '{sys.argv[2]}': No such file or directory")
            sys.exit(1)

    # Process options
    show_all = '-A' in sys.argv
    vertical = '-l' in sys.argv
    reverse = '-r' in sys.argv
    sort_by_time = '-t' in sys.argv
    human_readable = '-h' in sys.argv

    filter_option = None
    for arg in sys.argv:
        if arg.startswith('--filter='):
            filter_option = arg.split('=')[1]
            break

    print_ls(directory, show_all, vertical, reverse, sort_by_time, filter_option, human_readable)

if __name__ == "__main__":
    if '--help' in sys.argv:
        print_help()
    else:
        main()
