from flask import render_template,send_from_directory,request
import os,time,json
from app import app

@app.route('/css/<path:path>')
def send_css(path):
    # return send_from_directory(os.path.join(app.root_path, 'static/css'), path)
    return send_from_directory(app.static_folder+'/css', path)


@app.route('/js/<path:path>')
def send_js(path):
    # return send_from_directory(os.path.join(app.root_path, 'static/js'), path)
    return send_from_directory(app.static_folder + '/js', path)


@app.route('/images/<path:path>')
def send_image(path):
    # return send_from_directory(os.path.join(app.root_path, 'static/js'), path)
    return send_from_directory(app.static_folder + '/images', path)