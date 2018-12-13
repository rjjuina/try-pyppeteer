import os
import time
import yaml
import logging.config

from functools import wraps


def get_logger(name):
    with open(os.path.join(os.path.dirname(__file__), 'logging_config/logging.yaml')) as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    logger = logging.getLogger(name)
    logger.setLevel('INFO')

    return logger


utils_logger = get_logger(__name__)


def write_html(page_source, filename, path=os.path.join(os.path.dirname(__file__), os.pardir, 'report/html')):
    html_dir = os.path.join(os.path.dirname(__file__), path)
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)

    with open(os.path.join(html_dir, filename), 'w', encoding='utf8') as outfile:
        outfile.write(page_source)


def profile_time(method):
    @wraps(method)
    def _impl(*method_args, **method_kwargs):
        start = time.time()
        result = method(*method_args, **method_kwargs)
        end = time.time()
        utils_logger.info("method:%s, duration: %f" % (method.__name__, end - start))
        return result

    return _impl
