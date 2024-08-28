from app import app #, db
#from app.models import User
from flask import jsonify, request, render_template
from user_agents import parse

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    user_agent = parse(request.headers.get('User-Agent'))
    #temp
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    #/temp
    if user_agent.is_pc:
        return render_template('web_index.html', title='Home', user=user, posts=posts)
    else:
        return render_template('mobile_index.html', title='Home', user=user)

"""@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'username': u.username, 'email': u.email} for u in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201"""