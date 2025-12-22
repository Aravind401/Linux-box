from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "secret123"

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'enter'
app.config['MYSQL_DB'] = 'userdb'

mysql = MySQL(app)

# ---------------- LOGIN ----------------
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM login_users WHERE username=%s AND password=%s", (user, pwd))
        account = cur.fetchone()

        if account:
            session['loggedin'] = True
            return redirect('/home')
    return render_template('login.html')

# ---------------- HOME / LIST ----------------
@app.route('/home')
def home():
    if not session.get('loggedin'):
        return redirect('/')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return render_template('home.html', users=users)

# ---------------- CREATE ----------------
@app.route('/add', methods=['POST'])
def add():
    if not session.get('loggedin'):
        return redirect('/')
    data = (
        request.form['username'],
        request.form['dob'],
        request.form['email'],
        request.form['phone']
    )
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(username, dob, email, phone) VALUES(%s,%s,%s,%s)", data)
    mysql.connection.commit()
    return redirect('/home')

# ---------------- DELETE ----------------
@app.route('/delete/<int:id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id,))
    mysql.connection.commit()
    return redirect('/home')

# ---------------- UPDATE ----------------
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        data = (
            request.form['username'],
            request.form['dob'],
            request.form['email'],
            request.form['phone'],
            id
        )
        cur.execute("UPDATE users SET username=%s,dob=%s,email=%s,phone=%s WHERE id=%s", data)
        mysql.connection.commit()
        return redirect('/home')

    cur.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cur.fetchone()
    return render_template('edit.html', user=user)

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run()

