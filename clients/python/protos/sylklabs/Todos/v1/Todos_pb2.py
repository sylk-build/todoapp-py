# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sylklabs/Todos/v1/Todos.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsylklabs/Todos/v1/Todos.proto\x12\x11sylklabs.Todos.v1\"D\n\x04Task\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04\x64one\x18\x04 \x01(\x08\"\x14\n\x06TaskId\x12\n\n\x02id\x18\x01 \x01(\t2L\n\x0bTaskService\x12=\n\x07GetTask\x12\x19.sylklabs.Todos.v1.TaskId\x1a\x17.sylklabs.Todos.v1.Taskb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sylklabs.Todos.v1.Todos_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_TASK']._serialized_start=52
  _globals['_TASK']._serialized_end=120
  _globals['_TASKID']._serialized_start=122
  _globals['_TASKID']._serialized_end=142
  _globals['_TASKSERVICE']._serialized_start=144
  _globals['_TASKSERVICE']._serialized_end=220
# @@protoc_insertion_point(module_scope)
