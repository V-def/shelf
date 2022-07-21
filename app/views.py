from flask import Blueprint, render_template, request, url_for, redirect, flash

main = Blueprint('main', __name__, static_folder='static')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/search/')
def search_page():
    return render_template('search.html')

# Errors

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_message="Mince ! La page que vous avez cherché n'existe pas...", error_log=e)

@main.app_errorhandler(500)
def page_not_found(e):
    return render_template('error.html', error_message="Mince ! Il y a eu une erreur interne...", error_log=e)

# PWA

@main.route('/sw.js', methods=['GET'])
def sw():
    return main.send_static_file('js/sw.js')

