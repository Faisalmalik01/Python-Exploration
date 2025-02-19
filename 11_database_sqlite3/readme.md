# YOUTUBE MANAGER WITH DATABASE SQLITE 3


## What This Project Will Do

This project, **YouTube Manager**, is a simple CLI Python application that demonstrates various aspects of error handling through database operations, user input validation, and safe data manipulation. It will:

- Manage a list of YouTube videos using an SQLite database.
- Allow users to list, update, delete, and search for videos while handling potential input errors.
- Ensure robust exception handling to prevent crashes and improve user experience.

## 1. Database Operations with SQLite

```python
import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL 
    )
''')
```

### Keywords and Mechanisms

- **`sqlite3.connect()`**: Establishes a connection with the SQLite database.
- **`cursor.execute()`**: Executes SQL commands.
- **`CREATE TABLE IF NOT EXISTS`**: Ensures the table is created only if it does not exist.

### Underlying Mechanisms

- **Database Persistence**: Stores video data persistently.
- **Schema Enforcement**: Ensures a structured format for video data.

## 2. Listing and Adding Videos with Error Handling

```python
def list_videos():
    try:
        cursor.execute('SELECT * FROM videos')
        videos = cursor.fetchall()
        if not videos:
            print("No videos found.")
            return
        for row in videos:
            print(f"ID: {row[0]}, Name: {row[1]}, Time: {row[2]}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def add_video(name, time):
    try:
        cursor.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (name, time))
        conn.commit()
        print("Video added successfully!")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
```

### Error Handling Techniques Used

- **Try-Except Blocks**: Catches and handles SQLite errors.
- **Exception Reporting**: Provides meaningful messages to users.

## 3. Updating and Deleting Videos with Input Validation

```python
def update_video(video_id, name, time):
    try:
        cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
        conn.commit()
        print("Video updated successfully!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def delete_video(video_id):
    confirm = input("Are you sure you want to delete this video? (y/n): ").strip().lower()
    if confirm == 'y':
        try:
            cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
            conn.commit()
            print("Video deleted successfully!")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    else:
        print("Deletion canceled.")
```

### Input Validation and Error Handling

- **User Confirmation**: Prevents accidental deletions.
- **Exception Handling**: Catches database-related errors.
- **Commit Mechanism**: Ensures data consistency.

## 4. Searching Videos Safely

```python
def search_video():
    search_term = input("Enter video name or ID to search: ")
    try:
        cursor.execute("SELECT * FROM videos WHERE id = ? OR name LIKE ?", (search_term, f"%{search_term}%"))
        videos = cursor.fetchall()
        if not videos:
            print("No matching videos found.")
            return
        for row in videos:
            print(f"ID: {row[0]}, Name: {row[1]}, Time: {row[2]}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
```

### Error Handling Techniques Used

- **Handling Multiple Data Types**: Supports searching by ID or name.
- **Ensuring SQL Security**: Uses parameterized queries to prevent SQL injection.

## 5. Main Menu with Error Handling

```python
def main():
    print("🎥 Welcome to YouTube Video Manager!")
    while True:
        print("\n=== Main Menu ===")
        print("1. 📋 List all videos")
        print("2. ➕ Add new video")
        print("3. 📝 Update video")
        print("4. ❌ Delete video")
        print("5. 🔍 Search video")
        print("6. 🚪 Exit")
        choice = input("\nEnter your choice (1-6): ").strip()
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            search_video()
        elif choice == '6':
            print("\nThanks for using YouTube Video Manager! Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 6.")
    conn.close()

if __name__ == "__main__":
    main()
```

## Key Concepts Learned

- **Database Management**: Handling SQLite operations.
- **Exception Handling**: Preventing crashes and improving UX.
- **User Input Validation**: Ensuring safe user interaction.
- **Error Reporting**: Displaying meaningful messages.

