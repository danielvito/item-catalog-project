from app import db, ma
from datetime import datetime
from sqlalchemy import asc
from marshmallow import Schema, fields


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    picture = db.Column(db.String(250))

    def __repr__(self):
        return '<User {}>'.format(self.name + ',' + self.email + ',' + str(self.id))  # noqa

    def get_by_id(id):
        return User.query.filter_by(id=id).one_or_none()

    def get_by_email(email):
        return User.query.filter_by(email=email).one_or_none()

    def check_new_user(name, email, picture):
        user = User.get_by_email(email)
        if user is not None:
            return user
        user = User(name=name, email=email, picture=picture)
        db.session.add(user)
        db.session.commit()
        return user


class Brand(db.Model):
    __tablename__ = 'brand'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)

    def __repr__(self):
        return '<Brand {}>'.format(self.name)

    def get_by_id(id):
        return Brand.query.filter_by(id=id).one_or_none()


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)

    def __repr__(self):
        return '<Category {}>'.format(self.name)

    def list_categories():
        return Category.query.all()

    def get_by_id(id):
        return Category.query.filter_by(id=id).one_or_none()


class CategoryItem(db.Model):
    __tablename__ = 'category_item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    price = db.Column(db.String(16))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
                               backref=db.backref("items", lazy="dynamic"))
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    brand = db.relationship(Brand)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)

    def __repr__(self):
        return '<CategoryItem {}>'.format(self.name + ', user_id: ' + str(self.user_id))  # noqa

    def list_category_items_by_category(category_id):
        return CategoryItem.query \
            .filter_by(category_id=category_id)  \
            .order_by(asc(CategoryItem.name))

    def by_id(id):
        return CategoryItem.query.filter_by(id=id).one_or_none()


class CategorySchema(ma.ModelSchema):
    items = fields.Nested('CategoryItemSchema', many=True,
                          exclude=('category', 'user', ))

    class Meta:
        model = Category


class CategoryItemSchema(ma.ModelSchema):
    brand = fields.Nested('BrandSchema')

    class Meta:
        model = CategoryItem


class BrandSchema(ma.ModelSchema):
    class Meta:
        model = Brand
