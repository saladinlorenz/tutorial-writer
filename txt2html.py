import re

def txt2html(filename):
    
    # Read the content of the text file
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Use regular expressions to make text between two asterisks bold
    content_html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
    content_html = re.sub(r'\*(.*?)\*\*', r'<strong>\1</strong>', content)
    # Replace line breaks with <br> tags
    content_html = content_html.replace("\n", "<br>")

    # Extract the main title (H1) from the filename
    filename_without_extension = filename.split(".")[0]  # Remove file extension
    main_title = f"<h1>{filename_without_extension}</h1>"

    # Insert the main title into the HTML content
    content_html = main_title + content_html

    # Change file extension from .txt to .html
    output_filename = filename.replace(".txt", ".html")

    # Write formatted HTML content to a file
    with open(output_filename, "w", encoding="utf-8") as f:
        # Write the beginning of the HTML document with Bootstrap
        f.write('<!DOCTYPE html>\n<html>\n<head>\n')
        f.write('<link rel="stylesheet" href="https://cdn.oaistatic.com/_next/static/css/f0019dbbf98d8b06.css" as="style" crossorigin="anonymous"/>\n')
        f.write('<noscript data-n-css=""></noscript>\n')
        f.write('<style>\n')
        f.write('body { font-family: Arial, sans-serif; margin: 40px; }\n')
        f.write('.strong { font-weight: bold; color: #337ab7; }\n')  # Blue color
        f.write('.code { background-color: #f0f0f0; padding: 10px; border-radius: 5px; color: #333; }\n')  # Dark gray color
        f.write('</style>\n</head>\n<body>\n')

        # Main content within a Bootstrap container
        f.write('<div class="container">\n')

        # Formatted content
        f.write('<div class="row">\n')
        f.write('<div class="col-md-12">\n')
        f.write(content_html)
        f.write('</div>\n')
        f.write('</div>\n')

        # End of Bootstrap container
        f.write('</div>\n')

        # Write the end of the HTML document
        f.write('\n</body>\n</html>')
