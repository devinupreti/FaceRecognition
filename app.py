from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/login/', methods=["GET", "POST"])
def login():
    return render_template('login.html')


@app.route('/profile/')
def profile():
    return render_template('profile.html')


@app.route('/devin/', methods=['GET', 'POST'])
def devin():
    error = ''
    if request.method == 'POST':
        if request.form['username'] != 'nkashyap' or request.form['password'] != 'nkashyap':
            error = 'Invalid Credentials, Please Try Again!'
        else:
            return redirect(url_for('devin2'))

    return render_template("devin.html", error=error)


@app.route('/devin2/')
def devin2():
    return render_template("devin2.html")


if __name__ == "__main__":
    app.run(debug=True)