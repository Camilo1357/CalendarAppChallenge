from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


# TODO: Implement Reminder class here
@dataclass
class Reminder:
   EMAIL: str = field(init= False, default ='email')
   SYSTEM: str = field(init= False, default = 'system')
   date_time: datetime
   type: str = ClassVar[EMAIL]

   def __str__(self) -> str:
       return f"Reminder on {self.date_time} of type {self.type}"

# TODO: Implement Event class here
@dataclass
class Event:
    title : str
    description : str
    date_ : date
    start_at : time
    end_at : time
    reminders : list[Reminder] = field(init=False, default_factory = list)
    id: str = field(default_factory= generate_unique_id)

    def add_reminder(self, date_time: datetime, type: str):
        self.reminders.append(Reminder(date_time, type))

    def delete_reminder(self, reminder_index: int ):
        if 0 <= reminder_index < len(self.reminders):
            self.reminders.pop(reminder_index)
        else:
            reminder_not_found_error()

    def __str__(self):
        return f"ID: {self.id}\n Event title: {self.title}\n Description: {self.description}\n Time: {self.start_at} - {self.end_at}"

# TODO: Implement Day class here
class Day:
    def __init__(self, date_: date):
        self.date_ : date = date_
        self.slots : dict[time, str | None] = {}
        self._init_slots()

    def _init_slots(self):
        for hour in range(0, 24):
            for minute in [0, 15, 30, 45]:
                time_slot = time(hour, minute)
                self.slots[time_slot] = None

    def add_event(self,event_id: str, start_at: time, end_at: time):
        self.slots.append(event_id)









# TODO: Implement Calendar class here
