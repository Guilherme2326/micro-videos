from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
from  unittest import TestCase

@dataclass() 
class Category:
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now()
        )
    
    
# print(Category('Movie', 'some description', True, datetime.now()))