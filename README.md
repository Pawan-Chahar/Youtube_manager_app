
```markdown
# YouTube Manager App

A simple, lightweight **Python console-based YouTube video manager** that helps you organize and keep track of your favorite YouTube videos, playlists, or channels — all locally on your machine!

Perfect for beginners learning Python file handling, classes, error handling, and building small CLI tools.

## What This Project Does

This app lets you:
- Add new YouTube videos (title + URL)
- View your saved list of videos
- Update or delete entries
- Save everything persistently to a text file (`youtube.txt`)
- Handle errors gracefully (wrong inputs, file issues, etc.)

It's a great mini-project to practice:
- Python classes & objects
- File I/O (reading/writing text files)
- Basic error handling
- Command-line user interaction (menu-driven program)

No external APIs, no internet required after setup — everything runs locally!

## Tech Stack

- **Python** 3.x (pure Python — no external libraries needed!)
- File handling (`open()`, `readlines()`, `writelines()`)
- Basic OOP (classes for structure)
- Exception handling (`try-except`)

## Project Structure

``` bash
Youtube_manager_app/
├── dict_enum.py          # Likely defines enums or constants (dictionaries/enumerations for options)
├── error_handling.py     # Custom error handling functions or exceptions
├── youtube.txt           # Data file where your video list is saved (auto-created/updated)
└── youtube_manager.py    # Main program — contains the core logic, menu, and video management
```

## How to Run the App

### 1. Clone the repository

```bash
git clone https://github.com/Pawan-Chahar/Youtube_manager_app.git
cd Youtube_manager_app
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Run the main script

```bash
python youtube_manager.py
```

You'll see a simple menu like:

```
=== YouTube Manager ===
1. Add a video
2. List all videos
3. Update a video
4. Delete a video
5. Exit
Enter your choice:
```

Just type numbers and follow the prompts!

## Example Usage

1. Choose **1** → Enter video title and URL  
   → Saved to `youtube.txt`
2. Choose **2** → See your full list
3. Choose **3** or **4** → Modify or remove entries

Data persists between runs thanks to the text file.



