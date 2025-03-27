import os

def append_source_code_to_file(source_folder, output_file, extensions):
    """
    Recursively browse through a folder and append all source code text to a single file.

    :param source_folder: The folder to browse.
    :param output_file: The file where all source code will be appended.
    :param extensions: A tuple of file extensions to include (e.g., ('.py', '.js')).
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(source_folder):
            for file in files:
                if file.endswith(extensions):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            outfile.write(f"// File: {file_path}\n")
                            outfile.write(infile.read())
                            outfile.write("\n\n")
                    except Exception as e:
                        print(f"Could not read file {file_path}: {e}")

if __name__ == "__main__":
    # Specify the folder to browse and the output file
    source_folder = r"c:\path\to\your\folder"  # Change this to your folder path
    output_file = r"c:\path\to\output\all_source_code.txt"  # Change this to your desired output file path
    extensions = ('.py', '.js', '.java', '.cpp', '.c', '.cs', '.html', '.css')  # Add or modify extensions as needed

    append_source_code_to_file(source_folder, output_file, extensions)