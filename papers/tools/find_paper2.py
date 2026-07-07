import subprocess

pdf_path = "../02/02 Insights into the Trilateral Relationship of Crowdfunding Campaigns, Open Source and Communities.pdf"

print("Searching PDF pages for authors: Ilin, Platis, Hammouda...")

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
        if "Ilin" in text or "trilateral relationship" in text.lower():
            print(f"Found on page {page}!")
            found_pages.append(page)
            if len(found_pages) >= 5:
                break
    except Exception as e:
        print(f"Error on page {page}: {e}")
        break

print(f"All matching pages: {found_pages}")
