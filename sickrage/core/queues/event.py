# Author: echel0n <echel0n@sickrage.ca>
# URL: https://sickrage.ca
#
# This file is part of SiCKRAGE.
#
# SiCKRAGE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SiCKRAGE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SiCKRAGE.  If not, see <http://www.gnu.org/licenses/>.



from functools import partial

from tornado.ioloop import IOLoop

import sickrage
from sickrage.core.queues import SRQueue, SRQueueItem


class EventQueue(SRQueue):
    def __init__(self):
        SRQueue.__init__(self, "EVENTQUEUE")

    def fire_event(self, event, **kwargs):
        sickrage.app.io_loop.add_callback(self.put, EventQueueItem(event, **kwargs))


class EventQueueItem(SRQueueItem):
    """
    Represents an event in the queue waiting to be executed
    """

    def __init__(self, event, **kwargs):
        super(EventQueueItem, self).__init__('Firing Event')
        self.event = partial(event, **kwargs)

    def run(self):
        self.event()
