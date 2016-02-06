"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.

# Part 2: Write queries

m = Model.query
b = Brand.query

# Get the brand with the **id** of 8.

b8 = b.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

chevrolet_corvettes = m.filter(Model.brand_name == "Chevrolet", 
                                    Model.name == "Corvette").all()

# Get all models that are older than 1960.

older_models = m.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

younger_brands = b.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

cor_models = m.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
old_brands = b.filter(Brand.founded ==1903, Brand.discontinued == None).all()

# Get all brands that are either discontinued or founded before 1950.

brands = b.filter((Brand.founded < 1950) | 
                    (Brand.discontinued.isnot(None))).all()

# Get any model whose brand_name is not Chevrolet.

not_chevrolet = m.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = m.filter(Model.year==year).all()
    for car in models:
        print car.name, car.brand_name, car.brand.headquarters 

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    all_brands = b.all()
    for brand in all_brands:
        all_models = brand.models
        for model in all_models:
            print model.brand_name, model.name

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional

# Design a function in python that takes in any string as parameter, 
# and returns a list of objects that are brands whose name contains 
# or is equal to the input string.
def search_brands_by_name(mystr):
    brands = b.filter(Brand.name.like('%mystr%')).all()
    return brands


# Design a function that takes in a start year and end year (two integers), 
# and returns a list of objects that are models with years that fall between 
# the start year and end year.

def get_models_between(start_year, end_year):
    models = m.filter(Model.year > start_year, Model.year < end_year).all()
    return models

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# The returned value is a query, not the actual brand object. Specifically, 
# it returns "<flask_sqlalchemy.BaseQuery object at 0x10a606290>"


# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An association table exists just to connect other tables. It contains keys 
# from other tables, but it contains no unique, meaningful information
# in its own right. It manages relationships between other tables.


