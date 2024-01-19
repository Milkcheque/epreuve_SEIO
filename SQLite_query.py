import sqlite3

def get_db():
    """Connexion à la DB"""
    db = sqlite3.connect('./DB.db')
    return db

def clean_table(table:str):
    """Requête de suppression de toutes les données de la table"""
    db = get_db()
    db.cursor().execute("DELETE FROM "+table+";")
    db.commit()
    db.close()

def insert_user(id:str, mdp:str):
    """Requête d'insertion d'un nouvel utilisateur dans la table User"""
    db = get_db()
    query = 'INSERT INTO User VALUES("'+id+'","'+mdp+'");'
    db.cursor().execute(query)
    db.commit()
    db.close()

def verify_user_id(id:str):
    """
    Requête pour vérifier l'existence d'un utilisateur
       @return  True si l'utilisateur existe, False sinon
    """
    db = get_db()
    query = 'SELECT DISTINCT id FROM User WHERE id="'+id+'";'
    from_db_id = db.cursor().execute(query).fetchall()
    db.close()
    return True if len(from_db_id) else False

def verify_password(id:str, pwd:str):
    """
    Requête de vérification du mot de passe de l'utilisateur id
        @return  True si le mot de passe est correct, False sinon
    """
    db = get_db()
    query = 'SELECT DISTINCT password FROM User WHERE id="'+id+'";'
    from_db_pwd = db.cursor().execute(query).fetchall()
    db.commit()
    db.close()
    if len(from_db_pwd) == 0:
        return False
    return from_db_pwd[0][0] == pwd

def change_password(id:str, pwd:str):
    """Requête de changement de mot de passe pour l'utilisateur id"""
    db = get_db()
    query = 'UPDATE User SET password = "'+pwd+'" WHERE id = "'+id+'";'
    db.cursor().execute(query)
    db.commit()
    db.close()

def insert_website_component(id:str, content:str):
    """Requête d'insertion d'un nouveau composant de site web dans la table Website_component"""
    db = get_db()
    query = 'INSERT INTO Website_component VALUES("'+id+'","'+content+'");'
    db.cursor().execute(query)
    db.commit()
    db.close()

def get_website_component(id:str):
    """
    Requête de récupération d'un composant de site web
        @return  content le contenu du composant id
    """
    db = get_db()
    query = 'SELECT DISTINCT content FROM Website_component WHERE id="'+id+'";'
    content = db.cursor().execute(query).fetchall()
    db.close()
    return content[0][0]

def modify_tagline(content:str):
    """Requête de modification du slogan"""
    db = get_db()
    query = 'UPDATE Website_component SET content = "'+content+'" WHERE id = "tagline";'
    db.cursor().execute(query)
    db.commit()
    db.close()

