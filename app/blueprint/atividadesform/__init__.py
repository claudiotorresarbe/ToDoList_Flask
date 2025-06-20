from config.__db__ import *
from flask_wtf import FlaskForm
from wtforms import *
from flask import *

bp_atividadesform = Blueprint("bp_atividadesform",__name__,template_folder="templates")

class Atividades_wtf(FlaskForm):
    descricao = StringField('Descricao',[validators.data_required(),validators.length(min=1,max=250)])
    status = SelectField('Status',[validators.data_required(),validators.length(min=1,max=1)],choices=[('1','Ativo'),('0','Inativo')])
    submit = SubmitField('Salvar')
    
@bp_atividadesform.route("/atividadesform/<action>/<int:id>",methods=["GET","POST"])
@bp_atividadesform.route("/atividadesform/<action>/", defaults={"id": 0}, methods=["GET","POST"])
def atividadesform(action,id):

   #check if logged
   '''
   if "id" not in session:
      return redirect(url_for('bp_atividades.atividades'))
   '''
   form = Atividades_wtf()

   if action == 'create':
   
      disabled = False
      button = 'Salvar'

   elif action in('update','delete','info'):
      
      existe = Atividades.query.filter_by(id=id).first()
   
      if existe:

         form = Atividades_wtf(id=existe.id,descricao=existe.descricao,status=existe.status)

         if action == 'update' and id:
            
            disabled = False
            button = 'Alterar'

         elif action == 'delete' and id:

            disabled = True
            button = 'Apagar'
         
         elif action == 'info' and id:
            
            disabled = True
            button = None

      else:

         #alert
         error = ['danger','O registro não existe!']

         flash(error[0],error[1])

         return redirect(url_for('bp_atividades.atividades'))

   return render_template("atividadesform/index.html",form=form,action=action,id=id,disabled=disabled,button=button)
    
@bp_atividadesform.route("/atividadesform/create/commit",methods=["POST"])
def create():

   #get data of form
   form = Atividades_wtf(request.form)
   
   #check data
   if form.validate_on_submit():
      
      #write the inputs
      add = Atividades(descricao=form.descricao.data,status=form.status.data)
   
      #write inputs in the database
      db.session.add(add)
      db.session.commit()

      #alert
      error = ['success','Registro incluído!']

   else:

      #alert
      error = ['danger','Transação interrompida!']

   flash(error[0],error[1])
   
   return redirect(url_for('bp_atividades.atividades'))

@bp_atividadesform.route("/atividadesform/update/<int:id>/commit",methods=["POST"])
def update(id):

   #get data of form
   form = Atividades_wtf(request.form)
   
   if request.method == 'GET':
      print(request.args.get('action'))
   
   #check data
   if form.validate_on_submit():

      #check email in database
      existe = Atividades.query.filter_by(id=id).first()   
      
      #check condition
      if existe:
         existe.descricao = form.descricao.data
         existe.status = form.status.data
         db.session.commit()

      #alert
      error = ['success','Registro alterado!']

   else:

      #alert
      error = ['danger','Transação interrompida!']

   flash(error[0],error[1])

   return redirect(url_for('bp_atividades.atividades'))
    
@bp_atividadesform.route("/atividadesform/delete/<int:id>/commit",methods=["POST"])
def delete(id):

   #get data of form
   code = Atividades.query.get_or_404(id)
   
   #delete data
   db.session.delete(code)
   db.session.commit()

   #alert
   error = ['success','Registro apagado!']
   
   flash(error[0],error[1])
   
   return redirect(url_for('bp_atividades.atividades'))

@bp_atividadesform.route("/atividadesform/info/<int:id>/commit",methods=["POST"])
def info(id):

   pass
   
   return redirect(url_for('bp_atividades.atividades'))
    
    