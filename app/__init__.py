from flask import Flask, render_template
from . import portfolio

def create_app(environ=None, start_response=None):
    app = Flask(__name__)

    from. import portfolio

    app.register_blueprint(portfolio.bp)



    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app
