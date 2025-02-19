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

def list_videos():
    cursor.execute('SELECT * FROM videos')
    videos = cursor.fetchall()

    if not videos:
        print("No videos found.")
        return

    print("\n=== Video List ===")
    for row in videos:
        print(f"ID: {row[0]}, Name: {row[1]}, Time: {row[2]}")

def add_video(name, time):
    cursor.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (name, time))
    conn.commit()
    

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
        cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
        conn.commit()
        print("Video deleted successfully!")
    else:
        print("Deletion canceled.")

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
            print("❌ Invalid choice! Please enter a number between 1 and 5.")
    conn.close()

if __name__ == "__main__":
    main()

