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

    def add_reminder(self):





# TODO: Implement Day class here


# TODO: Implement Calendar class here
