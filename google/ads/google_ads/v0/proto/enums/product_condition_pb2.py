# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/product_condition.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/enums/product_condition.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v0.enumsB\025ProductConditionProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums\352\002!Google::Ads::GoogleAds::V0::Enums'),
  serialized_pb=_b('\n;google/ads/googleads_v0/proto/enums/product_condition.proto\x12\x1dgoogle.ads.googleads.v0.enums\"l\n\x14ProductConditionEnum\"T\n\x10ProductCondition\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x07\n\x03NEW\x10\x03\x12\x0f\n\x0bREFURBISHED\x10\x04\x12\x08\n\x04USED\x10\x05\x42\xea\x01\n!com.google.ads.googleads.v0.enumsB\x15ProductConditionProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enums\xea\x02!Google::Ads::GoogleAds::V0::Enumsb\x06proto3')
)



_PRODUCTCONDITIONENUM_PRODUCTCONDITION = _descriptor.EnumDescriptor(
  name='ProductCondition',
  full_name='google.ads.googleads.v0.enums.ProductConditionEnum.ProductCondition',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REFURBISHED', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USED', index=4, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=118,
  serialized_end=202,
)
_sym_db.RegisterEnumDescriptor(_PRODUCTCONDITIONENUM_PRODUCTCONDITION)


_PRODUCTCONDITIONENUM = _descriptor.Descriptor(
  name='ProductConditionEnum',
  full_name='google.ads.googleads.v0.enums.ProductConditionEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PRODUCTCONDITIONENUM_PRODUCTCONDITION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=202,
)

_PRODUCTCONDITIONENUM_PRODUCTCONDITION.containing_type = _PRODUCTCONDITIONENUM
DESCRIPTOR.message_types_by_name['ProductConditionEnum'] = _PRODUCTCONDITIONENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductConditionEnum = _reflection.GeneratedProtocolMessageType('ProductConditionEnum', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCTCONDITIONENUM,
  __module__ = 'google.ads.googleads_v0.proto.enums.product_condition_pb2'
  ,
  __doc__ = """Condition of a product offer.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.ProductConditionEnum)
  ))
_sym_db.RegisterMessage(ProductConditionEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
