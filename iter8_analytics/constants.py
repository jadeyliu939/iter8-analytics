"""
Environment variables that control the iter8 analytics server
"""

ITER8_ANALYTICS_DEBUG_ENV = 'ITER8_ANALYTICS_DEBUG' # deprecated; used only by flask
ITER8_ANALYTICS_LOG_LEVEL_ENV = 'ITER8_ANALYTICS_LOG_LEVEL' # used by fastapi

ITER8_DATA_CAPTURE_MODE_ENV = 'ITER8_DATA_CAPTURE_MODE'

ITER8_REQUEST_COUNT = 'iter8_request_count' # special metric indicating num requests to a version

METRICS_BACKEND_DEFAULT_CONFIGFILE = 'config.yaml'
METRICS_BACKEND_CONFIGFILE_ENV = 'METRICS_BACKEND_CONFIGFILE'

LOG_LEVEL = 'logLevel'
LOG_LEVEL_DEFAULT_LEVEL = 'debug'

ANALYTICS_SERVICE_PORT = 'ANALYTICS_SERVICE_PORT'
ANALYTICS_SERVICE_DEFAULT_PORT = 8080
ANALYTICS_SERVICE_CONFIGFILE_PORT = 'port'
ANALYTICS_SERVICE_PORT_ENV = 'ITER8_ANALYTICS_SERVER_PORT'

METRICS_BACKEND_CONFIGFILE_URL = 'url'
METRICS_BACKEND_CONFIGFILE_AUTH = 'auth'
METRICS_BACKEND_URL_ENV = 'ITER8_ANALYTICS_METRICS_BACKEND_URL'

METRICS_BACKEND_CONFIG_METRICS_BACKEND = 'metricsBackend'
METRICS_BACKEND_CONFIG_URL = 'url'
METRICS_BACKEND_CONFIG_DEFAULT_URL = "http://prometheus.istio-system:9090"
METRICS_BACKEND_CONFIG_TYPE = 'type'
METRICS_BACKEND_CONFIG_TYPE_PROMETHEUS = 'prometheus'
METRICS_BACKEND_CONFIG_AUTH = 'auth'
METRICS_BACKEND_CONFIG_AUTH_TYPE = 'type'
METRICS_BACKEND_CONFIG_AUTH_TYPE_NONE = 'none'
METRICS_BACKEND_CONFIG_AUTH_TYPE_BASIC = 'basic'
METRICS_BACKEND_CONFIG_AUTH_USERNAME = 'username'
METRICS_BACKEND_CONFIG_AUTH_PASSWORD = 'password'
METRICS_BACKEND_CONFIG_AUTH_CA_FILE = 'ca_file'
METRICS_BACKEND_CONFIG_AUTH_TOKEN = 'token'
METRICS_BACKEND_CONFIG_AUTH_INSECURE_SKIP_VERIFY = 'insecure_skip_verify'