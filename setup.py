from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of dependencies.

    Args:
        file_path (str): The path to the requirements file.

    Returns:
        List[str]: A list of dependencies specified in the requirements file,
                with '-e .' removed if present.
    """
    try:
        requirements = []
        with open(file_path) as file:
            requirements = file.readlines()
            requirements = [req.replace("\n", "") for req in requirements]

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except Exception as e:
        print(e)

    return requirements

setup(
    name='finance-bot',
    version='0.0.1',
    author='Muhammad Hamza Anjum',
    author_email='hamza.anjum380@gmail.com',
    description='A Finance Chatbot, which provides personalized financial assistance and insights.',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
