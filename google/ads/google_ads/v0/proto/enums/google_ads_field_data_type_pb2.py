# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/google_ads_field_data_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/enums/google_ads_field_data_type.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v0.enumsB\033GoogleAdsFieldDataTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums\352\002!Google::Ads::GoogleAds::V0::Enums'),
  serialized_pb=_b('\nDgoogle/ads/googleads_v0/proto/enums/google_ads_field_data_type.proto\x12\x1dgoogle.ads.googleads.v0.enums\"\xcf\x01\n\x1aGoogleAdsFieldDataTypeEnum\"\xb0\x01\n\x16GoogleAdsFieldDataType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07\x42OOLEAN\x10\x02\x12\x08\n\x04\x44\x41TE\x10\x03\x12\n\n\x06\x44OUBLE\x10\x04\x12\x08\n\x04\x45NUM\x10\x05\x12\t\n\x05\x46LOAT\x10\x06\x12\t\n\x05INT32\x10\x07\x12\t\n\x05INT64\x10\x08\x12\x0b\n\x07MESSAGE\x10\t\x12\x11\n\rRESOURCE_NAME\x10\n\x12\n\n\x06STRING\x10\x0b\x42\xf0\x01\n!com.google.ads.googleads.v0.enumsB\x1bGoogleAdsFieldDataTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enums\xea\x02!Google::Ads::GoogleAds::V0::Enumsb\x06proto3')
)



_GOOGLEADSFIELDDATATYPEENUM_GOOGLEADSFIELDDATATYPE = _descriptor.EnumDescriptor(
  name='GoogleAdsFieldDataType',
  full_name='google.ads.googleads.v0.enums.GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType',
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
      name='BOOLEAN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENUM', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_NAME', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=11, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=135,
  serialized_end=311,
)
_sym_db.RegisterEnumDescriptor(_GOOGLEADSFIELDDATATYPEENUM_GOOGLEADSFIELDDATATYPE)


_GOOGLEADSFIELDDATATYPEENUM = _descriptor.Descriptor(
  name='GoogleAdsFieldDataTypeEnum',
  full_name='google.ads.googleads.v0.enums.GoogleAdsFieldDataTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GOOGLEADSFIELDDATATYPEENUM_GOOGLEADSFIELDDATATYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=311,
)

_GOOGLEADSFIELDDATATYPEENUM_GOOGLEADSFIELDDATATYPE.containing_type = _GOOGLEADSFIELDDATATYPEENUM
DESCRIPTOR.message_types_by_name['GoogleAdsFieldDataTypeEnum'] = _GOOGLEADSFIELDDATATYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GoogleAdsFieldDataTypeEnum = _reflection.GeneratedProtocolMessageType('GoogleAdsFieldDataTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _GOOGLEADSFIELDDATATYPEENUM,
  __module__ = 'google.ads.googleads_v0.proto.enums.google_ads_field_data_type_pb2'
  ,
  __doc__ = """Container holding the various data types.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.GoogleAdsFieldDataTypeEnum)
  ))
_sym_db.RegisterMessage(GoogleAdsFieldDataTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
