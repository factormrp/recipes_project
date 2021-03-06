CHANGELOG
==========================================================
*This document outlines all notable changes to the project Types of changes included: Added, Changed, Removed, Deprecated, Fixed, Security*
==========================================================
# version[0.0.8]
##  Added
### scraping.py
    - debug attribute for Recipe class to print what type of error occurs
### encoding.py
    - multiprocessing for speedup by utilizing Pool.map
##  Changed
### scraping.py
    - changed urllib to requests in order to reuse http connections
    - changed BeautifulSoup parser from python's html parser to lxml


# version[0.0.7]
##  Added
### scraping.py
    - implemented cleaning method in Recipe to standardize ingredients
    - implemented quantized output
##  Changed
###   change.log -> changelog.md
    - changed to Markdown for easier previewing
### GIT 
    - moved encoding to new branch 
##  Removed
### GIT
    - stopped tracking whl and pyc files 


#   version[0.0.6]
##  Added
### encoding.py
    - implemented batched processing
    - implemented batched output
##  Changed
### scraping.py
    - fixed improper copy
    - fixed Recipe class to include error handling for scraping errors
    - changed return of getnutri method to sorted dictionary and standardized keys
### encoding.py
    - segmented code


#   version[0.0.5]
##  Added
### setup.py
    - initializer for the package
### encoding.py
    - moved code for creating DataFrame
##  Changed
### allrecipes_recipes.py -> scraping.py
    - moved into foodscrape package 


#   version[0.0.4]
##  Added
### allrecipes_recipes.py
    - code to create DataFrame and to export to excel
    - code to convert ingredients into one-hot encodings
### change.log
    - documentation file to keep detailed track of project
    with current progress
##  Changed
### allrecipes_recipes.py
    - values to nutrition values wrapped in list for eaiser
    concatenation to DataFrame 


#   version[0.0.3]
##  Added
### allrecipes_recipes.py
    - documentation to classes and helper methods
##  Changed
### allrecipes_recipes.py
    - data structure to hold Recipe ingredients from list
    to set 


#   version[0.0.2]
##  Added
### allrecipes_recipes.py
    - starter code to export pandas DataFrame to an excel
    sheet


#   version[0.0.1]
##  Added
### allrecipes_recipes.py 
    - class definitions of Recipebook and Recipe
    - helper method convertedstr to handle nonAscii numbers and spaces
    - helper method makesoup to encapsulate BeautifulSoup object creation