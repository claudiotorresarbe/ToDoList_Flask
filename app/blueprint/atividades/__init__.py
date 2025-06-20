from config.__db__ import *
from flask import *

bp_atividades = Blueprint("bp_atividades",__name__,template_folder="templates")

@bp_atividades.route("/atividades/",methods=["GET","POST"])
def atividades():

   #check if logged
   '''
   if "id" not in session:
      return redirect(url_for('bp_signin.signin'))
   '''
   #rows per page
   row = 10

   #get
   if request.method != 'POST':
      search = request.args.get('search')
      page = request.args.get('page')
      #flash('danger','Preencha o campo!')

   #prepare value of search 
   if search:
      where = 'where id||descricao like "%'+search+'%"'
   else:
      where = ''

   #if page is null
   if page is None:
      page = 0

   #page actual
   page = int(page) * (0 if page == 0 else row)

   #prepare query to search
   qry = db.text(f"select id, descricao, case when status = 0 then 'I' else 'A' end from tb_atividades {where} order by id asc limit {row+1} offset {page}")

   #search
   data = list(db.session.execute(qry))

   #tratament of result
   if not isinstance(data,list):
      data = ''

   return render_template("atividades/index.html",data=data,row=row)
        