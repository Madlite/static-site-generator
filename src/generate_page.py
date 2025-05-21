from markdown_blocks import markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        contents = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(contents).to_html()
    title = extract_title(contents)

    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_node)

    with open(dest_path, "w") as f:
        f.write(html)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip().lstrip("# ")
    raise Exception("no header in markdown")
