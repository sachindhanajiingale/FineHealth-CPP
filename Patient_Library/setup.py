from setuptools import setup, find_packages

setup(
    name='Patient_Library',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2.4',
    ],
    entry_points='''
        [console_scripts]
        Patient_Library=Patient_Library.manage:main
    ''',
)
