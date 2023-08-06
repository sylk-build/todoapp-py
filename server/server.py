"""sylk.build Generated Server Code"""
_ONE_DAY_IN_SECONDS = 60 * 60 * 24
from concurrent import futures
import time
import grpc
from services.protos.sylklabs.Todos.v1 import Todos_pb2_grpc as Todos_v1_pb2_grpc
from services.TaskService.v1.TaskService import TaskService as TaskService_v1

def serve(host="0.0.0.0:51010"):
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	Todos_v1_pb2_grpc.add_TaskServiceServicer_to_server(TaskService_v1(),server)
	server.add_insecure_port(host)
	server.start()
	print("[*] Started sylk.build server at -> %s" % (host))
	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop(0)

if __name__ == "__main__":
	serve()