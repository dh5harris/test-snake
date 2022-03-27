import random
import constants
from game.shared.color import Color
from game.casting.cast import Cast
from game.casting.actor import Actor
from game.shared.point import Point


class Food(Actor):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self._points = 0
        self.set_text("")
        # self._foods = []
        # self._foods = self.set_food()
        self.set_color(constants.YELLOW)
        self.reset()
        # self.set_food()
        
    def reset(self):
        """Selects a random position and points that the food is worth."""
        for i in range(constants.DEFAULT_FOOD):
            self._points = random.randint(1, 8)
            # x = random.randint(1, constants.COLUMNS - 1)
            x = random.randint(1, constants.MAX_X - 1)
            y = random.randint(1, constants.MAX_Y - 1)
            position = Point(x, y)
            position = position.scale(constants.CELL_SIZE)
            
            # food = Actor()
            self.set_position(position)
            self.set_text('&')
        # food.set_text("&")
        # self._foods.append(food)

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
        
        
    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        return self._points

    def set_food(self):
        for n in range(constants.DEFAULT_FOOD):
            # text_list = [42,79]
            # text = chr(random.choice(text_list)) 

            self._points = random.randint(1, 8)
            x = random.randint(1, constants.MAX_X - 10)
            y = random.randint(1, constants.MAX_Y - 10)
            position = Point(x, y)
            position = position.scale(constants.CELL_SIZE)
            
            foods = self.reset()
            # self.set_text(text)
            self.set_font_size(constants.FONT_SIZE)
            # self.set_color(color)
            self.set_color(constants.YELLOW)
            self.set_position(position)
            # self.set_velocity(Point(0, 1))
            self.set_text("@")
            self._foods = foods
            # cast.add_actor("food", food)

    def get_food(self):
        return self._foods