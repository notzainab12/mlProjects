## setup.py will be responsible for creating my machine learning application as a package.
## and even deploy it to PyPI.

from setuptools import find_packages, setup
## ths will automsatically find all the packages in my project.

HYPEN_E_DOT = '-e .'


from typing import List

def getrequirements(file_path: str) -> List[str]:


    ''' this function will return the list of requirements'''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        ## this will replace the new line character with blank.

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements       


# when we read the lines from the file, it will also read the new line character(\n)
# so when we get requirements.txt, we'll replace \n with blank.
setup(

    name="mlproject",
    version="0.0.1",
    author="zainab",
    author_email="zzainab1225@gmail.com",
    packages=find_packages(),
    install_requires=getrequirements("requirements.txt")
)