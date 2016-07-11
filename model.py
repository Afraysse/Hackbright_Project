""" 
OpenBook 2.0 uses SQLAlchemy and PostgreSQL to store and query user and 
site information. 

"""

from flask_sqlalchemy import SQLAlchemy

import datetime

# search engines uses the library SQLAlchemy-searchable 

from SQLAlchemy-searchable import make_searchable
from sqlalchemy_utils.types import TSVectorType  

db = SQLAlchemy()

make_searchable()

############################################################