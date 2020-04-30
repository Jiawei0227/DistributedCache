# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: content_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import payload_pb2 as payload__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='content_service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x15\x63ontent_service.proto\x1a\rpayload.proto2X\n\x0e\x43ontentService\x12#\n\nsetContent\x12\x08.Request\x1a\t.Response(\x01\x12!\n\ngetContent\x12\x08.Request\x1a\t.Responseb\x06proto3'
  ,
  dependencies=[payload__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CONTENTSERVICE = _descriptor.ServiceDescriptor(
  name='ContentService',
  full_name='ContentService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=40,
  serialized_end=128,
  methods=[
  _descriptor.MethodDescriptor(
    name='setContent',
    full_name='ContentService.setContent',
    index=0,
    containing_service=None,
    input_type=payload__pb2._REQUEST,
    output_type=payload__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getContent',
    full_name='ContentService.getContent',
    index=1,
    containing_service=None,
    input_type=payload__pb2._REQUEST,
    output_type=payload__pb2._RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTENTSERVICE)

DESCRIPTOR.services_by_name['ContentService'] = _CONTENTSERVICE

# @@protoc_insertion_point(module_scope)
