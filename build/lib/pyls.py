# import json

# def load_directory_structure(json_file):
#     with open(json_file, 'r') as f:
#         return json.load(f)

# def print_ls(directory):
#     if 'contents' in directory:
#         for item in directory['contents']:
#             if not item['name'].startswith('.'):
#                 print(item['name'])

# def main():
#     json_file = 'structure.json'
#     directory_structure = load_directory_structure(json_file)
#     print_ls(directory_structure)

# if __name__ == "__main__":
#     main()

# import json
# import sys

# def load_directory_structure(json_file):
#     with open(json_file, 'r') as f:
#         return json.load(f)

# def print_ls(directory, show_all=False):
#     if 'contents' in directory:
#         for item in directory['contents']:
#             if show_all  or not item['name'].startswith('.'):
#                 print(item['name'])
            
# def main():
#     json_file = 'structure.json'
    
#     show_all = '-A' in sys.argv

#     directory_structure = load_directory_structure(json_file)
#     print_ls(directory_structure, show_all)

# if __name__ == "__main__":
#     main()

# import json
# import sys

# def load_directory_structure(json_file):
#     with open(json_file, 'r') as f:
#         return json.load(f)

# def print_ls(directory, show_all=False, vertical=False):
#     if 'contents' in directory:
#         for item in directory['contents']:
#             if show_all or not item['name'].startswith('.'):
#                 if vertical:
#                     #print(item[])
#                     print(f"{item['permissions']}, {item['size']}, {item['time_modified']},{item['name']} ")
#                 else:
#                     print(item['name'])

# def main():
#     json_file = 'structure.json'
    
#     show_all = '-A' in sys.argv
#     vertical = '-l' in sys.argv

#     directory_structure = load_directory_structure(json_file)
#     print_ls(directory_structure, show_all, vertical)

# if __name__ == "__main__":
#     main()

# import json
# import sys
# from datetime import datetime

# def load_directory_structure(json_file):
#     with open(json_file, 'r') as f:
#         return json.load(f)

# def format_time(timestamp):
#     return datetime.fromtimestamp(timestamp).strftime('%b %d %H:%M')

# def print_ls(directory, show_all=False, vertical=False):
#     if 'contents' in directory:
#         for item in directory['contents']:
#             if show_all or not item['name'].startswith('.'):
#                 if vertical:
#                     formatted_time = format_time(item['time_modified'])
#                     print(f"{item['permissions']} {item['size']} {formatted_time} {item['name']}")
#                 else:
#                     print(item['name'])

# def main():
#     json_file = 'structure.json'
    
#     show_all = '-A' in sys.argv
#     vertical = '-l' in sys.argv

#     directory_structure = load_directory_structure(json_file)
#     print_ls(directory_structure, show_all, vertical)

# if __name__ == "__main__":
#     main()

# import json
# import sys
# from datetime import datetime

# def load_directory_structure(json_file):
#     with open(json_file, 'r') as f:
#         return json.load(f)

# def format_time(timestamp):
#     return datetime.fromtimestamp(timestamp).strftime('%b %d %H:%M')

# def print_ls(directory, show_all=False, vertical=False, reverse=False):
#     if 'contents' in directory:
#         contents = directory['contents']
#         if reverse:
#             contents = contents[::-1]
#         for item in contents:
#             if show_all or not item['name'].startswith('.'):
#                 if vertical:
#                     formatted_time = format_time(item['time_modified'])
#                     print(f"{item['permissions']} {item['size']} {formatted_time} {item['name']}")
#                 else:
#                     print(item['name'])

# def main():
#     json_file = 'structure.json'
    
#     show_all = '-A' in sys.argv
#     vertical = '-l' in sys.argv
#     reverse = '-r' in sys.argv

#     directory_structure = load_directory_structure(json_file)
#     print_ls(directory_structure, show_all, vertical, reverse)

# if __name__ == "__main__":
#     main()




# import json
# import sys
# from datetime import datetime

# def load_directory_structure(json_file):
#     with open(json_file, 'r') as f:
#         return json.load(f)

# def format_time(timestamp):
#     return datetime.fromtimestamp(timestamp).strftime('%b %d %H:%M')

