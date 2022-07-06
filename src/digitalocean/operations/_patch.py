# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import TYPE_CHECKING

from ._operations import DropletsOperations as Droplets

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    pass


class DropletsOperations(Droplets):
    def get_public_IPv4(self, droplet_id: int):
        droplet = self.get(droplet_id)

        ip_address = ""
        for net in droplet["networks"]["v4"]:
            if net["type"] == "public":
                ip_address = net["ip_address"]
        return ip_address


__all__ = ["DropletsOperations"]


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
