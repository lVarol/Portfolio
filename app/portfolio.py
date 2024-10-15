from flask import Flask, Blueprint, render_template, send_file


bp = Blueprint('portfolio',__name__,url_prefix="/")

@bp.route("/", methods=['GET'])
def index():
    return render_template('portfolio/index.html')

@bp.route("/blog", methods=['GET'])
def blog():
    return render_template('portfolio/blogs.html')

@bp.route("/projects",methods=['GET'])
def projects():
    return render_template('portfolio/projects.html')

from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.png', mimetype='image/png')


@bp.errorhandler(404)
def page_not_found():
    return render_template('404.html')
