#!/usr/bin/env python3
import gym # environment of gym
from collections import namedtuple # to create a specific struct
import numpy as np # numpy duh
from tensorboardX import SummaryWriter # to write the result in some sick as graphs

# our core for machine learning
import torch
import torch.nn as nn # neural network
import torch.optim as optim # optimization (backpropagation?)


HIDDEN_SIZE = 128 # the number of hidden neurons
BATCH_SIZE = 16
PERCENTILE = 70 # only the best 30% remeains after each batch

# Basically a struct the first is the name of the struct (which in this case is,
# duh, the same name of the variable) Then we got the field names. There are
# only two things, in the first one "reward" and "steps" episode.reward and
# episode.steps is possible in this situation We can also do episode[0] to refer
# to reward and likewise episode[1] to refer to "steps" the second one is the
# episode step with observation and action inside
Episode = namedtuple('Episode', field_names=['reward', 'steps'])
EpisodeStep = namedtuple('EpisodeStep', field_names=['observation', 'action'])

class Net(nn.Module): # we specify the parent class so that we can use super later
    def __init__(self, obs_size, hidden_size, n_actions):
        """ Constructor. We are just creating a NN, that's it!"""
        super(Net, self).__init__() # inicializar herencia
        self.net = nn.Sequential(
            nn.Linear(obs_size, hidden_size), # 1st and 2nd layer
            nn.ReLU(), # activation funtion. Always use relu (sigmoid is also common)
            nn.Linear(hidden_size, n_actions) # 2nd and 3rd layer
            # note that there is no softmax, we would use a special function for
            # that
        )

    def forward(self, x):
        """ Returns the value of the network """
        return self.net(x) # with the currents weights return the output
        # x -> y. Just like a regular funtion, we introduce 4 observation values
        # and return 2 actions We will then have to decide that the highest of
        # those two actions will be the actual output that is still to be
        # implemented, with the training I guess


def iterate_batches(env, net, batch_size):
    """ We are just going to go through the batches and see what happens hahha
    """
    # declaring the varibles needed
    batch = [] # rn the batch is empty
    episode_reward = 0.0 # note that by putting the .0 we make sure that the value is float
    episode_steps = [] # why is this an array? maybe we want to change every step and its info?
    obs = env.reset() # of course we need to reset the environment passed to us at the beginning
    sm = nn.Softmax(dim=1) # This is used to get probabilities out of the raw input.

    while True:
        obs_v = torch.FloatTensor([obs]) 
        # We transform the initial observations gathered into a tensor (this
        # will be used to feed the NN). Not that this is a single element 1x4
        # (two dimensions)
        act_probs_v = sm(net(obs_v)) 
        # we are only feeding the observation tensor into the net and using sm
        # to unpack it given that it is not destributed probability, and we want
        # a probability
        act_probs = act_probs_v.data.numpy()[0] 
        # we need to unpack all this data and transform it into an array. What
        # happens is that the output is 1x2 so the [0] will access to both
        # actions probabilities
        action = np.random.choice(len(act_probs), p=act_probs) 
        # now choose one of those based on the probabilities that I have passed
        # to you. You're gonna have to choose between 0 and 1. The probs of 0
        # and 1 are determined by act_probs. 0 and 1 are the two choices for
        # actions. In this example it's just left and right. This is interesting
        # cuz I could use this probabilities in my robot game by choosing
        # between two actions: call lie or believe it. Pretty interesting stuff!
        new_obs, reward, is_done, _ = env.step(action) 
        # perfect so now I used the random action based on those probabilities
        # and act on the environment. I will get the reward, next observation
        # and is_done
        episode_reward += reward 
        # Total amount of reward. Isn't this reseted to 0 when we lose? Probs
        # later.
        episode_steps.append(EpisodeStep(observation=obs, action=action)) 
        # save this results for further examination. Note that we are not saving
        # the action that we got. We observe and we act. That's what we save,
        # that's the "thought" process of the agent we are going to repeat this
        # process and saving steps until is_done = True
        if is_done:
            # save the results into a batch with the episode and the total
            # reward the reward is, i am guessing the metric used to discern
            # good and bad episodes
            batch.append(Episode(reward=episode_reward, steps=episode_steps))
            episode_reward = 0.0 # reset the reward
            episode_steps = [] # reset episodes
            new_obs = env.reset() # reset env and get new observation
            if len(batch) == BATCH_SIZE: # have we gone through all the episodes that we wanted to?
                yield batch 
                # damn. It can be used to pick up were it left off. It's a
                # return but leaves the funtion intact so that we can create
                # more batches without declaring everything again. I find this
                # amazing, what a reserved word
                batch = [] 
                # when we pickup again we have an empty batch all of a sudden
        obs = new_obs # crucial. We assign the last observation to the new one


