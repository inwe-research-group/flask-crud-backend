from flask import Blueprint, request, jsonify, redirect, url_for
from models.contact import Contact
from utils.db import db
contacts = Blueprint('contacts',__name__)

@contacts.route('/')
def index():
    contactos=Contact.query.all()        
    return jsonify(contactos)      

@contacts.route('/new', methods=['POST'])
def insert():
    body        =   request.get_json()    
    fullname    =   body['fullname']
    email       =   body['email']
    phone       =   body['phone']
    
    new_contact=Contact(fullname,email,phone)
    db.session.add(new_contact)
    db.session.commit()
    return redirect(url_for('contacts.index'))   

@contacts.route('/update', methods=['POST','GET'])
def update():
    body      = request.get_json()
    id        = body['id']
    contacto=Contact.query.get(id)
    if request.method == "POST":        
        contacto.fullname   =body['fullname']
        contacto.email      =body['email']
        contacto.phone      =body['phone']
        db.session.commit()         
        return redirect(url_for('contacts.index'))              
    return jsonify(contacto) 

@contacts.route('/delete')
def delete():
    body      = request.get_json()
    id        = body['id']
    contacto=Contact.query.get(id)
    db.session.delete(contacto)
    db.session.commit()     
    return redirect(url_for('contacts.index'))   

    
