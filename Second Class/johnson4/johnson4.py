class User: 
    # Class to represent a user and their music collection
    def __init__(self, username):
        # Initialize the user with a username and an empty collection
        self.username = username
        # Initialize an empty dictionary to store songs
        self.collection = {} 

    # Function to add a song to the collection
    def addSong(self, title, artist):
        if title in self.collection:
            print(f"'{title}' already exists.")
        else:
            self.collection[title] = artist
            print(f"Added '{title}' by {artist}.")

    # Function to retrieve song details
    def retrieveSong(self, title):
        # Check if the song exists in the collection
        artist = self.collection.get(title)
        if artist:
            print(f"'{title}' is by {artist}.")
        else:
            print(f"'{title}' not found.")
    # Function to retrieve song details
    def updateSong(self, title, new_artist):
        # Check if the song exists in the collection
        if title in self.collection:
            self.collection[title] = new_artist
            print(f"Updated '{title}' to be by {new_artist}.")
        else:
            print(f"'{title}' not found.")

    # Function to delete a song from the collection        
    def deleteSong(self, title):
        # Check if the song exists in the collection
        if title in self.collection:
            del self.collection[title]
            print(f"Deleted '{title}' from the collection.")
        else:
            print(f"'{title}' not found in the collection.")

    # Function to display all songs in the collection
    def displaySongs(self):
        # Check if the collection is empty
        if not self.collection:
            print("No songs in the collection.")
        else:
            print("Your music collection:")
            # Iterate through the collection and print each song
            for title, artist in self.collection.items():
                print(f"- {title} by {artist}")


def main():
    print("Welcome to the Music Collection Program!")
    users = {}
    current_user = None

    while True:
        print("=== Menu ===")
        print("1. Add a User")
        print("2. Change a User")
        print("3. Add a song")
        print("4. Retrieve song details")
        print("5. Update song details")
        print("6. Delete Song")
        print("7. Display all Songs")
        print("8. Exit")

        choice = int(input("Choose an option: "))
        match choice:

            case 1:
                username = input("Enter new username: ")
                if username in users:
                    print("User already exists.")
                else:
                    # Create a new user and add to the users dictionary
                    users[username] = User(username)
                    # Set the current user to the new user
                    current_user = users[username]
                    print(f"User '{username}' added and set as current user.")

            case 2:
                if not users:
                    print("No users available. Add a user first.")
                    continue
                print("Available users:", ", ".join(users.keys()))
                # Prompt the user to select a username to switch to
                username = input("Enter username to switch to: ")
                if username in users:
                    # Set the current user to the selected user
                    current_user = users[username]
                    print(f"Switched to user '{username}'.")
                else:
                    print("User not found.")

            case 3:
                # Check if a user is selected
                if current_user:
                    title = input("Enter song title: ")
                    artist = input("Enter artist name: ")
                    # Add the song to the current user collection
                    current_user.addSong(title, artist)
                else:
                    print("No user selected. Please add or switch to a user.")

            case 4:
                # Check if a user is selected
                if current_user:
                    title = input("Enter song title: ")
                    # Retrieve the song details from the current user collection
                    current_user.retrieveSong(title)
                else:
                    print("No user selected.")

            case 5:
                # Check if a user is selected
                if current_user:
                    title = input("Enter song title to update: ")
                    new_artist = input("Enter new artist name: ")
                    # Update the song in the current user collection
                    current_user.updateSong(title, new_artist)
                else:
                    print("No user selected.")

            case 6:
                # Check if a user is selected
                if current_user:
                    title = input("Enter song title to delete: ")
                    # Delete the song from the current user collection
                    current_user.deleteSong(title)
                else:
                    print("No user selected.")

            case 7:
                # Check if a user is selected
                if current_user:
                    # Display all songs in the current user collection
                    current_user.displaySongs()
                else:
                    print("No user selected.")

            case 8:
                # Exit the program
                print("Exiting Program.")
                break

            case _:
                print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
