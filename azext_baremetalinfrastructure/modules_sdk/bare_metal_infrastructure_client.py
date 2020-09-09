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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.azure_bare_metal_instances_operations import AzureBareMetalInstancesOperations
from .operations.bare_metal_instances_operations import BareMetalInstancesOperations
from .operations.operations import Operations
from . import models


class BareMetalInfrastructureClientConfiguration(AzureConfiguration):
    """Configuration for BareMetalInfrastructureClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Azure subscription ID. This is a
     GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(BareMetalInfrastructureClientConfiguration, self).__init__(base_url)

        self.add_user_agent('baremetalinfrastructure/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class BareMetalInfrastructureClient(SDKClient):
    """The BareMetalInfrastructure Management client

    :ivar config: Configuration for client.
    :vartype config: BareMetalInfrastructureClientConfiguration

    :ivar azure_bare_metal_instances: AzureBareMetalInstances operations
    :vartype azure_bare_metal_instances: microsoft.baremetalinfrastructure.operations.AzureBareMetalInstancesOperations
    :ivar bare_metal_instances: BareMetalInstances operations
    :vartype bare_metal_instances: microsoft.baremetalinfrastructure.operations.BareMetalInstancesOperations
    :ivar operations: Operations operations
    :vartype operations: microsoft.baremetalinfrastructure.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Azure subscription ID. This is a
     GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = BareMetalInfrastructureClientConfiguration(credentials, subscription_id, base_url)
        super(BareMetalInfrastructureClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2020-08-06-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.azure_bare_metal_instances = AzureBareMetalInstancesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.bare_metal_instances = BareMetalInstancesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
