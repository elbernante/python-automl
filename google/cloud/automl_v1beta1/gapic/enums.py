# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrappers for protocol buffer enum types."""

import enum


class ClassificationType(enum.IntEnum):
    """
    Type of the classification problem.

    Attributes:
      CLASSIFICATION_TYPE_UNSPECIFIED (int): Should not be used, an un-set enum has this value by default.
      MULTICLASS (int): At most one label is allowed per example.
      MULTILABEL (int): Multiple labels are allowed for one example.
    """

    CLASSIFICATION_TYPE_UNSPECIFIED = 0
    MULTICLASS = 1
    MULTILABEL = 2


class NullValue(enum.IntEnum):
    """
    ``NullValue`` is a singleton enumeration to represent the null value for
    the ``Value`` type union.

    The JSON representation for ``NullValue`` is JSON ``null``.

    Attributes:
      NULL_VALUE (int): Null value.
    """

    NULL_VALUE = 0


class TypeCode(enum.IntEnum):
    """
    ``TypeCode`` is used as a part of ``DataType``.

    Each legal value of a DataType can be encoded to or decoded from a JSON
    value, using the encodings listed below, and definitions of which can be
    found at

    https: //developers.google.com/protocol-buffers //
    /docs/reference/google.protobuf#value.

    Attributes:
      TYPE_CODE_UNSPECIFIED (int): Not specified. Should not be used.
      FLOAT64 (int): Encoded as ``number``, or the strings ``"NaN"``, ``"Infinity"``, or
      ``"-Infinity"``.
      TIMESTAMP (int): Must be between 0AD and 9999AD. Encoded as ``string`` according to
      ``time_format``, or, if that format is not set, then in RFC 3339
      ``date-time`` format, where ``time-offset`` = ``"Z"`` (e.g.
      1985-04-12T23:20:50.52Z).
      STRING (int): Encoded as ``string``.
      ARRAY (int): Encoded as ``list``, where the list elements are represented according
      to

      ``list_element_type``.
      STRUCT (int): Encoded as ``struct``, where field values are represented according to
      ``struct_type``.
      CATEGORY (int): Values of this type are not further understood by AutoML, e.g. AutoML is
      unable to tell the order of values (as it could with FLOAT64), or is
      unable to say if one value contains another (as it could with STRING).
      Encoded as ``string`` (bytes should be base64-encoded, as described in
      RFC 4648, section 4).
    """

    TYPE_CODE_UNSPECIFIED = 0
    FLOAT64 = 3
    TIMESTAMP = 4
    STRING = 6
    ARRAY = 8
    STRUCT = 9
    CATEGORY = 10


class Model(object):
    class DeploymentState(enum.IntEnum):
        """
        Deployment state of the model.

        Attributes:
          DEPLOYMENT_STATE_UNSPECIFIED (int): Should not be used, an un-set enum has this value by default.
          DEPLOYED (int): Model is deployed.
          UNDEPLOYED (int): Model is not deployed.
        """

        DEPLOYMENT_STATE_UNSPECIFIED = 0
        DEPLOYED = 1
        UNDEPLOYED = 2
