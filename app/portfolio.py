from flask import Flask, Blueprint, render_template, send_file

bp = Blueprint('portfolio', __name__, url_prefix="/")

@bp.route("/", methods=['GET'])
def index():
    return render_template('portfolio/index.html')

@bp.route("/blog", methods=['GET'])
def blog():
    return render_template('portfolio/blogs.html')

@bp.route("/projects", methods=['GET'])
def projects():
    return render_template('portfolio/projects.html')

#=========================================================================
@app.route("/log-prerender", methods=["POST"])
def log_prerender():
    app.logger.info("Detected a possible prerender/preload!")
    return ("", 200)

@app.route("/log-foreground", methods=["POST"])
def log_foreground():
    app.logger.info("Page is now fully visible (real visit).")
    return ("", 200)
#=========================================================================
# Example for favicon route
@bp.route('/favicon.ico', methods=['GET'])
def favicon():
    return '', 204  # You can adjust this to return an actual favicon if needed

@bp.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Blogs

@bp.route("/ETL-Pipeline", methods=['GET'])
def etlpipeline():
    return render_template('portfolio/blogs/ETL-pipeline.html')
