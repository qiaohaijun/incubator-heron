# copyright 2016 twitter. all rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''module for example topology: CustomGroupingTopology'''

import heron.api.src.python.api_constants as constants
from heron.api.src.python.topology import Topology
from heron.api.src.python.stream import Grouping

from heron.examples.src.python.spout import MultiStreamSpout
from heron.examples.src.python.bolt import CountBolt, StreamAggregateBolt

class MultiStream(Topology):
  spout = MultiStreamSpout.spec(par=2)
  count_bolt = CountBolt.spec(par=2,
                              inputs={spout: Grouping.fields('word')},
                              config={constants.TOPOLOGY_TICK_TUPLE_FREQ_SECS: 10})
  stream_aggregator = StreamAggregateBolt.spec(par=1,
                                               inputs={spout: Grouping.ALL,
                                                       spout['error']: Grouping.ALL},
                                               config={constants.TOPOLOGY_TICK_TUPLE_FREQ_SECS: 15})