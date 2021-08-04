from os import environ

class Config:

    ################### Global ###################

    ENV = environ.get("TOYBOX_AUTHZ_ENV","production")
    DEBUG = int(environ.get("TOYBOX_AUTHZ_DEBUG","0"))
    TESTING = environ.get("TOYBOX_AUTHZ_TESTING","0")
    SECRET_KEY = environ.get("TOYBOX_AUTHZ_SECRET_KEY","HARD_STRONG_SECRET_SECRET")
    JSONIFY_PRETTYPRINT_REGULAR = True


