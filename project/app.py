import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from project.oauth import oauth

oauth = oauth()