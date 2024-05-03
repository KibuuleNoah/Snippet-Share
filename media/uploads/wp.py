import weasyprint

# Define the HTML file and PDF file paths
html_file = "input.html"
pdf_file = "output.pdf"

# Open the HTML file
with open(html_file, "r") as f:
    html_string = f.read()

# Create a WeasyPrint document
doc = weasyprint.HTML(string=html_string)

# Render the document to a PDF file
doc.write_pdf(pdf_file)
