from pydantic import BaseModel
from datetime import date, timedelta
from typing import List, Dict, Optional

class UserProfile(BaseModel):
    dietary_restrictions: List[str]
    preferences: Optional[List[str]] = []
    household_size: int

class PantryItem(BaseModel):
    name: str
    quantity: float

class MealSlot(BaseModel):
    name: str
    time: str

class MealPlanRequest(BaseModel):
    start_date: date
    end_date: date
    user_profile: UserProfile
    pantry: List[PantryItem]
    meal_slots: List[MealSlot]

class MockMealPlanRequest(BaseModel):
    dietary_restrictions: List[str]
    household_size: int
    start_date: date
    end_date: date

    def generate_mock_request(self) -> MealPlanRequest:
        mock_pantry = [
            PantryItem(name="lettuce", quantity=2),
            PantryItem(name="tomato", quantity=3),
            PantryItem(name="chicken", quantity=1),
            PantryItem(name="pasta", quantity=2)
        ]
        
        mock_meal_slots = [
            MealSlot(name="Breakfast", time="08:00 AM"),
            MealSlot(name="Lunch", time="12:30 PM"),
            MealSlot(name="Dinner", time="07:00 PM")
        ]
        
        return MealPlanRequest(
            start_date=self.start_date,
            end_date=self.end_date,
            user_profile=UserProfile(dietary_restrictions=self.dietary_restrictions, preferences=[], household_size=self.household_size),
            pantry=mock_pantry,
            meal_slots=mock_meal_slots
        )

class Recipe(BaseModel):
    name: str
    ingredients: List[str]
    instructions: str
    dietary_tags: List[str]

class MealPlan(BaseModel):
    date: date
    meals: Dict[str, Recipe]

class MealPlanResponse(BaseModel):
    plan: List[MealPlan]