from setuptools import setup

setup(
    name='daterenamer',
    version='0.1',
    packeges=['renamer'],
    py_modules=['daterenamer'],
    license='MIT',
    author='Qabil Orucov',
    author_email='orqabil15509@sabah.edu.az',
    description='Commondline tool written in Python 3 for renaming files',
    install_requires=['click>=3.3'],
    entry_points='''
        [console_scripts]
        daterenamer=daterenamer:all_procedure
        '''
)