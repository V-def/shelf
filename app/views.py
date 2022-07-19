from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
app.config.from_object('config')

# Main pages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/')
def search():
    return render_template('search.html')

# Errors

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_message="Mince ! La page que vous avez cherché n'existe pas...", error_log=e)

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html', error_message="Mince ! Il y a eu une erreur interne...", error_log=e)

# PWA

@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('js/sw.js')
