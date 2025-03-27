import os
import argparse

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
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Recursively merge source code files into a single file.")
    parser.add_argument("--input_folder", required=True, help="The folder to browse for source code files.")
    parser.add_argument("--output_file", required=True, help="The file where all source code will be appended.")
    parser.add_argument(
        "--extensions",
        nargs="+",
        default=['.py'],
        help="List of file extensions to include (default: .py)."
    )
    args = parser.parse_args()
    #print("The source file path is: ", args.input_folder)
    #print("The output file path is: ", args.output_file)
    # Call the function with parsed arguments
    append_source_code_to_file(args.input_folder, args.output_file, tuple(args.extensions))