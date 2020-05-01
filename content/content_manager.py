import logging
import os
import sys

import grpc

sys.path.append(os.path.abspath("."))
from grpc_services import membership_pb2, membership_pb2_grpc
from grpc_services import content_service_pb2_grpc
from grpc_services import payload_pb2
import constant

## This class should extends XXXServicer generated by proto
class ContentManager():
    def __init__(self):
        self.channel = grpc.insecure_channel(constant.PROJECT_DOMAIN + constant.CONTENT_SERVER_PORT)
        self.stub = content_service_pb2_grpc.ContentServiceStub(self.channel)
    
    def getContent(self, key, server_id):
        request = payload_pb2.Request(client_id=server_id, request_url=key)
        resMsg = self.stub.getContent(request)
        return resMsg

    def setContent(self, key, value, server_id):
        request = payload_pb2.Request(client_id=server_id, request_url=key, data=value)
        resMsg = self.stub.setContent(iter([request]))
        return resMsg