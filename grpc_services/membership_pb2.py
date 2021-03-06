# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: membership.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='membership.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10membership.proto\"I\n\tHeartBeat\x12\x15\n\rcacheServerId\x18\x01 \x01(\t\x12\x13\n\x0bmemoryUsage\x18\x02 \x01(\t\x12\x10\n\x08\x63puUsage\x18\x03 \x01(\t\"h\n\tResultMsg\x12%\n\x06status\x18\x01 \x01(\x0e\x32\x15.ResultMsg.StatusCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\"\'\n\nStatusCode\x12\r\n\tSUCCEEDED\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x32\x41\n\x14MembershipManagement\x12)\n\rSendHeartBeat\x12\n.HeartBeat\x1a\n.ResultMsg\"\x00\x62\x06proto3'
)



_RESULTMSG_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='ResultMsg.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=160,
  serialized_end=199,
)
_sym_db.RegisterEnumDescriptor(_RESULTMSG_STATUSCODE)


_HEARTBEAT = _descriptor.Descriptor(
  name='HeartBeat',
  full_name='HeartBeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cacheServerId', full_name='HeartBeat.cacheServerId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memoryUsage', full_name='HeartBeat.memoryUsage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpuUsage', full_name='HeartBeat.cpuUsage', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=93,
)


_RESULTMSG = _descriptor.Descriptor(
  name='ResultMsg',
  full_name='ResultMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ResultMsg.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='ResultMsg.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESULTMSG_STATUSCODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=199,
)

_RESULTMSG.fields_by_name['status'].enum_type = _RESULTMSG_STATUSCODE
_RESULTMSG_STATUSCODE.containing_type = _RESULTMSG
DESCRIPTOR.message_types_by_name['HeartBeat'] = _HEARTBEAT
DESCRIPTOR.message_types_by_name['ResultMsg'] = _RESULTMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HeartBeat = _reflection.GeneratedProtocolMessageType('HeartBeat', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEAT,
  '__module__' : 'membership_pb2'
  # @@protoc_insertion_point(class_scope:HeartBeat)
  })
_sym_db.RegisterMessage(HeartBeat)

ResultMsg = _reflection.GeneratedProtocolMessageType('ResultMsg', (_message.Message,), {
  'DESCRIPTOR' : _RESULTMSG,
  '__module__' : 'membership_pb2'
  # @@protoc_insertion_point(class_scope:ResultMsg)
  })
_sym_db.RegisterMessage(ResultMsg)



_MEMBERSHIPMANAGEMENT = _descriptor.ServiceDescriptor(
  name='MembershipManagement',
  full_name='MembershipManagement',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=201,
  serialized_end=266,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendHeartBeat',
    full_name='MembershipManagement.SendHeartBeat',
    index=0,
    containing_service=None,
    input_type=_HEARTBEAT,
    output_type=_RESULTMSG,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MEMBERSHIPMANAGEMENT)

DESCRIPTOR.services_by_name['MembershipManagement'] = _MEMBERSHIPMANAGEMENT

# @@protoc_insertion_point(module_scope)
