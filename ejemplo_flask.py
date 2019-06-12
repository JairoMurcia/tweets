# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:35:06 2019

@author: Estudiantes
"""

from flask import Flask
from flask import render_template


app=Flask(__name__)

@app.route('/')

def saludar():
    return render_template('holamundo.html')

if __name__=='__main__':
    app.run(port=5000,debug=True)