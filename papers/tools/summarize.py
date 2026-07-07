import os
scratch_dir = "../tools/summary"
output_md = os.path.join(scratch_dir, "summarized_abstracts.md")

with open(output_md, "w", encoding="utf-8") as out:
    out.write("# Abstracts of the Available FOSS Research Papers\n\n")

    for subdir in ["01", "02"]:
        out.write(f"## Question {subdir} Papers\n\n")
        subdir_path = os.path.join(scratch_dir, subdir)
        if not os.path.exists(subdir_path):
            continue

        files = sorted(os.listdir(subdir_path))
        for file in files:
            if not file.endswith(".txt"):
                continue

            file_path = os.path.join(subdir_path, file)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # Get the first 2500 characters
            snippet = content[:2500]

            out.write(f"### {file[:-4]}\n")
            out.write("```text\n")
            out.write(snippet)
            out.write("\n```\n\n")
            out.write("---\n\n")

print(f"Summarized abstracts saved to {output_md}")
