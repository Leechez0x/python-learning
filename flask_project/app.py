from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = 'Leechez Ogo!'
    skills = ['Python', 'Pandas', 'Numpy', 'Flask']
    return render_template('home.html', name = name, skills = skills)

@app.route('/about')
def about():
    return 'About Page'

if __name__ == '__main__':
    app.run(debug =True)