
import logging

from gorillaspy.web.api.util import create_actions_blueprint

# from .util import check_authentication, get_auth_data
from niponcred_api.model import Customer
from niponcred_api.config import API_VERSION

# actions = create_actions_blueprint(Customer, api_version=API_VERSION)

logger = logging.getLogger(__name__)


def create_api(api):
    api.create_api(Customer,
                   methods=['GET', 'POST'],
                   url_prefix='/%s' % API_VERSION,
                   results_per_page=10,
                   primary_key='id',
                   preprocessors={
                   },
                   postprocessors={
                   })