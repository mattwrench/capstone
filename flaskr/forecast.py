import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

# Linear regression coefficients
BEDROOMS = 46.95255478
BEDS = 11.31627843

ZIP = {
    98119: 83.31005859,
    98109: 79.37011719,
    98107: 50.56005859,
    98117: 38.91992188,
    98103: 46.35009766,
    98105: 39.72998047,
    98115: 40.06982422,
    98122: 65,
    98112: 65.35986328,
    98144: 34.31982422,
    98101: 95.40966797,
    98121: 91.48974609,
    98102: 72.79980469,
    98199: 77.10009766,
    98104: 86.47998047,
    98134: 92.39013672,
    98136: 42.40966797,
    98126: 42.48974609,
    98146: 58.33984375,
    98116: 53.48974609,
    98177: 0,
    98118: 25.14013672,
    98108: 15.85986328,
    98133: 20.12988281,
    98106: 19.66992188,
    98178: 12.56005859,
    98125: 29.73974609
}

APARTMENT = 0
HOUSE = 10

ENTIRE = 75
PRIVATE = 32
SHARED = 0

def estimate_price(request):
    price = 0.0

    # Bedrooms
    price += BEDROOMS * int(request.form['bedrooms'])

    # Beds
    price += BEDS * int(request.form['beds'])

    # ZIP
    price += ZIP[int(request.form['zipcode'])]

    # Property Type
    type = request.form['property-type']
    if type == 'apartment':
        price += APARTMENT
    elif type == 'house':
        price += HOUSE

    # Room Type
    type = request.form['room-type']
    if type == 'entire':
        price += ENTIRE
    elif type == 'private':
        price += PRIVATE
    elif type == 'shared':
        price += SHARED

    # Round to nearest dollar
    price = round(price) 

    return price