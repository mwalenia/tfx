# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Setup dependencies for local and cloud deployment."""
import setuptools

# LINT.IfChange
TF_VERSION = '1.13.1'
# LINT.ThenChange(train_mlengine.sh, start_model_server_mlengine.sh)

# LINT.IfChange
BEAM_VERSION = '2.12.0'
# LINT.ThenChange(setup_beam_on_flink.sh)

if __name__ == '__main__':
    setuptools.setup(
        name='tfx_chicago_taxi',
        version='0.13.0',
        packages=setuptools.find_packages(),
        install_requires=[
            'apache-beam[gcp]==' + BEAM_VERSION,
            'jupyter==1.0',
            'protobuf==3.7.1',
            'tensorflow==' + TF_VERSION,
            'tensorflow-data-validation==0.13.1',
            'tensorflow-metadata==0.13.0',
            'tensorflow-model-analysis==0.13.2',
            'tensorflow-serving-api==1.13.0',
            'tensorflow-transform==0.13.0',
            'scikit-learn<=0.20'
            ],
        python_requires='>=2.7,<3')