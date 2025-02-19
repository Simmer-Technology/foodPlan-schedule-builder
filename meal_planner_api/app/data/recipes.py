from app.models import Recipe

MOCK_RECIPES = [
    Recipe(
        name="Grilled Chicken Salad",
        ingredients=["chicken", "lettuce", "tomato"],
        instructions="Grill the chicken, chop the lettuce and tomato, mix them together.",
        dietary_tags=["high-protein", "gluten-free"]
    ),
    Recipe(
        name="Pasta Primavera",
        ingredients=["pasta", "tomato"],
        instructions="Boil pasta, sauté tomato, mix together.",
        dietary_tags=["vegetarian"]
    ),
    Recipe(
        name="Tomato Soup",
        ingredients=["tomato"],
        instructions="Blend tomatoes, cook on low heat, serve warm.",
        dietary_tags=["vegan", "gluten-free"]
    ),
    Recipe(
        name="Chicken Stir Fry",
        ingredients=["chicken", "lettuce"],
        instructions="Stir-fry chicken with lettuce in a pan.",
        dietary_tags=["high-protein"]
    ),
    Recipe(
        name="Lettuce Wraps",
        ingredients=["lettuce", "chicken"],
        instructions="Wrap cooked chicken in lettuce leaves.",
        dietary_tags=["low-carb", "gluten-free"]
    )
]