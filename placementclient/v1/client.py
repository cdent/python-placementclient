#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from placementclient import client
from placementclient.v1 import aggregates
from placementclient.v1 import inventories
from placementclient.v1 import resource_providers
from placementclient.v1 import usages


class Client(object):
    """Client for the placement v1 API.

    :param string session: session
    :type session: :py:class:`keystoneauth.adapter.Adapter`
    """

    def __init__(self, session=None, service_type='placement', **kwargs):
        """Initialize a new client for the placement v1 API."""
        self.api = client.SessionClient(session, service_type=service_type,
                                        **kwargs)
        self.resource_providers = resource_providers.ResourceProvidersManager(
            self)
        self.inventories = inventories.InventoriesManager(self)
        self.aggregates = aggregates.AggregatesManager(self)
        self.usages = usages.UsagesManager(self)
