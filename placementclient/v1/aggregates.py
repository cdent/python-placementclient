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

from oslo_serialization import jsonutils

from placementclient import utils
from placementclient.v1 import base


class AggregatesManager(base.Manager):
    url = "/resource_providers/%s/aggregates"

    def list(self, resource_provider_uuid):
        """List resource provider aggregates.

        :param resource_provider_uuid: UUID of the resource provider
        :type resource_provider_uuid: str
        """
        utils.ensure_resource_provider_uuid_is_uuid(resource_provider_uuid)
        url = self.url % resource_provider_uuid
        return self._get(url).json()

    def associate(self, resource_provider_uuid, aggregates):
        """Associate a list of aggregates with a resource provider.

        :param resource_provider_uuid: UUID of the resource provider
        :type resource_provider_uuid: str
        :param aggregates: aggregates to be associated to the resource provider
        :type aggregates: list of str
        """
        utils.ensure_resource_provider_uuid_is_uuid(resource_provider_uuid)
        url = self.url % resource_provider_uuid
        self._put(url, headers={'Content-Type': "application/json"},
                  data=jsonutils.dumps(aggregates))
