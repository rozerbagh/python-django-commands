from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from flaskr.db import get_db

blogModule = Blueprint("blog", __name__, url_prefix="/blog")


@blogModule.route("/get/all", methods=("GET"))
def get_all():
    if request.method == "GET":
        db = get_db()
        params = request.args
