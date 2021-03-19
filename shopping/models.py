import shopping
from wtforms import form
from flask import render_template, url_for, flash, redirect,request, session
from shopping.forms import ContactForm
from shopping import app, mysql
import MySQLdb.cursors 



class footer():
  def footer():
    contact = ContactForm()
    if request.method == 'POST': 
      name = request.form['name']
      email = request.form['email'] 
      phone = request.form['phone']
      message = request.form['message']
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
      cursor.execute('INSERT INTO contact VALUES (NULL, % s, % s, % s,%s)', (name,email,phone,message))  
      mysql.connection.commit() 
      cursor.close()
      msg = 'Your message successfully delivered !'
    return contact
