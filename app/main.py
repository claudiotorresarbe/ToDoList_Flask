from config.__db__ import *
from flask_wtf.csrf import CSRFProtect
from flask import *

from blueprint.atividades import bp_atividades
from blueprint.atividadesform import bp_atividadesform
from blueprint.home import bp_home

app = Flask(__name__)
app.config.from_pyfile('./config/__config__.py')
csrf = CSRFProtect(app)
db.init_app(app)

app.register_blueprint(bp_atividades)
app.register_blueprint(bp_atividadesform)
app.register_blueprint(bp_home)

@app.errorhandler(404)
def error(e):
   return redirect("/")

@app.route('/signout')
def signout():
    session.pop('id', None)
    return redirect('/signin')

if __name__ == "__main__":
   with app.app_context():
      db.create_all()
   app.run(host="0.0.0.0",port=3000,debug=True)
    