import gym # import gym library
env = gym.make('CartPole-v0') # this is the environment, from the library
env.reset() # reset to 0 the environment
for _ in range(1000): # for 1000 steps
    env.render() # render the result, in order to see the progress
    env.step(env.action_space.sample()) # Take a step in the environment
env.close() # close the environment
