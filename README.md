# todoapp-py

This project has been generated thanks to [```sylk.build```](https://www.sylk.build) !

This project is using gRPC as main code generator and utilize HTTP2 + protobuf protocols for communication.

# Index
Usage:
- [Python](#python)

Resources:
- [TaskService](#taskservice)
- [Todos](#todos)

# Services

## TaskService

__`GetTask`__ [Unary]
- Input: [sylklabs.Todos.v1.TaskId](#taskid)
- Output: [sylklabs.Todos.v1.Task](#task)

# Packages

## `sylklabs.Todos.v1`


<details id="#Task">
<summary><b>Task</b></summary>

### __Task__
: 
* __id__ [TYPE_STRING]


* __title__ [TYPE_STRING]


* __description__ [TYPE_STRING]


* __done__ [TYPE_BOOL]

</details>


<details id="#TaskId">
<summary><b>TaskId</b></summary>

### __TaskId__
: 
* __id__ [TYPE_STRING]

</details>


# Usage

This project supports clients communication in the following languages:

### Python

```py
from clients.python import todoapppy

client = todoapppy()

# Unary call
response = stub.<Unary>(<InMessage>())
print(response)

# Server stream
responses = stub.<ServerStream>(<InMessage>())
for res in responses:
	print(res)

# Client Stream
requests = iter([<InMessage>(),<InMessage>()])
response = client.<ClientStream>(requests)
print(response)

# Bidi Stream
responses = client.<BidiStream>(requests)
for res in responses:
	print(res)
```


* * *
__This project and README file has been created thanks to [sylk.build](https://www.sylk.build)__