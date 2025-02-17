import json
import os

DATA_FILE_PATH = os.path.join('10_error_handling', 'youtube.txt') #constant

def load_data():
    """Loads video data from the JSON file.

    Returns:
        list: A list of video dictionaries, or an empty list if the file is not found.
    """
    try:
        with open(DATA_FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found. Returning an empty list.")
        return []

def save_data_helper(videos):
    """Saves video data to the JSON file."""
    with open(DATA_FILE_PATH, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    """Lists all videos with their index and duration."""
    print("\n")
    print("*" * 70)
    if not videos:
        print("No videos found.")
        return
    
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")

    print("\n")
    print("*" * 70)

def add_video(videos):
    """Adds a new video to the list."""
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print(f"Video '{name}' added successfully!")

def update_video(videos):
    """Updates an existing video's details."""
    list_all_videos(videos)
    try: #Error Handling Added
        index = int(input("Enter the video number to update: "))
        if 1 <= index <= len(videos):
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            videos[index-1] = {'name': name, 'time': time}
            save_data_helper(videos)
        else:
            print("Invalid index selected")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_video(videos):
    """Deletes a video from the list."""
    list_all_videos(videos)
    try: #Error Handling Added
        index = int(input("Enter the video number to delete: "))

        if 1 <= index <= len(videos):
            # Confirmation
            confirmation = input(f"Are you sure you want to delete video {index}? (y/n): ")
            if confirmation.lower() == 'y':
                del videos[index-1]
                save_data_helper(videos)
                print(f"Video at index {index} deleted successfully!") #Fixed sentence
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid video index Selected.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")
        #print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Thank you for using YouTube Manager!")
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()
