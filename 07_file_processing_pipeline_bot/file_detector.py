def file_detector(path):

    all_lists = {
        "img": [".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp"],
        "doc": [".pdf", ".doc", ".docx", ".odt", ".rtf", ".epub", ".mobi"],
        "text": [".txt", ".md"],
        "audio": [".mp3", ".wav", ".m4a", ".flac", ".aac", ".ogg"],
        "code": [".py", ".js", ".java", ".html", ".css", ".cpp",
                 ".c", ".cs", ".rb", ".go", ".ts", ".php",
                 ".swift", ".sh", ".rs", ".pl"],
        "data": [".csv", ".json", ".sql", ".xml", ".xlsx", ".yaml"],
        "archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "video": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm"],
        "fonts": [".ttf", ".otf", ".woff", ".woff2"],
        "config": [".ini", ".cfg", ".yml", ".env"]
    }

    files = {}

    try:
        for item in sorted(path.iterdir()):

            if item.is_symlink():
                continue

            if not item.is_file():
                continue

            ext = item.suffix.lower()
            category = "others"

            for name, extensions in all_lists.items():
                if ext in extensions:
                    category = name
                    break

            files[item] = category

    except Exception as e:
        print(f"Error detecting files: {e}")

    return files