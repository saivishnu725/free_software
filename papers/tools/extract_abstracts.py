import os
import subprocess

papers_dir = "../"
scratch_dir = "../tools/summary"

os.makedirs(scratch_dir, exist_ok=True)

for subdir in ["01", "02"]:
    subdir_path = os.path.join(papers_dir, subdir)
    output_subdir = os.path.join(scratch_dir, subdir)
    os.makedirs(output_subdir, exist_ok=True)

    for file in os.listdir(subdir_path):
        if not file.endswith(".pdf"):
            continue
        if "FRENCH" in file:
            print(f"Skipping French paper: {file}")
            continue

        pdf_path = os.path.join(subdir_path, file)
        txt_name = os.path.splitext(file)[0] + ".txt"
        txt_path = os.path.join(output_subdir, txt_name)

        print(f"Extracting: {file}...")
        try:
            # Extract pages 1 and 2
            subprocess.run(["pdftotext", "-f", "1", "-l", "2", pdf_path, txt_path], check=True)
        except Exception as e:
            print(f"Error extracting {file}: {e}")

print("Extraction completed.")
