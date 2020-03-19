import gym

env = gym.make('NChain-v0')
env.reset()

from gym import spaces

## setup code for custom env

class MazeEnv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

  def __init__(self, maze):
    super(MazeEnv, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:
    N_DISCRETE_ACTIONS = 4
    # This line means an input can be from 0-3 inclusive
    self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)

    # TODO still need to define observation space?
    # should be all prior moves
    # self.observation_space = pass

    # TODO render maze from file?


    # Example for using image as input:
    # self.observation_space = spaces.Box(low=0, high=255, shape=
    #                 (HEIGHT, WIDTH, N_CHANNELS), dtype=np.uint8)

  def step(self, action):
    # Execute one time step within the environment
    ...
  def reset(self, starting_room, num_rooms):
    # Reset the state of the environment to an initial state
    self.current_room = starting_room
    self.seen = {starting_room.id}
    self.num_rooms = num_rooms
    self.traversal_path = []
    
  def render(self, mode='human', close=False):
    # Render the environment to the screen
    ...