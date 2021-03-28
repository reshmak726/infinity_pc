from datetime import datetime
from math import degrees
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from shopping import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', '{self.phone}')"

class Contact(db.Model, UserMixin):
    __tablename__ = 'Contact'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(5000), nullable=False)

    def __repr__(self):
        return f"Contact('{self.username}', '{self.email}','{self.phone}', '{self.message}')"

class Category(db.Model, UserMixin):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True)
    category_name=db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return f"Category('{self.id}', '{self.category_name}')"

class SubCategory(db.Model,UserMixin):
    __tablename__ = 'SubCategory'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id') ,nullable=False)
    subcategory_name=db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"SubCategory('{self.id}', '{self.category_id}','{self.subcategory_name}')"

class Product(db.Model, UserMixin):
    __tablename__ = 'Product'
    id = db.Column(db.Integer,primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id') ,nullable=False)
    subcategory_id = db.Column(db.Integer, db.ForeignKey('SubCategory.id') ,nullable=False)
    name = db.Column(db.String(120), nullable=False)
    des = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(20), nullable=False, default='default.jpg')
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Product('{self.id}', '{self.subcategory_id}','{self.name}', '{self.des}',, '{self.img}', '{self.price}')"

class cart_items(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.phone}', '{self.message}')"