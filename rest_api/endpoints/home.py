from rest_api.app import *

@app.route('/home/<username>', methods=['POST', 'GET'])
@login_required
def home(username):

    if request.method == 'POST':
        
        return redirect(url_for('logOut'))

    return render_template('home.html')

