from setuptools import find_packages, setup
setup(
    name='foodscrape',
    packages=find_packages(include=['foodscrape']),
    version='0.0.8',
    description='Custom scraping library for allrecipes.com',
    author='Maximiliano Rivera-Patton',
    license='MIT',
    install_requires=['bs4','textblob','pandas','xlsxwriter','sklearn'],
    setup_requires=['pytest-runner']
)