# def print_ls(directory, show_all=False, vertical=False, reverse=False):
#     if 'contents' in directory:
#         contents = directory['contents']
#         if reverse:
#             contents = reversed(contents)
#         for item in contents:
#             if show_all or not item['name'].startswith('.'):
#                 if vertical:
#                     formatted_time = format_time(item['time_modified'])
#                     print(f"{item['permissions']} {item['size']} {formatted_time} {item['name']}")
#                 elif reverse:
#                     formatted_time = format_time(item['time_modified'])
#                     print(f"{item['permissions']} {item['size']} {formatted_time} {item['name']}")
#                 else:
#                     print(item['name'])

# def main():
#     json_file = 'structure.json'
    
#     show_all = '-A' in sys.argv
#     vertical = '-l' in sys.argv
#     reverse = '-r' in sys.argv

#     directory_structure = load_directory_structure(json_file)
#     print_ls(directory_structure, show_all, vertical, reverse)

# if __name__ == "__main__":
#     main()

# import json
# import sys
# from datetime import datetime

# def load_directory_structure(json_file):
#     with open(json_file, 'r') as f:
#         return json.load(f)

# def format_time(timestamp):
#     return datetime.fromtimestamp(timestamp).strftime('%b %d %H:%M')

# def print_ls(directory, show_all=False, vertical=False, reverse=False, sort_by_time=False):
#     if 'contents' in directory:
#         contents = directory['contents']
#         if sort_by_time:
#             contents = sorted(contents, key=lambda x: x['time_modified'])
#         if reverse:
#             contents = list(reversed(contents))
#         for item in contents:
#             if show_all or not item['name'].startswith('.'):
#                 if vertical:
#                     formatted_time = format_time(item['time_modified'])
#                     print(f"{item['permissions']} {item['size']} {formatted_time} {item['name']}")
#                 else:
#                     print(item['name'])

# def main():
#     json_file = 'structure.json'
    
#     show_all = '-A' in sys.argv
#     vertical = '-l' in sys.argv
#     reverse = '-r' in sys.argv
#     sort_by_time = '-t' in sys.argv

#     directory_structure = load_directory_structure(json_file)
#     print_ls(directory_structure, show_all, vertical, reverse, sort_by_time)

# if __name__ == "__main__":
#     main()

# import json
# import sys
# from datetime import datetime

# def load_directory_structure(json_file):
#     with open(json_file, 'r') as f:
#         return json.load(f)

# def format_time(timestamp):
#     return datetime.fromtimestamp(timestamp).strftime('%b %d %H:%M')

# def print_ls(directory, show_all=False, vertical=False, reverse=False, sort_by_time=False, filter_option=None):
#     if 'contents' in directory:
#         contents = directory['contents']
        
#         if filter_option == 'file':
#             contents = [item for item in contents if not item['permissions'].startswith('d')]
#         elif filter_option == 'dir':
#             contents = [item for item in contents if item['permissions'].startswith('d')]
#         elif filter_option:
#             print(f"error: '{filter_option}' is not a valid filter criteria. Available filters are 'dir' and 'file'")
#             return

#         if sort_by_time:
#             contents = sorted(contents, key=lambda x: x['time_modified'])
#         if reverse:
#             contents = list(reversed(contents))
            
#         for item in contents:
#             if show_all or not item['name'].startswith('.'):
#                 if vertical:
#                     formatted_time = format_time(item['time_modified'])
#                     print(f"{item['permissions']} {item['size']} {formatted_time} {item['name']}")
#                 else:
#                     print(item['name'])

# def main():
#     json_file = 'structure.json'
    
#     show_all = '-A' in sys.argv
#     vertical = '-l' in sys.argv
#     reverse = '-r' in sys.argv
#     sort_by_time = '-t' in sys.argv

#     filter_option = None
#     for arg in sys.argv:
#         if arg.startswith('--filter='):
#             filter_option = arg.split('=')[1]
#             break

#     directory_structure = load_directory_structure(json_file)
#     print_ls(directory_structure, show_all, vertical, reverse, sort_by_time, filter_option)

# if __name__ == "__main__":
#     main()


# import json
# import sys
# from datetime import datetime

