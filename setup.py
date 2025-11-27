from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str)->List[str]:
    ''' This function will return the list of requirements to install/run this project'''
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements


setup(
    name='ds_project',
    version='0.0.1',
    author='Mitish Raina',
    author_email='rainamitish7@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)