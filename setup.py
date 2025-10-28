from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:

    requirement_lst: List[str] = []
    try:
        with open('requirements.txt' , 'r') as file:
            # read all lines from the file
            lines = file.readlines()
            # remove any empty lines or whitespace
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except Exception as e:
        print(f"Error reading requirements.txt: {e}")
    return requirement_lst


setup(
    name = 'NetworkSecurity',
    version = '0.0.1',
    author = 'Krish Naik',
    author_email = 'krishnaik06@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements()
)

print (get_requirements())

