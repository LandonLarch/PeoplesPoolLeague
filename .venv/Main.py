# Reminder: Consider moving this file out of the .venv folder (reserved for virtual environment packages).
from flask import Flask
from decouple import config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
app.config['SECRET_KEY'] = config('SECRET_KEY')
app.config['ENV']        = config('FLASK_ENV', default='production')

@app.route('/')
def hello():
    return 'Hello, Pool League!'

if __name__ == '__main__':
    app.run(debug=True)
