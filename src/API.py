from flask import Flask, request, make_response
from functools import wraps
from auth import authenticate

app = Flask(__name__)

def auth_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
#going to call authrize function here and call ffor vaild usernames and passwords
        auth = request.authorization
        if auth and authenticate(auth.username, auth.password):
            return f(*args, **kwargs)
        
        return make_response('Could not verify your login.', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    
    return decorated
@app.route('/')
def index():
    auth = request.authorization
    if auth and auth.username == 'username' and auth.password == 'password':
        return '<h1>You are Logged in!<h1>'
    
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

@app.route('/page')
@auth_required
def page():
    return '<h1> You are on the page!<h1>'
@app.route('/otherpage')
@auth_required
def otherpage():
    return '<h1>you are on the other page<h1>'

if __name__ == '__main__':
    app.run(debug=True)