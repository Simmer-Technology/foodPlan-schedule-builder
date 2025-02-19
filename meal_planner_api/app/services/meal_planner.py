from http.client import HTTPException
from app.models import MealPlanRequest, MealPlanResponse, MealPlan, Recipe
from app.data.recipes import MOCK_RECIPES
from datetime import timedelta

def find_recipes(user_profile, pantry):
    available_ingredients = {item.name for item in pantry}
    filtered_recipes = [r for r in MOCK_RECIPES if all(i in available_ingredients for i in r.ingredients) and not any(tag in user_profile.dietary_restrictions for tag in r.dietary_tags)]
    return filtered_recipes

def generate_meal_plan_service(request: MealPlanRequest) -> MealPlanResponse:
    available_recipes = find_recipes(request.user_profile, request.pantry)
    if not available_recipes:
        raise HTTPException(status_code=404, detail="No suitable recipes found")
    
    meal_plan = []
    current_date = request.start_date
    while current_date <= request.end_date:
        daily_meals = {}
        for slot in request.meal_slots:
            recipe = available_recipes.pop(0) if available_recipes else None
            if recipe:
                daily_meals[slot.name] = recipe
        meal_plan.append(MealPlan(date=current_date, meals=daily_meals))
        current_date += timedelta(days=1)
    
    return MealPlanResponse(plan=meal_plan)
