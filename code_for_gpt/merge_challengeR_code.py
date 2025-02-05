import os

# Set the folder containing .R files
folder_path = "/Users/ariellubonja/prog/challengeR/R"  # Change this to your actual folder path

# Output file
output_file = "full_code.txt"

# Get a list of all .R files in the folder
r_files = [f for f in os.listdir(folder_path) if f.endswith(".R")]

# Sort files alphabetically (optional)
r_files.sort()

# Merge the files
with open(output_file, "w", encoding="utf-8") as outfile:
    for r_file in r_files:
        file_path = os.path.join(folder_path, r_file)
        with open(file_path, "r", encoding="utf-8") as infile:
            outfile.write(f"\n# --- Start of {r_file} ---\n\n")  # Separator
            outfile.write(infile.read())
            outfile.write(f"\n# --- End of {r_file} ---\n\n")  # Separator

print(f"All .R files have been merged into {output_file}")
