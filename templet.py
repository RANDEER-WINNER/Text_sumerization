import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textsummerizer"

list_of_file = [
    ".github/workflows/.gitkeep",
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 1c78ec2190657b5ecee8284f51ad645d2ed6c0be
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
<<<<<<< HEAD
=======
=======
    f"src/{project_name}/_init_.py",
    f"src/{project_name}/components/_init_.py",
    f"src/{project_name}/utils/_init_.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/_init_.py",
    f"src/{project_name}/config/_init_.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/_init_.py",
    f"src/{project_name}/entity/_init_.py",
    f"src/{project_name}/constants/_init_.py",
>>>>>>> ecc67f28359cddbb4e72bf7531858f41e5696092
>>>>>>> 1c78ec2190657b5ecee8284f51ad645d2ed6c0be
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")

