import sys, os

from easi_tools import notebook_utils
from datacube.utils.aws import configure_s3_access

def configure_nb_for_CAL():
    sys.path.append(os.path.expanduser('../../../../scripts'))

    cluster, client = notebook_utils.initialize_dask(use_gateway=False)
    os.environ['USE_PYGEOS'] = '0'

    configure_s3_access(aws_unsigned=False, requester_pays=True, client=client)
