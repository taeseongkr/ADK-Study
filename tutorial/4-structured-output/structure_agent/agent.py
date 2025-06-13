from google.adk.agents import Agent
from google.adk.tools import google_search
from pydantic import BaseModel, Field
def my_tool_function(query):
    # This function can be used to process the query before passing it to the tool
    return query

class FoodNutrition(BaseModel):
    food_name: str = Field(
        ...,
        description="The name of the food item being analyzed")
    calories_per_100g: float = Field(
        ...,
        description="Calories per 100 grams of the food")
    protein_g: float = Field(
        ...,
        description="Protein content in grams per 100g")
    carbs_g: float = Field(
        ...,
        description="Carbohydrate content in grams per 100g")
    fat_g: float = Field(
        ...,
        description="Fat content in grams per 100g")
    fiber_g: float = Field(
        default=0.0,
        description="Fiber content in grams per 100g")
    vitamins: list[str] = Field(
        default_factory=list,
        description="List of key vitamins present in the food")
    minerals: list[str] = Field(
        default_factory=list,
        description="List of key minerals present in the food")



root_agent = Agent(
    name="structure_agent",
    description="Search agent",
    instruction="""
    You are a nutrition expert that provides detailed nutritional information about food items.
    When given a food item, analyze its nutritional content and provide accurate data about:
    - Calories per 100g
    - Macronutrients (protein, carbs, fat)
    - Fiber content
    - Key vitamins and minerals
    
    Be precise with numerical values and comprehensive with vitamin/mineral lists.
    IMPORTANT: your response must be structured in the FoodNutrition schema.
        {
        "food_name": Food name,
        "calories_per_100g": calories per 100 grams,
        "protein_g": protein content in grams per 100g,
        "carbs_g": carbohydrate content in grams per 100g,
        "fat_g": fat content in grams per 100g,
        "fiber_g": fiber content in grams per 100g,
        "vitamins": list of key vitamins present in the food,
        "minerals": list of key minerals present in the food
        }
    
    """,
    output_schema=FoodNutrition,
    model="gemini-2.0-flash")

