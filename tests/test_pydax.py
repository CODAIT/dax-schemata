#!/bin/env python

#
# Copyright 2020 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# This scripts tests all files in CODAIT/dax-schemata. It shouldn't report any error.

import pydax


pydax.init(
    DEFAULT_DATASET_SCHEMA_URL='https://raw.githubusercontent.com/CODAIT/dax-schemata/master/datasets.yaml',
    DEFAULT_FORMAT_SCHEMA_URL='https://raw.githubusercontent.com/CODAIT/dax-schemata/master/formats.yaml',
    DEFAULT_LICENSE_SCHEMA_URL='https://raw.githubusercontent.com/CODAIT/dax-schemata/master/licenses.yaml'
)

for name, versions in pydax.list_all_datasets().items():
    for version in versions:
        pydax.load_dataset(name=name, version=version, subdatasets=None)
