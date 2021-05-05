import pandas as pd
import numpy as np
import os
import re
from flask import Flask, render_template, request, jsonify
import Gatello_smart_matching


path0=os.path.abspath(os.path.dirname(__file__))
#file_0=os.path.join(path0, 'list_tag_key_500.joblib')
#file_1=os.path.join(path0, 'reg_log_saved.joblib')



from pyresparser import ResumeParser
app = Flask(__name__) # Creer app et charger les fonctionalités de Flask

# Home page
@app.route('/') 
def index():
    return render_template('index.html')
                                                    
@app.route('/smart_matching', methods=['POST'])
def smart_matching():
    
    # Appeler les Inputs de la page HTML dashboard
    question1 = request.form['question1']
    question2 = request.form['question2'] 
    link_resume = ''
    link_joboffer = ''
    if question1 and question2 is not None:
        link_joboffer = str(path0+'\/'+question1)
        link_resume = str(path0+'\/'+question2) 
        #link_resume=question
        dist_matching = Gatello_smart_matching.Gatello_smart_matching(link_joboffer,link_resume)
    #return jsonify(resume_parsing)
          
    return render_template('smart_matching.html', tags = dist_matching)
                  

if __name__== '__main__': #Executer directement
    app.run(debug=True, port=5000) #Lancer le serveur local (localhost/adresse ip 127.0.0.1)



