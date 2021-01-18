from app import app, db
from app.models import Platform, Game, Tag


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Platform': Platform, 'Game': Game, 'Tag': Tag}
