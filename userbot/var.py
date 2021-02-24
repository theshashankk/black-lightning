import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from localconfig import Var as config
else:
    from heroku_config import config


Var = config
