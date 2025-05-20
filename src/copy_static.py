import os, shutil

def copy_static_to_public(src="./static", dst="./public"):
    if dst == "./public" and os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            copy_static_to_public(src_path, dst_path)
    