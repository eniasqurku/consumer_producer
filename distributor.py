from __future__ import annotations
import queue
from typing import Optional

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Only imports the below statements during type checking
    from consumer import Consumer


class ContentDistributor:

    def __init__(self) -> None:
        self.consumers = {}

    def set_message(self, message: Optional[str]) -> None:
        for _queue in self.consumers.values():
            _queue.put(message)

    def get_message(self, consumer: Consumer) -> str:
        value = self.consumers[consumer].get()

        return value

    def add_consumer(self, consumer: Consumer) -> None:
        self.consumers[consumer] = queue.Queue()
