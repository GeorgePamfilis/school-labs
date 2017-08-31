import zipfile
from io import BytesIO
import time

from flask import flash
from flask import render_template, session, redirect, url_for, jsonify
from flask import request
from flask import send_file
from flask import send_from_directory
from flask.views import MethodView
from wtforms import IntegerField, SubmitField

from app.download.meteo import MeteorologicalDataDownloader
from app.utils import makeArchive, dirEntries
from config import basedir
from . import download
import os
APP_STATIC = os.path.join(basedir, 'app/tmp')



class MeteoData(MethodView):

    def get(self):
        year_from = request.args.get('year_from', None, int)
        year_to = request.args.get('year_to', None, int)

        MeteorologicalDataDownloader(year_from, year_to, location='crete').main()

        makeArchive(dirEntries(APP_STATIC, True), APP_STATIC + '/data.zip', APP_STATIC)

        return send_from_directory(APP_STATIC, 'data.zip', as_attachment=True)


download.add_url_rule("/meteo-data", view_func=MeteoData.as_view("meteo-data"), methods=['GET', 'POST', 'PUT', 'DELETE'])


from flask_wtf import Form

class DataSelection(Form):
    yf = IntegerField('Year From')
    yt = IntegerField('Year T')
    ok = SubmitField('OK')


from app import csrf






@download.route('/crete', methods=['get','post'])
def test():
    form = DataSelection()
    if form.validate_on_submit():
        flash('You were successfully logged in')
        MeteorologicalDataDownloader(form.yf.data, form.yt.data, location='crete').main()
        flash('You were successfully logged in')
        makeArchive(dirEntries(APP_STATIC, True), APP_STATIC+'/data.zip', APP_STATIC)
        return send_from_directory(APP_STATIC, 'data.zip', as_attachment=True)

    else:
        flash('You were successfully logged in')

        return render_template('index.html', form=form)
    # makeArchive(dirEntries(APP_STATIC, True), APP_STATIC+'/data.zip', APP_STATIC)
    # return send_from_directory(APP_STATIC, 'data.zip', as_attachment=True)

