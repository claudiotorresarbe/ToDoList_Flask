from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Example(db.Model):
   __tablename__ = 'TB_EXAMPLE'
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   email = db.Column(db.String(250), nullable=False)
   status = db.Column(db.Integer, nullable=False)

class Login(db.Model):
   __tablename__ = 'TB_LOGIN'
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   email = db.Column(db.String(250), nullable=False)
   senha = db.Column(db.String(250), nullable=False)
   token = db.Column(db.String(250), nullable=False)
   dtinclusao = db.Column(db.DateTime, nullable=False)
   usrinclusao = db.Column(db.String(250), nullable=False)
   dtalteracao = db.Column(db.DateTime, nullable=True)
   usralteracao = db.Column(db.String(250), nullable=True)
   status = db.Column(db.Integer, nullable=False)

class Newsletter(db.Model):
   __tablename__ = 'TB_NEWSLETTER'
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   email = db.Column(db.String(250), nullable=False)
   dtinclusao = db.Column(db.DateTime, nullable=False)
   usrinclusao = db.Column(db.String(250), nullable=False)
   dtalteracao = db.Column(db.DateTime, nullable=True)
   usralteracao = db.Column(db.String(250), nullable=True)
   status = db.Column(db.Integer, nullable=False)

class Atividades(db.Model):
   __tablename__ = 'TB_ATIVIDADES'
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   descricao = db.Column(db.String(250), nullable=False)
   status = db.Column(db.Integer, nullable=False)