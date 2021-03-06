## TODO: start up content server: Assignee: Jie
import logging
import os
import sys, time
from concurrent import futures
import grpc

sys.path.append(os.path.abspath("."))

from grpc_services import content_service_pb2_grpc
from grpc_services import payload_pb2
import constant

class ContentServer(content_service_pb2_grpc.ContentServiceServicer):
    def __init__(self):
        super().__init__()
        self.contentStore = {}

    def setContent(self, request, context):
        # get value from the requests
        logging.debug("Content Server set content for client ({0}) for url {1}".format(
            request.client_id, request.request_url))
        # append value in case it is too long
        self.contentStore[request.request_url] = request.data

        # make response
        response = payload_pb2.Response (
            status = payload_pb2.Response.StatusCode.OK
        )
        logging.debug("sleep 1 seconds before getting back")
        time.sleep(constant.CONTENT_POST_DELAY_SECOND)
        
        return response

    def getContent(self, request, context):
        logging.debug("Content Server get content for client ({0}) for url {1}".format(
            request.client_id, request.request_url))
        key = request.request_url
        if (key in self.contentStore):
            value = self.contentStore[key]
            response = payload_pb2.Response(
                status = payload_pb2.Response.StatusCode.OK,
                request_url = key,
                data = value
            )
        else:
            response = payload_pb2.Response(
                status = payload_pb2.Response.StatusCode.NO_SUCH_KEY_ERROR,
                request_url = key,
            )
        logging.debug("sleep 5 seconds before getting back")
        time.sleep(constant.CONTENT_GET_DELAY_SECOND)
        return response

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    content_service_pb2_grpc.add_ContentServiceServicer_to_server(ContentServer(), server)

    server.add_insecure_port(constant.PROJECT_DOMAIN + constant.CONTENT_SERVER_PORT)
    
    logging.debug("-----------------Start Content Server--------------")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=constant.PROJ_LOG_LEVEL)
    main()