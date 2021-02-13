from rest_api.app import *

@app.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    if request.method == 'POST':
        
        return redirect(url_for('logOut'))

    return render_template('home.html')

