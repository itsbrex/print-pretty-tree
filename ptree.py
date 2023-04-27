import os
import fnmatch
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Define the folders and file patterns to exclude
EXCLUDED_FOLDERS = {
    'node_modules', '.git', '.history', '__pycache__', '.vscode', '.idea',
    'venv', '.env', '.ipynb_checkpoints', 'dist', 'build', '.next', '.nuxt'
}
EXCLUDED_FILE_PATTERNS = {'*.log', 'yarn.lock', 'package-lock.json', '*.pyc', '*.pyo', '*.egg-info', '*.egg', '.DS_Store'}

# Define file type colors
FILE_TYPE_COLORS = {
    '.md'  : Fore.CYAN,    # Markdown files
    '.json': Fore.YELLOW,  # JSON files
    '.py'  : Fore.GREEN,   # Python files
    '.js'  : Fore.BLUE,    # JavaScript files
    '.html': Fore.MAGENTA, # HTML files
    '.css' : Fore.CYAN,    # CSS files
    '.txt' : Fore.WHITE,   # Text files
    '.csv' : Fore.YELLOW,  # CSV files
    '.xml' : Fore.MAGENTA, # XML files
    '.yml' : Fore.YELLOW,  # YAML files
    '.yaml': Fore.YELLOW,  # YAML files
    '.ts'  : Fore.BLUE,    # TypeScript files
    '.jsx' : Fore.BLUE,    # JSX files
    '.tsx' : Fore.BLUE,    # TypeScript JSX files
    '.sh'  : Fore.GREEN,   # Shell script files
    '.log' : Fore.RED,     # Log files
    '.ini' : Fore.YELLOW,  # INI files
    '.sql' : Fore.CYAN,    # SQL files
    '.java': Fore.BLUE,    # Java files
    '.c'   : Fore.BLUE,    # C files
    '.cpp' : Fore.BLUE,    # C++ files
    '.h'   : Fore.BLUE,    # Header files
    '.hpp' : Fore.BLUE,    # C++ Header files
    # Add more file types and colors here as needed
}

def get_file_color(filename):
    # Get the file extension
    file_extension = os.path.splitext(filename)[1]
    # Return the color based on the file extension, or the default color if not specified
    return FILE_TYPE_COLORS.get(file_extension, Fore.RESET)

def print_project_tree(start_path, excluded_folders, excluded_file_patterns, prefix=''):
    # List the contents of the current directory
    items = [item for item in os.listdir(start_path) if item not in excluded_folders]
    items.sort()
    
    for index, item in enumerate(items):
        # Construct the full path of the item
        item_path = os.path.join(start_path, item)
        
        # Determine if this is the last item in the list
        is_last_item = index == len(items) - 1
        
        # Determine the prefix for the current item
        item_prefix = '└─ ' if is_last_item else '├─ '
        
        # Determine the prefix for the child items
        child_prefix = '    ' if is_last_item else '│   '
        
        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Print the current directory with the prefix
            print(prefix + item_prefix + item)
            
            # Recursively print the contents of the directory
            print_project_tree(item_path, excluded_folders, excluded_file_patterns, prefix + child_prefix)
        else:
            # Check if the file matches any of the excluded patterns
            if not any(fnmatch.fnmatch(item, pattern) for pattern in excluded_file_patterns):
                # Get the color for the file
                file_color = get_file_color(item)
                
                # Print the file with the prefix and color
                print(prefix + item_prefix + file_color + item)

# Get the current working directory
cwd = os.getcwd()

# Print the project tree
print(os.path.basename(cwd))
print_project_tree(cwd, EXCLUDED_FOLDERS, EXCLUDED_FILE_PATTERNS)