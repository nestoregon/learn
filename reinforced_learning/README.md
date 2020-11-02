# Reinforced learning Nestor Morales

In this folder you will find a small tutorial for learning reinforced learning. I particularly found useful to use the OpenAI environment [info](www.openai.com)

To start I recommend setting a virtual environment in python [info](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### Installing
```bash
# inside virtual environment (recommended)
sudo pip install openai
```
### Basic notions of reinforced learning

There are two components that are important to understand:
- Agents
- Environment

The agents take actions into the environment. Their goal is to maximize the regard. For example Giraffes evolved because ones with the longest necks survived. Why? Because they could reach the upper branches and feed. They adapted to the environment. The section to maximize was ``neck length``. This is important because our agent is going to try to maximize that goal. If our agent is reaching that goal we're going to give him a "reward" so that it knows that is going in the right track. For example, this can be applied to teaching a dog to sit. Whenever the dog sits we give him a reward to it links the action of sitting with the treat. The dog will therefore try to maximize the amount of treats that he gets by adapting to the behaviour demanded (sitting). The following image reflects this interaction between agent and environment.

![image1](photos/agent_environment.svg)

### 1. Cartpole

In this exercise you should take a look at the comments made in the file ``cartpole.py``.
To follow this tutorial also refer to [this page](https://gym.openai.com/docs/) were it talks about the whole process.
Spaces are the range of action of the agent. What can the agent do?
