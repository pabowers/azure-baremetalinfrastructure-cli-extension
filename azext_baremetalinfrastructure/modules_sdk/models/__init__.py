# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .resource_py3 import Resource
    from .hardware_profile_py3 import HardwareProfile
    from .disk_py3 import Disk
    from .storage_profile_py3 import StorageProfile
    from .os_profile_py3 import OSProfile
    from .ip_address_py3 import IpAddress
    from .network_profile_py3 import NetworkProfile
    from .azure_bare_metal_instance_py3 import AzureBareMetalInstance
    from .display_py3 import Display
    from .operation_py3 import Operation
    from .result_py3 import Result
    from .error_definition_py3 import ErrorDefinition
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .tags_py3 import Tags
except (SyntaxError, ImportError):
    from .resource import Resource
    from .hardware_profile import HardwareProfile
    from .disk import Disk
    from .storage_profile import StorageProfile
    from .os_profile import OSProfile
    from .ip_address import IpAddress
    from .network_profile import NetworkProfile
    from .azure_bare_metal_instance import AzureBareMetalInstance
    from .display import Display
    from .operation import Operation
    from .result import Result
    from .error_definition import ErrorDefinition
    from .error_response import ErrorResponse, ErrorResponseException
    from .tags import Tags
from .azure_bare_metal_instance_paged import AzureBareMetalInstancePaged
from .operation_paged import OperationPaged
from .bare_metal_infrastructure_client_enums import (
    AzureBareMetalHardwareTypeNamesEnum,
    AzureBareMetalInstanceSizeNamesEnum,
    AzureBareMetalInstancePowerStateEnum,
    AzureBareMetalProvisioningStatesEnum,
)

__all__ = [
    'Resource',
    'HardwareProfile',
    'Disk',
    'StorageProfile',
    'OSProfile',
    'IpAddress',
    'NetworkProfile',
    'AzureBareMetalInstance',
    'Display',
    'Operation',
    'Result',
    'ErrorDefinition',
    'ErrorResponse', 'ErrorResponseException',
    'Tags',
    'AzureBareMetalInstancePaged',
    'OperationPaged',
    'AzureBareMetalHardwareTypeNamesEnum',
    'AzureBareMetalInstanceSizeNamesEnum',
    'AzureBareMetalInstancePowerStateEnum',
    'AzureBareMetalProvisioningStatesEnum',
]
