from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Connect to Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Create FastAPI app
app = FastAPI()


# -----------------------------
# Request model
# -----------------------------

class RecipeRequest(BaseModel):
    ingredients: list[str]


# -----------------------------
# Home
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Food Recipe Backend is Working!"
    }


# -----------------------------
# Test database connection
# -----------------------------

@app.get("/test-db")
def test_db():

    response = supabase.table("recipes").select("*").limit(1).execute()

    return {
        "message": "Supabase connected!",
        "data": response.data
    }


# -----------------------------
# Test recipe
# -----------------------------

@app.post("/test-recipe")
def test_recipe():

    recipe = {
        "title": "Tomato Egg Masala",
        "description": "Simple tomato and egg recipe",
        "ingredients": ["Tomato", "Egg", "Onion"],
        "instructions": [
            "Chop vegetables",
            "Cook onion and tomato",
            "Add egg"
        ],
        "cooking_time": 15,
        "servings": 2,
        "cuisine": "Indian",
        "dietary_type": "Non-Vegetarian"
    }

    response = supabase.table("recipes").insert(recipe).execute()

    return response.data


# -----------------------------
# Temporary AI recipe generator
# -----------------------------

def generate_recipe(ingredients):

    recipe = {
        "title": "AI Generated Recipe",
        "description": "Recipe generated using the given ingredients.",
        "ingredients": ingredients,
        "instructions": [
            "Prepare the ingredients.",
            "Cook the ingredients properly.",
            "Serve the prepared dish."
        ],
        "cooking_time": 20,
        "servings": 2,
        "cuisine": "Indian",
        "dietary_type": "Vegetarian"
    }

    return recipe


# -----------------------------
# Generate recipe
# -----------------------------

@app.post("/recipes")
def create_recipe(request: RecipeRequest):

    # Get ingredients from user
    ingredients = request.ingredients

    # Generate recipe
    recipe = generate_recipe(ingredients)

    # Save recipe in Supabase
    response = supabase.table("recipes").insert(recipe).execute()

    return {
        "message": "Recipe generated and saved successfully!",
        "recipe": response.data
    }