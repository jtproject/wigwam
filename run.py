from xyz import build

_A = build()

if __name__ == '__main__':
    _A.config['SECRET_KEY'] = 'hjgkkjghjgjgkjgjgh'
    _A.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///the.db'
    _A.run(debug=True)