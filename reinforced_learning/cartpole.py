import gym # import gym library
env = gym.make('CartPole-v0') # this is the environment, from the library

iterations = int(input("What's the number of iterations?: "))

for i in range(iterations): # for 1000 steps
    observation= env.reset() # reset to 0 the environment
    for t in range(100):
        env.render() # render the result, in order to see the progress
        print(observation) # what is happening
        action = env.action_space.sample() # get a random action
        observation, reward, done, infor = env.step(action) # Action and see what the environment gets you (observation) the reward of your action, if we have achieved our goal and general information
        if done:
            print("We're done here")
            break
env.close() # close the environment
