from markdown_blocks import markdown_to_html_node
import os

def generate_pages_recursive(path="./content"):
    template_path = "./template.html"
    files = os.listdir(path)
    for file in files:
        src_path = os.path.join(path, file)
        dst_path = src_path.replace("./content", "./public").replace(".md", ".html")
        if os.path.isfile(src_path):
            generate_page(src_path, template_path, dst_path)
        else:
            generate_pages_recursive(src_path)

    


def generate_page(from_path, template_path, dst_path):
    print(f"Generating page from {from_path} to {dst_path} using {template_path}")
    with open(from_path, "r") as f:
        contents = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(contents).to_html()
    title = extract_title(contents)

    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_node)
    
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)

    with open(dst_path, "w") as f:
        f.write(html)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip().lstrip("# ")
    raise Exception("no header in markdown")
