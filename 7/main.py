# Use type hints like "directory: Directory" inside the class it hints to
from __future__ import annotations


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str):
        self.name = name
        self.size = None
        self.parent = None
        self.subdirectories = []
        self.files = []

    def add_subdirectory(self, directory: Directory):
        self.subdirectories.append(directory)
        directory.parent = self

    def add_file(self, file: File):
        self.files.append(file)

    # Calculate the total (recursive) size of this directory.
    # All subdirectories must calculate their size first, otherwise
    # this function will fail because the size of a subdirectory is unknown
    def calculate_size(self):
        self.size = 0

        # Calculate the size of the subdirectories
        for subdirectory in self.subdirectories:

            # If the subdirectory size has not yet been calculated,
            # something must have gone wrong earlier
            if subdirectory.size == None:
                print("Subdirectory size not known, cannot calculate size!")
                self.size = None
                return

            # Otherwise, add it just like a file
            self.size += subdirectory.size

        # Calculate the size of the files in this directory
        for file in self.files:
            self.size += file.size

        return self.size


class FileSystem:
    def __init__(self):
        # Create the filesystem root directory
        self.root = Directory("/")

        # Start with the root as the current working directory
        self.cd("/")

        self.directory_sizes = []
        self.max_directory_size = 100_000
        self.size_total = 70_000_000
        self.size_required = 30_000_000
        self.size_in_use = None
        self.size_unused = None

    # Change directory
    def cd(self, directory: str):

        # Switch to the root directory
        if directory == "/":
            self.cwd = self.root
            return
        
        # Move one level out / up
        if directory == "..":
            self.cwd = self.cwd.parent
            return

        # Move one level in / down
        for subdirectory in self.cwd.subdirectories:
            if not directory == subdirectory.name:
                continue

            self.cwd = subdirectory
            break

    # For the ls command, the output will be on the subsequent lines,
    # and since we already keep track of the current directory with self.cwd,
    # there is nothing else to do here
    def ls(self):
        pass

    # A variant of depth-first search that traverses the file tree
    # and finds all of the directories with a given maximum size
    def find_small_directories(self, directory: Directory):
        small_directories = []

        # First, calculate the sizes of all subdirectories
        for subdirectory in directory.subdirectories:
            small_subdirectories = self.find_small_directories(subdirectory)

            # If a subdirectory has a size of at most 100000,
            # add it to the list of small directories
            small_directories.extend(small_subdirectories)

        # Then, calculate the size of the current directory
        size = directory.calculate_size()
        self.directory_sizes.append(size)

        # Add it to the list of small subdirectories if it's small enough
        if size <= self.max_directory_size:
            small_directories.append(size)

        # Return the small subdirectories found so far
        return small_directories

    def clean(self):
        # Determine how much
        self.size_in_use = self.root.size
        self.size_unused = self.size_total - self.size_in_use

        # Calculate the minimum size that must be freed for the update
        size_min = self.size_required - self.size_unused

        # Check the small directories in ascending order of size
        for size in sorted(self.directory_sizes):
            
            # Skip directories that are too small
            if size < size_min:
                continue

            # If it's big enough, return its size (mark for deletion)
            return size

def process_terminal_output(file_system: FileSystem):
    # Read the terminal output from the input file
    with open("input.txt", "r") as terminal:

        # Process the terminal output line by line
        for line in terminal.readlines():

            # Parse input line
            parts = line.rstrip().split(" ")

            # Process ls and cd commands
            if parts[0] == "$":
                command = parts[1]
                
                if command == "ls":
                    file_system.ls()
                
                elif command == "cd":
                    dir = parts[2]
                    file_system.cd(dir)
                
                else:
                    print(f"Invalid command: `{command}`")

            # Found a directory
            elif parts[0] == "dir":
                name = parts[1]
                directory = Directory(name)
                file_system.cwd.add_subdirectory(directory)

            # Found a file
            else:
                size = int(parts[0])
                name = parts[1]
                file = File(name, size)
                file_system.cwd.add_file(file)


def part_1(file_system: FileSystem):
    
    # Create the file tree based on the terminal output
    process_terminal_output(file_system)

    # Find directories with a size of at most 100.000 and sum their sizes
    small_directories = file_system.find_small_directories(file_system.root)
    file_system.small_directories = small_directories
    sum_of_total_sizes = sum(small_directories)
    
    print(f"Sum of total sizes of small directories: {sum_of_total_sizes}")


def part_2(file_system: FileSystem):
    
    # Find the smallest directory to be deleted in order to free up
    # enough space for the system update (30.000.000)
    size = file_system.clean()

    print(f"Total size of directory to be deleted: {size}")


if __name__ == "__main__":
    file_system = FileSystem()

    part_1(file_system)
    part_2(file_system)