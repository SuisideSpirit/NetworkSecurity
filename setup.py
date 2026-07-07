from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""

    requirements_list = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e." and requirement != "-e .":
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    return requirements_list

print(get_requirements("requirements.txt"))
setup(
    name="Network_Security",
    version="0.0.1",
    author="Pratik",
    author_email="pratiksinghnegi7@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)