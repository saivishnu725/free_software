import subprocess
import re

pdf_path = "../02/01 Exploring the Susceptibility to Fraud of Monetary Incentive Mechanisms for Strengthening FOSS Projects.pdf"

print("Searching PDF pages for authors: Swierzy, Pohl, Ohm, Meier...")

# We can search page by page or read the table of contents.
# Let's extract metadata or check page ranges using pdftotext.
# Since it is 36MB, let's look for pages that contain "Swierzy" or "Susceptibility to Fraud".

# We'll run pdftotext to search for the title of the paper.
# Let's search page by page up to 1000 pages.
found_pages = []
for page in range(1, 1000):
    try:
        res = subprocess.run(
            ["pdftotext", "-f", str(page), "-l", str(page), pdf_path, "-"],
            capture_output=True,
            text=True,
            timeout=5
        )
        text = res.stdout
        if "Swierzy" in text or "Susceptibility to Fraud" in text:
            print(f"Found on page {page}!")
            found_pages.append(page)
            if len(found_pages) >= 5:
                break
    except Exception as e:
        print(f"Error on page {page}: {e}")
        break

print(f"All matching pages: {found_pages}")
