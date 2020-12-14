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
    DATASET_SCHEMA_URL='datasets.yaml',
    FORMAT_SCHEMA_URL='formats.yaml',
    LICENSE_SCHEMA_URL='licenses.yaml'
)

with open('datasets.yaml') as f:
    datasets = yaml.safe_load(f)

# Datasets name are the same from the schema files. This helps ensure that PyDAX doesn't miss any dataset during the
# test.
assert frozenset(datasets['datasets']) == frozenset(pydax.list_all_datasets())
# Sanity check. In case of all tests being skipped because of a minor error such as in formatting.
assert len(pydax.list_all_datasets()) > 0

for name, versions in pydax.list_all_datasets().items():
    # Versions must be the same from the schema files. This helps ensure that PyDAX doesn't miss any dataset during the
    # test.
    assert frozenset(datasets['datasets'][name]) == frozenset(versions)
    # Sanity check. In case of all tests being skipped because of a minor error such as in formatting.
    assert len(versions) > 0
    for version in versions:
        # Print dataset info. This also examines relevant portion in license.yaml
        print(pydax.get_dataset_metadata(name, version, human=True), end='\n\n')
        pydax.load_dataset(name=name, version=version, subdatasets=None)
