import os

def search_word_in_files(folder_path, search_word):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if search_word in content:
                        print(f"Word '{search_word}' found in: {file_path}")
            except (UnicodeDecodeError, PermissionError):
                pass

if __name__ == "__main__":
    folder_to_search = input("Enter the path to the folder: ")
    word_to_find = input("Enter the word to search for: ")
    
    if os.path.isdir(folder_to_search):
        search_word_in_files(folder_to_search, word_to_find)
    else:
        print("The specified path is not a valid directory.")
