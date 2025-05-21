import subprocess
from copy_static import copy_static_to_public
from generate_page import generate_page

def main():
    copy_static_to_public()
    generate_page("./content/index.md", "./template.html", "public/index.html")
    subprocess.run(["python3", "-m", "http.server", "8888"], cwd="public")
    
if __name__ == "__main__":
    main()
