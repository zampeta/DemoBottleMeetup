import bottle
import os


@bottle.route('/static/<directory>/<filename>')
def server_static(directory, filename):
    root = os.path.join(os.getcwd(), 'static', directory)
    return bottle.static_file(filename, root=root)

@bottle.route('/')
def index():
    return bottle.template('index', page='index')

@bottle.route('/about')
def about():
    return bottle.template('about', page='about')

@bottle.get('/blog')
def blog():
    with get_dao() as data_access_object:
        posts = data_access_object.select()
    return bottle.template('blog', posts=posts, page='blog')

def get_dao():
    import dao
    return dao.MockDataAccessObject()

@bottle.get('/post')
def new_entry():
    return bottle.template('post', page='post')


@bottle.post('/blog')
def add_entry():
    import datetime
    data = dict()
    data['TITLE'] = bottle.request.forms.get('title')
    data['AUTHOR'] = bottle.request.forms.get('author')
    data['CONTENT'] = bottle.request.forms.get('content')
    data['POST_DATE'] = datetime.datetime.now()

    with get_dao() as data_access_object:
        data_access_object.insert(data)
    # do stuff
    return blog()

application = bottle.default_app()
application.run()
