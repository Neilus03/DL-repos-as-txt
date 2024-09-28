import os

'''
Below I leave the script to turn all code files of any repo into a unified txt, this is nice to have for
inputting LLMs with more context (Gemini for instance accepts up to 2M tokens already (as of September 2024)
'''

# Define the path to the repository folder
repo_folder = "path/to/your/repo"

# Define the output file where you want to store the combined content
output_file = "full_repo.txt"

# Initialize an empty list to hold file contents
file_contents = []

# Loop through all files in the repository folder including subfolders
for root, dirs, files in os.walk(repo_folder):
    for file in files:
        file_path = os.path.join(root, file)
        
        # Only process text-based files (e.g., .py, .md, .txt, .json, etc.)
        if file.endswith(('.py', '.md', '.txt', '.json', '.yaml', '.yml', '.java', '.js', '.cpp', '.c', '.sh')):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    # Add a file separator to keep track of where each file starts
                    file_contents.append(f"\n\n=== File: {file_path} ===\n\n")
                    file_contents.append(content)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")

# Write all the collected content into a single output file
with open(output_file, 'w', encoding='utf-8') as f_out:
    f_out.write('\n'.join(file_contents))

print(f"All files have been combined into {output_file}")
