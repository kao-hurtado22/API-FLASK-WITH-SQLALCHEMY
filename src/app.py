from flask import Flask, jsonify, request, render_template
from flask_migrate import Migrate
from models import db, Contact

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = "dialect+driver://user:pass@host:port/dbname" # MySQL, Oracle, Postgresql, SQlite
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/contacts', methods=['GET'])
def get_contact():
    contacts = Contact.query.all() # [<Contact>, <Contact>, <Contact>]
    contacts = list(map(lambda contact: contact.serialize(), contacts)) # [{"id": 1}, {"id": 2}]
    return jsonify(contacts), 200

@app.route('/contacts/<int:id>', methods=['GET'])
def get_contact_by_id(id):
    contact = Contact.query.get(id)
    return jsonify(contact.serialize()), 200

@app.route('/contacts', methods=['POST'])
def create_contact():
    name = request.json.get('name')
    email = request.json.get('email')
    phone = request.json.get('phone')

    """ 
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone'] 
    """

    contact = Contact()
    contact.name = name
    contact.email = email
    contact.phone = phone

    db.session.add(contact)
    db.session.commit()

    return jsonify(contact.serialize()), 201

@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    name = request.json.get('name')
    email = request.json.get('email')
    phone = request.json.get('phone')

    """ 
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone'] 
    """

    contact = Contact.query.get(id)
    contact.name = name
    contact.email = email
    contact.phone = phone

    db.session.commit()

    return jsonify(contact.serialize()), 200

@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    return jsonify({}), 200



if __name__ == '__main__':
    app.run()