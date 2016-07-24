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


class InventoriesManager(base.Manager):
    url = "/resource_providers/%s/inventories"

    def list(self, resource_provider_uuid):
        """List resource provider inventories.

        :param resource_provider_uuid: UUID of the resource provider
        :type resource_provider_uuid: str
        """
        utils.ensure_resource_provider_uuid_is_uuid(resource_provider_uuid)
        url = self.url % resource_provider_uuid
        return self._get(url).json()

    def get(self, resource_provider_uuid, resource_class):
        """List resource provider inventories.

        :param resource_provider_uuid: UUID of the resource provider
        :type resource_provider_uuid: str
        :param resource_class: Resource class name of the inventory to be
          returned
        :type resource_class: str
        """
        utils.ensure_resource_provider_uuid_is_uuid(resource_provider_uuid)
        url = self.url % resource_provider_uuid + '/' + resource_class
        return self._get(url).json()

    def create(self, resource_provider_uuid, inventory):
        """Create an inventory.

        :param resource_provider_uuid: UUID of the resource provider
        :type resource_provider_uuid: str
        :param inventory: The inventory
        :type inventory: dict
        """
        utils.ensure_resource_provider_uuid_is_uuid(resource_provider_uuid)
        url = self.url % resource_provider_uuid
        return self._post(url, headers={'Content-Type': "application/json"},
                          data=jsonutils.dumps(inventory))

    def update(self, resource_provider_uuid, inventory, resource_class):
        """Update an inventory.

        :param resource_provider_uuid: UUID of the resource provider
        :type resource_provider_uuid: str
        :param inventory: The inventory
        :type inventory: dict
        :param resource_class: The resource class of the inventory to update
        :type resource_class: str
        """
        utils.ensure_resource_provider_uuid_is_uuid(resource_provider_uuid)
        url = self.url % resource_provider_uuid + '/' + resource_class
        self._put(url, headers={'Content-Type': "application/json"},
                  data=jsonutils.dumps(inventory))

    def delete(self, resource_provider_uuid, resource_class):
        """Delete an inventory.

        :param resource_provider_uuid: UUID of the resource provider
        :type resource_provider_uuid: str
        :param resource_class: Resource class name of the inventory to be
          deleted
        :type resource_class: str
        """
        utils.ensure_resource_provider_uuid_is_uuid(resource_provider_uuid)
        url = self.url % resource_provider_uuid + '/' + resource_class
        self._delete(url)
