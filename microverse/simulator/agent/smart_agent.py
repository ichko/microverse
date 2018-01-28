import math

from .agent import Agent
from ..utils import vec2
from ..plugins import \
    Sight, \
    NeuralNetwork, \
    Navigator, \
    Digestion, \
    Mobility, \
    Fatigue


class SmartAgent(Agent):
    def __init__(self, environment, obstacles, *args, **kwargs):
        super(SmartAgent, self).__init__(*args, **kwargs)

        sight = Sight(
            fov=math.pi / 2,
            ray_count=7,
            strength=50,
            environment=environment + obstacles
        )
        brain = NeuralNetwork([7, 10, 1])
        navigator = Navigator(steering_magnitude=0.01)
        digestion = Digestion(environment=environment)
        mobility = Mobility(obstacles=obstacles)
        fatigue = Fatigue()

        self.plug(sight, brain, navigator)
        self.plug(digestion)
        self.plug(mobility)
        self.plug(fatigue)
