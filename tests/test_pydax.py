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

import yaml

import pydax


pydax.init(
    DEFAULT_DATASET_SCHEMA_URL='datasets.yaml',
    DEFAULT_FORMAT_SCHEMA_URL='formats.yaml',
    DEFAULT_LICENSE_SCHEMA_URL='licenses.yaml'
)

with open('datasets.yaml') as f:
    datasets = yaml.safe_load(f)

# Datasets name are the same from the schema files. This helps ensure that PyDAX doesn't miss any dataset during the
# test.
assert frozenset(datasets['datasets']) == frozenset(pydax.list_all_datasets())

for name, versions in pydax.list_all_datasets().items():
    # Versions must be the same from the schema files. This helps ensure that PyDAX doesn't miss any dataset during the
    # test.
    assert frozenset(datasets['datasets'][name]) == frozenset(versions)
    for version in versions:
        pydax.load_dataset(name=name, version=version, subdatasets=None)
