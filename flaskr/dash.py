# Home for estimation feature and data exploration images
# Provides login and logout functions
import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from . import forecast

bp = Blueprint('dash', __name__)

@bp.route('/dashboard', methods=('GET', 'POST'))
def dash():
    # Redirects to login page if user is not authenticated
    if "authenticated" not in session:
        return redirect('/login')

    # Values that will be returned to the template
    forecasted = None
    property_type = None
    room_type = None
    bedrooms = None
    beds = None
    zipcode = None

    if (request.method == 'POST'):
        forecasted = forecast.estimate_price(request)

        # Assign returned strings
        if request.form['property-type'] == 'apartment':
            property_type = "Apartment"
        elif request.form['property-type'] == 'house':
            property_type = "House"

        if request.form['room-type'] == 'entire':
            property_type = "Entire home/apt"
        elif request.form['room-type'] == 'private':
            property_type = "Private room"
        elif request.form['room-type'] == 'shared':
            property_type = "Shared room"

        bedrooms = request.form['bedrooms']
        beds = request.form['beds']
        zipcode = request.form['zipcode']

            

    return render_template('dashboard.html', price=forecasted, property_type=property_type, room_type=room_type, bedrooms=bedrooms, beds=beds, zipcode=zipcode)