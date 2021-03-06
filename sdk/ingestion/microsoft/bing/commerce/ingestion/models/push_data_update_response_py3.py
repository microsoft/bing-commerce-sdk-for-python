# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PushDataUpdateResponse(Model):
    """A response to a push data update.

    :param update_id: The id of the push data update that you can use to track
     it down.
    :type update_id: str
    """

    _attribute_map = {
        'update_id': {'key': 'updateId', 'type': 'str'},
    }

    def __init__(self, *, update_id: str=None, **kwargs) -> None:
        super(PushDataUpdateResponse, self).__init__(**kwargs)
        self.update_id = update_id
