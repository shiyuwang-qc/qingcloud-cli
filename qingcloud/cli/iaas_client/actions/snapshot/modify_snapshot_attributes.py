# =========================================================================
# Copyright 2012-present Yunify, Inc.
# -------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================

from qingcloud.cli.iaas_client.actions.base import BaseAction

class ModifySnapshotAttributesAction(BaseAction):

    action = 'ModifySnapshotAttributes'
    command = 'modify-snapshot-attributes'
    usage = '%(prog)s -s snapshot_id [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--snapshot', dest='snapshot',
                action='store', type=str, default='',
                help='the id of the snapshot whose attributes you want to modify.')

        parser.add_argument('-N', '--name', dest='snapshot_name',
                action='store', type=str, default=None,
                help='specify the new snapshot name.')

        parser.add_argument('-D', '--description', dest='description',
                action='store', type=str, default=None,
                help='the detailed description of the resource.')

    @classmethod
    def build_directive(cls, options):
        if not options.snapshot:
            print('error: [snapshot] should be specified')
            return None

        return {
                'snapshot': options.snapshot,
                'snapshot_name': options.snapshot_name,
                'description': options.description,
                }
