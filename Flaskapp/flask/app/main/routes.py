from flask import Blueprint, render_template, request
import requests
import json
import redis

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/about")
def about():
    return render_template('about.html', title='About')






