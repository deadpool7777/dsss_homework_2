from setuptools import setup, find_packages

setup(
    name='your_project',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'your_script = your_module.module_file:main',
        ],
    },
)

