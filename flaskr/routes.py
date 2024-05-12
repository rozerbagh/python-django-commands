from markupsafe import escape

def init_routes(app):
    @app.route('/')
    @app.route('/index')
    def index():
        return "Hello, World!"

    @app.route('/projects')
    def projects():
        return 'The project page'

    @app.route('/about')
    def about():
        return 'The about page'

    @app.route('/login')
    def login():
        return 'login'

    @app.route('/user/<username>')
    def profile(username):
        return f'{username}\'s profile'

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # show the post with the given id, the id is an integer
        return f'Post {post_id}'