# def load_directory_structure(json_file):
#     with open(json_file, 'r') as f:
#         return json.load(f)

# def format_time(timestamp):
#     return datetime.fromtimestamp(timestamp).strftime('%b %d %H:%M')

# def print_ls(directory, show_all=False, vertical=False, reverse=False, sort_by_time=False, filter_option=None):
#     if 'contents' in directory:
#         contents = directory['contents']
        
#         if filter_option == 'file':
#             contents = [item for item in contents if not item['permissions'].startswith('d')]
#         elif filter_option == 'dir':
#             contents = [item for item in contents if item['permissions'].startswith('d')]
#         elif filter_option:
#             print(f"error: '{filter_option}' is not a valid filter criteria. Available filters are 'dir' and 'file'")
#             return

#         if sort_by_time:
#             contents = sorted(contents, key=lambda x: x['time_modified'])
#         if reverse:
#             contents = list(reversed(contents))
            
#         for item in contents:
#             if show_all or not item['name'].startswith('.'):
#                 if vertical:
#                     formatted_time = format_time(item['time_modified'])
#                     print(f"{item['permissions']} {item['size']} {formatted_time} {item['name']}")
#                 else:
#                     print(item['name'])

# def print_help():
#     print("Usage: python script.py [OPTIONS]")
#     print("Options:")
#     print("  -A       show all files")
#     print("  -l       use a long listing format")
#     print("  -r       reverse order")
#     print("  -t       sort by time modified")
#     print("  --filter=TYPE   filter by 'dir' or 'file'")
#     print("  --help   display this help and exit")

# def main():
#     json_file = 'structure.json'
    
#     if '--help' in sys.argv:
#         print_help()
#         sys.exit(0)
    
#     show_all = '-A' in sys.argv
#     vertical = '-l' in sys.argv
#     reverse = '-r' in sys.argv
#     sort_by_time = '-t' in sys.argv

#     filter_option = None
#     for arg in sys.argv:
#         if arg.startswith('--filter='):
#             filter_option = arg.split('=')[1]
#             break

#     directory_structure = load_directory_structure(json_file)
#     print_ls(directory_structure, show_all, vertical, reverse, sort_by_time, filter_option)

# if __name__ == "__main__":
#     main()

import json
import sys
from datetime import datetime

def load_directory_structure(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%b %d %H:%M')

def human_readable_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.1f}{unit}"
        size /= 1024.0
    return f"{size:.1f}PB"

def print_ls(directory, show_all=False, vertical=False, reverse=False, sort_by_time=False, filter_option=None, human_readable=False):
    if 'contents' in directory:
        contents = directory['contents']
        
        if filter_option == 'file':
            contents = [item for item in contents if not item['permissions'].startswith('d')]
        elif filter_option == 'dir':
            contents = [item for item in contents if item['permissions'].startswith('d')]
        elif filter_option:
            print(f"error: '{filter_option}' is not a valid filter criteria. Available filters are 'dir' and 'file'")
            return

        if sort_by_time:
            contents = sorted(contents, key=lambda x: x['time_modified'])
        if reverse:
            contents = list(reversed(contents))
            
        for item in contents:
            if show_all or not item['name'].startswith('.'):
                if vertical:
                    formatted_time = format_time(item['time_modified'])
                    size = human_readable_size(item['size']) if human_readable else item['size']
                    print(f"{item['permissions']} {size} {formatted_time} {item['name']}")
                else:
                    print(item['name'])

def print_help():
    print("Usage: python script.py [OPTIONS]")
    print("Options:")
    print("  -A           show all files")
    print("  -l           use a long listing format")
    print("  -r           reverse order")
    print("  -t           sort by time modified")
    print("  -h           display sizes in human readable format")
    print("  --filter=TYPE filter by 'dir' or 'file'")
    print("  --help       display this help and exit")

def main():
    json_file = 'structure.json'
    
    if '--help' in sys.argv:
        print_help()
        sys.exit(0)
    
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

    directory_structure = load_directory_structure(json_file)
    print_ls(directory_structure, show_all, vertical, reverse, sort_by_time, filter_option, human_readable)

if __name__ == "__main__":
    main()
