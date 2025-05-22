import subprocess
import sys
from copy_static import copy_static
from generate_page import generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_static("docs")
    generate_pages_recursive(basepath)
    # subprocess.run(["python3", "-m", "http.server", "8888"], cwd="public")
    
if __name__ == "__main__":
    main()
