import logging
import os
import sys
from concurrent import futures

import grpc

sys.path.append(os.path.abspath("."))
from grpc_services import membership_pb2, membership_pb2_grpc

class MembershipManager(membership_pb2_grpc.MembershipManagementServicer):
    def SendHeartBeat(self, request, context):
        """Send heartbeat
        A client to server function call
        """
        print("Get heartbeat message: ({0})".format(request))
        return membership_pb2.ResultMsg(succeed=True, msg="Msg received")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    membership_pb2_grpc.add_MembershipManagementServicer_to_server(
        MembershipManager(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
