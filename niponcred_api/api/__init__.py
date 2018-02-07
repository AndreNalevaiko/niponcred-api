import logging
from urllib.parse import urlparse

from flask import Flask
from flask_cors import CORS
from flask_restless.manager import APIManager


from flask_health.factory import HealthFactory
from flask_health.manager import ApiHealthManager
from gorillaspy.health.metrics.http import HTTPHealthMetric
from gorillaspy.logging import config_base_logger
from gorillaspy.web.api.util import exception_handler, DefaultJSONEncoder
from niponcred_api import config, db
from niponcred_api.api import customer, phone, uf, bank_receive

LOGGER = logging.getLogger(__name__)

#
# def create_custom_actions(flask_app):
#     flask_app.register_blueprint(customer.actions)
#     flask_app.register_blueprint(phone.actions)


def create_apis(api):
    customer.create_api(api)
    phone.create_api(api)
    uf.create_api(api)
    bank_receive.create_api(api)


config_base_logger()

app = Flask(__name__, static_folder="../static", template_folder="../templates")

app.json_encoder = DefaultJSONEncoder

app.config.from_object(config)

app.register_error_handler(Exception, exception_handler)

LOGGER.info('Configurado Flask')

CORS(app)

LOGGER.info("Configurado Ext Flask CORS")

db.init_app(app)

LOGGER.info('Configurado Extensão Flask SQLAlchemy')

api = APIManager(app=app, flask_sqlalchemy_db=db)

create_apis(api)

LOGGER.info('Configurado Ext Flask Restless')

# create_custom_actions(app)
#
# LOGGER.info('Configurado Blueprints do Flask')

health = ApiHealthManager()

health.init_app(app)

health_factory = HealthFactory(app.config)

health.registry(health_factory.get_mysql_metric(mandatory=True))
health.registry(health_factory.get_alembic_metric())
health.registry(HTTPHealthMetric(
    urlparse(app.config.get('DEAL_APP_WEB_URL')).hostname,
    port=urlparse(app.config.get('DEAL_APP_WEB_URL')).port,
    ssl=urlparse(app.config.get('DEAL_APP_WEB_URL')).scheme == 'https'))
health.registry(HTTPHealthMetric(
    urlparse(app.config.get('APP_WEB_URL')).hostname,
    port=urlparse(app.config.get('APP_WEB_URL')).port,
    ssl=urlparse(app.config.get('APP_WEB_URL')).scheme == 'https'))

LOGGER.info("Configurado o health status do API")

