from flask import Flask, session, redirect, url_for, escape, request, render_template
from simplepam import authenticate



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
#    if 'username' in session:
#        return 'Logged in as %s' % escape(session['username'])
#    return 'You are not logged in'
    if request.method == 'POST':
        username = request.args.get('uname')
        password = request.args.get('pwd')
        if authenticate(str(username), str(password)):
            session['username'] = request.args.get('uname')
# deprecated            render_template('sassy.html', item = escape(session['username']))
            return 'loginSuccess'
        return 'loginFailure'
    else:
        if 'username' in session:
            return render_template('loggedHeader.html', item = escape(session['username']))
        return render_template('index.html')



@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(port=4200,debug='True')