from fastapi import FastAPI, HTTPException
import azure.functions as func
from app.models import MealPlanRequest, MealPlanResponse, MockMealPlanRequest
from app.services.meal_planner import generate_meal_plan_service

app = FastAPI()

@app.post("/generate-meal-plan", response_model=MealPlanResponse)
def generate_meal_plan(request: MealPlanRequest):
    return generate_meal_plan_service(request)

@app.post("/mock-meal-plan", response_model=MealPlanRequest)
def mock_meal_plan(request: MockMealPlanRequest):
    return request.generate_mock_request()

# Azure Function entry point
def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle_request(req)