def filter_batch(batch, percentile):
    rewards = list(map(lambda s: s.reward, batch)) # wtf did it do. This is my first impression
    reward_bound = np.percentile(rewards, percentile) 
    # returns the percentile 70, upper 30%. This is just a number, for example
    # 35.5 is the 70 percentile reward. We can use this to delete everything
    # lower later
    reward_mean = float(np.mean(rewards)) 
    # calculate the mean (average of all the rewards, just to show it)

    train_obs = []
    train_act = []

    for example in batch:
        if example.reward < reward_bound:
            continue 
        # just skips this item in the for loop! Super useful. Bonus: pass is
        # used to don't do anything inside a funtion, for example if we want it
        # empty

        # extend is used to append another list, like list += new_list. Gotta be
        # careful with strings, which are considered arrays of chars.
        train_obs.extend(map(lambda step: step.observation, example.steps))
        train_act.extend(map(lambda step: step.action, example.steps))
        # i am going to have a massive 1 sample out of those 16 episodes that
        # consists in 5 of those episodes, all their steps (30+30+30+30+30)
        # observations and actions. What led them there? Why are those good?
    train_obs_v = torch.FloatTensor(train_obs) # we want the train observations
    train_act_v = torch.LongTensor(train_act) # Why is this tensor long? Why doesn't it have brackets?

    return train_obs_v, train_act_v, reward_bound, reward_mean


if __name__ == "__main__":

    # create env and get n_actions and n_observations
    env = gym.make("CartPole-v0")
    # env = gym.wrappers.Monitor(env, directory="mon", force=True)
    n_actions = env.action_space.n
    n_observations = env.observation_space.shape[0]

    net = Net(n_observations, HIDDEN_SIZE, n_actions)
    objective = nn.CrossEntropyLoss() 
    # this is what we want to achieve. Cross entropy method whatever that means,
    # don't fully understand it get.
    optimizer = optim.Adam(params=net.parameters(), lr=0.01) 
    # note that we can access the parent function .parameters. The learning rate
    # is set to 0.01. Not much thought given to learning rate. A higher learning
    # rate makes the algorithm be more aggressive but also more volatile. A
    # smaller learning rate will take longer but won't be as volatile. We wanna
    # find a sweet spot. Here! the optimizer can actually change the parameters
    # of the net, which is basically what's doing here
    writer = SummaryWriter()
    writer = SummaryWriter(comment="-cartpole")


    for iter_no, batch in enumerate(iterate_batches(env, net, BATCH_SIZE)):
        # YOU CAN ITERATE A FUNCTION WHAT!. Iterate batches returns yields
        # several batches of 16 this is just the first iteration (0). This is
        # basically like a while because we can call the function over and over
        # until our conditions are met. Pretty impressive.

        obs_v, acts_v, reward_b, reward_m = filter_batch(batch, PERCENTILE) 
        # creates obs_v and acts_v based on the batches
        optimizer.zero_grad()
        action_scores_v = net(obs_v)
        loss_v = objective(action_scores_v, acts_v) # what we actually got vs the target
        loss_v.backward() # backpropagation
        optimizer.step() # update the nn

        # show progress in the screen
        print("%d: loss=%.3f, reward_mean=%.1f, reward_bound=%.1f" %(iter_no, loss_v.item(), reward_m, reward_b))
        writer.add_scalar("loss", loss_v.item(), iter_no)
        writer.add_scalar("reward_bound", reward_b, iter_no)
        writer.add_scalar("reward_mean", reward_m, iter_no)
        if reward_m > 199:
            print("Solved!")
            break
    writer.close()


