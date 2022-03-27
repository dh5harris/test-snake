import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with the other snake, or to determine the end of the game.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score and moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        score = cast.get_actors("scores")
        food = cast.get_first_actor("foods")
        snakes = cast.get_actors("snakes")
        snake1 = snakes[0]
        snake2 = snakes[1]
        head1 = snake1.get_head()
        head2 = snake2.get_head()
        score1 = score[0]
        score2 = score[1]


        if head1.get_position().equals(food.get_position()):
            points = food.get_points()
            snake1.grow_tail(points)
            score1.add_points(points)
            food.reset()

        elif head2.get_position().equals(food.get_position()):
            points = food.get_points()
            snake2.grow_tail(points) 
            score2.add_points(points)
            food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with the other snake.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snakes = cast.get_actors("snakes")
        snake1 = snakes[0]
        snake2 = snakes[1]
        head1 = snake1.get_segments()[0]
        head2 = snake2.get_segments()[0]
        segments1 = snake1.get_segments()[1:]
        segments2 = snake2.get_segments()[1:]
        
        # for segmentgreen in segments1:
        #     for segmentblue in segments2:
                # if head1.get_position().equals(segmentgreen.get_position()):
                #     self._is_game_over = True

                # if head1.get_position().equals(segmentblue.get_position()):
                #     self._is_game_over = True

                # if head2.get_position().equals(segmentgreen.get_position()):
                #     self._is_game_over = True

        #         if head2.get_position().equals(segmentblue.get_position()):
        #             self._is_game_over = True
        

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snakes and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snakes = cast.get_actors("snakes")
            snake1 = snakes[0]
            snake2 = snakes[1]
            segments1 = snake1.get_segments()
            segments2 = snake2.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")   # add which team wins
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments1:
                segment.set_color(constants.WHITE)    # add the school color
            food.set_color(constants.WHITE)

            for segment in segments2:
                segment.set_color(constants.WHITE)    # add the school color
            food.set_color(constants.WHITE)
    