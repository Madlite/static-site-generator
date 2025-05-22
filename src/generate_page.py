from markdown_blocks import markdown_to_html_node
import os


def generate_pages_recursive(basepath, path="./content"):
    template_path = "./template.html"
    files = os.listdir(path)
    for file in files:
        src_path = os.path.join(path, file)
        dst_path = src_path.replace("./content", "./docs").replace(".md", ".html")
        if os.path.isfile(src_path):
            generate_page(basepath, src_path, template_path, dst_path)
        else:
            generate_pages_recursive(basepath, src_path)


def generate_page(basepath, from_path, template_path, dst_path):
    print(f"Generating page from {from_path} to {dst_path} using {template_path}")
    with open(from_path, "r") as f:
        contents = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(contents).to_html()
    title = extract_title(contents)

    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_node)
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')
    
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)

    with open(dst_path, "w") as f:
        f.write(html)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip().lstrip("# ")
    raise Exception("no header in markdown")
