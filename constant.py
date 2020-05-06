import os
import sys

sys.path.append(os.path.abspath("."))
from grpc_services import payload_pb2
import logging

# PORT
PROJECT_DOMAIN = '[::]:'
CONTENT_SERVER_PORT = '50052'

MASTER_SERVER_ID = 0
CONTENT_SERVER_ID = 1

HEARTBEAT_PORT = '50051'
HEARTBEAT_TIMEOUT = 10

CACHE_SERVICE_PORT_START = 50055

# Content server related
CONTENT_GET_DELAY_SECOND = 0
CONTENT_POST_DELAY_SECOND = 0

# feature
LEASE_MODE = True

# Error code
NO_SUCH_KEY_ERROR = 1
CONNECTION_CONTENT_SERVER_FAILED = 1000
CONNECTION_CACHE_SERVER_FAILED = 1001
NO_AVAILABLE_CACHE_SERVER = 1002

# Cache server related
CACHE_SIZE = 700
CACHE_TOKEN_RATE_LIMITER = 10
MASTER_NO_LEASE_RETRY_TIME = 1

STATUS_MAP = {
    0 : "Succeed",
    1 : "NO_SUCH_KEY_ERROR",
    2 : "CACHE_MISS",
    3 : "CACHE_HIT",
    4 : "FAILED",
    1000: "CONNECTION_CONTENT_SERVER_FAILED",
    1001: "CONNECTION_CACHE_SERVER_FAILED",
    1002: "NO_AVAILABLE_CACHE_SERVER",
}

STATUS_CODE = payload_pb2.Response.StatusCode

def getCacheServerAddr(cache_server_id):
    return PROJECT_DOMAIN + str(CACHE_SERVICE_PORT_START + cache_server_id)


PROJ_LOG_LEVEL = logging.INFO