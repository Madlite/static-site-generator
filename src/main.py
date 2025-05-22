import subprocess
from copy_static import copy_static_to_public
from generate_page import generate_pages_recursive

def main():
    copy_static_to_public()
    generate_pages_recursive()
    subprocess.run(["python3", "-m", "http.server", "8888"], cwd="public")
    
if __name__ == "__main__":
    main()
