from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = 'Leechez Ogo!'
    age = 20
    skills = ['Python', 'Pandas', 'Numpy', 'Flask']
    return render_template('home.html', name = name, age = age, skills = skills)

@app.route('/about')
def about():
    return  render_template('about.html')

if __name__ == '__main__':
    app.run(debug =True)