"""sylk.build service implemantation for -> TaskService"""
import grpc
from google.protobuf.timestamp_pb2 import Timestamp
from typing import Iterator
from services.protos.sylklabs.Todos.v1 import Todos_pb2_grpc, Todos_pb2

class TaskService(Todos_pb2_grpc.TaskServiceServicer):

	def __init__(self) -> None:
		self.tasks = [
			Todos_pb2.Task(
				id='1',
				title='Build App',
				description='Create a distributed system with sylk.build',
				done=True,
			),
			Todos_pb2.Task(
				id='2',
				title='Implement AI Chatbot',
				description='Build an AI-powered chatbot using Python and TensorFlow',
				done=False,
			),
			Todos_pb2.Task(
				id='3',
				title='Optimize Database Queries',
				description='Improve the performance of database queries for faster application response',
				done=False,
			),
		]


	# @rpc @@sylk - DO NOT REMOVE
	def GetTask(self, request: Todos_pb2.TaskId, context: grpc.ServicerContext) -> Todos_pb2.Task:
		print('[GetTask] Got request for task data: %s' % request.id)
		response = next((t for t in self.tasks if t.id == request.id),None)
		if response is not None:
			return response
		else:
			context.set_code(grpc.StatusCode.NOT_FOUND)
			context.set_details(f'Task by id: "{request.id}" not found.')
			return context
