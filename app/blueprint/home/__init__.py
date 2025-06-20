from config.__db__ import *
from config.__utils__ import *
from config.__rate_limiter__ import rate_limiter
from flask_wtf import FlaskForm
from datetime import *
from wtforms import *
from flask import *

# Criação do Blueprint
bp_home = Blueprint("bp_home",__name__,template_folder="templates")

# Definição do form
class Newsletter_wtf(FlaskForm):
    email = StringField('Email',[validators.data_required(),validators.length(min=1,max=250)])
    submit = SubmitField('Inscrever-se')

# Rota do home
@bp_home.route("/",methods=["GET","POST"])
def home():

   #check if logged
   '''
   if "id" in session:
      return redirect('/signin')
   '''
   #post
   #if request.method == 'POST':
      #email = request.form['email']
      #flash('danger','Preencha o campo!')

   form1 = Newsletter_wtf()

   return redirect(url_for('bp_atividades.atividades'))
   return render_template("home/index.html",form1=form1)

# Rota da newsletter
@bp_home.route("/home/newsletter",methods=["GET","POST"])
@rate_limiter(limit=3, window=60, message="Número de tentativas excedido!",page="bp_home.home")
def newsletter():

   #get data of form
   form = Newsletter_wtf(request.form)

   #check data
   if form.validate_on_submit():
      
      #check if exist
      if validar_email(form.email.data):

         #check email in database
         existe = Newsletter.query.filter_by(email=form.email.data).first()

         #check condition
         if existe:

            #alert
            error = ['danger','Email já cadastrado!']

         else:

            add = Newsletter(email=form.email.data,status=1,dtinclusao=datetime.now(),usrinclusao='user')
            db.session.add(add)
            db.session.commit()

            #alert
            error = ['success','Cadastro feito!']

      else:

         #alert
         error = ['danger','Email inválido!']

   else:

      #alert
      error = ['danger','Transação interrompida!']

   flash(error[0],error[1])

   return redirect(url_for("bp_home.home"))
    