import os
import sys
import time

def get_directory_structure(rootdir, max_depth=3, ignore_dirs=['.git']):
    """
    Crée une représentation structurée d'un répertoire sous forme de texte.
    """
    structure = []
    rootdir = rootdir.rstrip(os.sep)
    start_prefix = rootdir.rsplit(os.sep, 1)[-1]

    def recursive_directory_listing(directory, prefix, depth):
        if depth > max_depth:
            structure.append(prefix + '...')
            return

        items = os.listdir(directory)
        entries = [os.path.join(directory, i) for i in items]
        dirs = [d for d in entries if os.path.isdir(d) and os.path.basename(d) not in ignore_dirs]
        files = [f for f in entries if os.path.isfile(f)]

        for dir in dirs:
            structure.append(prefix + os.path.basename(dir))
            if os.path.basename(dir) not in ignore_dirs:
                recursive_directory_listing(dir, prefix + "│   ", depth + 1)

        for file in files:
            structure.append(prefix + '├── ' + os.path.basename(file))

    structure.append(start_prefix)
    recursive_directory_listing(rootdir, "", 1)

    return "\n".join(structure)

if __name__ == "__main__":
    directory_to_scan = r"D:\Compte ASUS\Desktop\Project-root"
    structure = get_directory_structure(directory_to_scan)

    with open("structure_projet.txt", "w", encoding="utf-8") as f:
        f.write(structure)

    print(structure)
