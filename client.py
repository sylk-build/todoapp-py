from clients.python import TaskService_v1
from clients.python.protos.sylklabs.Todos.v1.Todos_pb2 import TaskId
import grpc

client = TaskService_v1(
    client_opt={
        'host': 'localhost',
        'port': 51010
    }
)

try:
    task = client.GetTask(TaskId(id='1'))
    print(task)
# Custom handling of exceptions
except grpc.RpcError as rpc_error:
    if rpc_error.code() == grpc.StatusCode.NOT_FOUND:
        print(f"Received RPC error: code={rpc_error.code()} message={rpc_error.details()}")
    else:
        print(f"Received unknown RPC error: code={rpc_error.code()} message={rpc_error.details()}")