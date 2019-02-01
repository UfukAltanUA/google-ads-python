# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/common/explorer_auto_optimizer_setting.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/common/explorer_auto_optimizer_setting.proto',
  package='google.ads.googleads.v0.common',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v0.commonB!ExplorerAutoOptimizerSettingProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Common\312\002\036Google\\Ads\\GoogleAds\\V0\\Common\352\002\"Google::Ads::GoogleAds::V0::Common'),
  serialized_pb=_b('\nJgoogle/ads/googleads_v0/proto/common/explorer_auto_optimizer_setting.proto\x12\x1egoogle.ads.googleads.v0.common\x1a\x1egoogle/protobuf/wrappers.proto\"J\n\x1c\x45xplorerAutoOptimizerSetting\x12*\n\x06opt_in\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\xfc\x01\n\"com.google.ads.googleads.v0.commonB!ExplorerAutoOptimizerSettingProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Common\xea\x02\"Google::Ads::GoogleAds::V0::Commonb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_EXPLORERAUTOOPTIMIZERSETTING = _descriptor.Descriptor(
  name='ExplorerAutoOptimizerSetting',
  full_name='google.ads.googleads.v0.common.ExplorerAutoOptimizerSetting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opt_in', full_name='google.ads.googleads.v0.common.ExplorerAutoOptimizerSetting.opt_in', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=142,
  serialized_end=216,
)

_EXPLORERAUTOOPTIMIZERSETTING.fields_by_name['opt_in'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
DESCRIPTOR.message_types_by_name['ExplorerAutoOptimizerSetting'] = _EXPLORERAUTOOPTIMIZERSETTING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExplorerAutoOptimizerSetting = _reflection.GeneratedProtocolMessageType('ExplorerAutoOptimizerSetting', (_message.Message,), dict(
  DESCRIPTOR = _EXPLORERAUTOOPTIMIZERSETTING,
  __module__ = 'google.ads.googleads_v0.proto.common.explorer_auto_optimizer_setting_pb2'
  ,
  __doc__ = """Settings for the Display Campaign Optimizer, initially termed
  "Explorer".
  
  
  Attributes:
      opt_in:
          Indicates whether the optimizer is turned on.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.ExplorerAutoOptimizerSetting)
  ))
_sym_db.RegisterMessage(ExplorerAutoOptimizerSetting)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
