# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: address_server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='address_server.proto',
  package='address_server',
  serialized_pb=_b('\n\x14\x61\x64\x64ress_server.proto\x12\x0e\x61\x64\x64ress_server\"\x80\x02\n\x16\x61\x64\x64ress_server_message\x12\x0b\n\x03uid\x18\x01 \x01(\x0c\x12\x41\n\x04type\x18\x02 \x01(\x0e\x32\x33.address_server.address_server_message.message_type\x12\x12\n\x07network\x18\x03 \x01(\r:\x01\x31\x12\x17\n\x0foffered_address\x18\x04 \x01(\r\x12\x0b\n\x03ttl\x18\x05 \x01(\r\x12\x13\n\x05ident\x18\x06 \x01(\r:\x04\x34\x30\x31\x35\"G\n\x0cmessage_type\x12\x0c\n\x08\x44ISCOVER\x10\x00\x12\t\n\x05OFFER\x10\x01\x12\x0b\n\x07REQUEST\x10\x02\x12\x07\n\x03\x41\x43K\x10\x03\x12\x08\n\x04NACK\x10\x04')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ADDRESS_SERVER_MESSAGE_MESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='message_type',
  full_name='address_server.address_server_message.message_type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DISCOVER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFFER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACK', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NACK', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=226,
  serialized_end=297,
)
_sym_db.RegisterEnumDescriptor(_ADDRESS_SERVER_MESSAGE_MESSAGE_TYPE)


_ADDRESS_SERVER_MESSAGE = _descriptor.Descriptor(
  name='address_server_message',
  full_name='address_server.address_server_message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='address_server.address_server_message.uid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='address_server.address_server_message.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='network', full_name='address_server.address_server_message.network', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offered_address', full_name='address_server.address_server_message.offered_address', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='address_server.address_server_message.ttl', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ident', full_name='address_server.address_server_message.ident', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=4015,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADDRESS_SERVER_MESSAGE_MESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=297,
)

_ADDRESS_SERVER_MESSAGE.fields_by_name['type'].enum_type = _ADDRESS_SERVER_MESSAGE_MESSAGE_TYPE
_ADDRESS_SERVER_MESSAGE_MESSAGE_TYPE.containing_type = _ADDRESS_SERVER_MESSAGE
DESCRIPTOR.message_types_by_name['address_server_message'] = _ADDRESS_SERVER_MESSAGE

address_server_message = _reflection.GeneratedProtocolMessageType('address_server_message', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESS_SERVER_MESSAGE,
  __module__ = 'address_server_pb2'
  # @@protoc_insertion_point(class_scope:address_server.address_server_message)
  ))
_sym_db.RegisterMessage(address_server_message)


# @@protoc_insertion_point(module_scope)
