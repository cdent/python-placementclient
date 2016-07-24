#
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


class ResourceProvidersManager(base.Manager):
    url = "/resource_providers"

    def list(self):
        """List resource providers."""
        return self._get(self.url).json()

    def get(self, resource_provider_uuid):
        """Get a resource provider.

        :param resource_provider_uuid: UUID of the resource provider
        :type resource_provider_uuid: str
        """
        utils.ensure_resource_provider_uuid_is_uuid(resource_provider_uuid)
        url = self.url + '/' + resource_provider_uuid
        return self._get(url).json()

    def create(self, resource_provider):
        """Create a resource provider.

        :param resource_provider: The resource provider
        :type resource_provider: dict
        """
        return self._post(
            self.url, headers={'Content-Type': "application/json"},
            data=jsonutils.dumps(resource_provider))

    def update(self, resource_provider_uuid, resource_provider):
        """Update an resource provider.

        :param resource_provider_uuid: UUID of the resource provider
        :type resource_provider_uuid: str
        :param resource_provider: the resource provider
        :type archive_policy: dict
        """
        self._put(self.url + '/' + resource_provider_uuid,
                  headers={'Content-Type': "application/json"},
                  data=jsonutils.dumps(resource_provider))

    def delete(self, resource_provider_uuid):
        """Delete an resource provider.

        :param resource_provider_uuid: UUID of the resource provider
        :type resource_provider_uuid: str
        """
        url = self.url + '/' + resource_provider_uuid
        self._delete(url)
