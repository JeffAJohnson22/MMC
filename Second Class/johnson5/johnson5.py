class Folder:
    def __init__(self, name):
        # Initialize the folder with a name, an empty list of files, and an empty list of subfolders
        self.name = name
        # Initialize an empty list to store files
        self.files = []
        # Initialize an empty list to store subfolders
        self.subfolders = []

    # Function to add a file to the folder
    def add_file(self, file_name):
        # Check if the file already exists, so we dont get duplicates
        if file_name not in self.files:
            self.files.append(file_name)

    # Function to add a subfolder to the folder
    def add_subfolder(self, folder_name):
        # Check if the folder already exists, so we dont get duplicates
        if folder_name.lower() in [f.name.lower() for f in self.subfolders]:
            return
        # Create a new subfolder and append it to the list of subfolders
        new_folder = Folder(folder_name)
        self.subfolders.append(new_folder)
    
    # Function to select a subfolder by name
    # This function searches for a subfolder by name and returns it 
    # If the folder is not found, it returns None
    def select_folder(self, name):
        if self.__eq__(name):
            return self
        for sub in self.subfolders:
            if sub.__eq__(name):
                return sub.select_folder(name)
        return None

    # Function to count the total number of files in the folder and its subfolders
    def __count_files(self):
        count = len(self.files)
        for sub in self.subfolders:
            count += sub.__count_files()
        return count
    
    # Function to count the total number of subfolders in the folder
    # handling casing as well
    def __eq__(self, other):
        if isinstance(other, Folder):
            return self.name.lower() == other.name.lower()
        if isinstance(other, str):
            return self.name.lower() == other.lower()
        return False
    
    # Function to count the total number of files in the folder and its subfolders
    def __len__(self):
        return self.__count_files()
    
    # Function to print the folder structure
    def __str__(self, level=0):
        indent = "--" * level
        result = f"{indent}--Folder: {self.name}\n"
        for file in self.files:
            # Print the files in the folder
            # Indent the file names based on the folder level
            result += f"{indent}--File: {file}\n"
        for sub in self.subfolders:
            result += sub.__str__(level + 1)
        return result

def main():
    root = Folder("Root")
    current = root

    while True:
        print("=== Menu ===")
        print(f"==Current Folder: {current.name}==")
        print("1. Add a File")
        print("2. Add a Folder")
        print("3. Select a Folder")
        print("4. Print a Folder")
        print("5. Exit")
        print("===============")
        print(f"Total files in '{current.name}': {len(current)}") 
        print(f"Total folders in '{current.name}': {len(current.subfolders)}")
        print("===============")

        choice = int(input("Choose an option: "))
        match choice:

            case 1:
                fileName = input("Enter a File Name: ")
                current.add_file(fileName)
            case 2:
                subFolderName = input("Enter a Folder Name: ")
                current.add_subfolder(subFolderName)
            case 3:
                folderName = input("Enter a Folder Name: ")
                print(f"Searching for folder: '{folderName}'")
                # Check if the folder exists
                if folderName.lower() == current.name.lower():
                    print(f"Already in folder: '{current.name}'")
                    continue
                # Attempt to select the folder
                # If the folder is not found, not found
                try:
                    selected = root.select_folder(folderName)
                    if selected is not None:
                        print(f"Switched to folder: '{selected.name}'")
                        current = selected
                    else:
                        print("Folder not found.")
                except Exception as e:
                    print(f"Error selecting folder: {e}")
            case 4:
                # Print the folder structure
                print(f"Total number of files in the folder and all its subfolders: {current.__len__()}")
                print(current.__str__())
            case 5: 
                # Exit the program
                print("Exiting the Program.")
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
