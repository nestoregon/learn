# Book

In order to learn faster I have bought the following book
- Deep Reinforcement Learning Hands-On (Maxim Lapan 2018)
I will be covering everything I am learning in this file. The book is aimed for people that already know how NN work and a strong background in Python and Mathematics.

## Chapter 1
This chapter is an introduction to concepts.
Reinforcement Learning (RL) its a Machine Learning (ML) subdivision in which we try to solve problems. It differs from Supervised Learning, where we fit an algorithm to fit some training data, and Unsupervised Learning, where we cluster the data. What is then done differently? Among an environment with high uncertainty an agent tries to maximize certain actions while getting some feedback (rewards). This is how dogs learn, how humans learn and how machines can adapt to changing environments instead of being fixed. I suggest you do your own research about the things that you can do and apply.  
It defines Reinforced Learning key ideas such as the agent, environment, actions, reward, observations etc.  
Basically our agent is going to be interacting with its environment. How does it do so? Well it can act on it (actions) and it receives feedback from the environment. It receives observations of its state, and a reward (if appropriate). The reward is a very important concept in RL, given that this is how humans learn. In the following image you can see how the agent interacts with its environment.  
![Agent interacting with the environment](photos/agent_environment.svg)  

Then we are introduced to Markov. Who is this guy and why is he famous? He is famous to have coined the term Markov Processes, which is basically an interaction between states. States are linked with other states in the form of a matrix. The value of the matrix is the probability of changing from state A to state B. The most basic example of this is the weather.  

We can have sunny and cloudy weather. If we are in a sunny state we can change to a rainy state or stay sunny. The probabilities are shown in the table below

||Sunny|Rainy|
|---|---|---|
|Sunny|0.8|0.2|
|Rainy|0.1|0.9|
  
The present state is shown in vertical (sunny rainy) and the following state is the horizontal. For example there is a 0.1 probability of changing from Rainy to Sunny weather. Of course this is not perfect, Markov Processes assumes that the current state has no implications over the past state. This is to say that we don't care what the previous states were, we only focus on the weather right now.
  
**Markov Reward Process**. To make matters more accurate we introduce the concept of reward into the mix. The reward is a feedback given when we change from one state to the other.
  
||Sports|Sleep|
|---|---|---|
|Sports|1|3|
|Sleep|4|-1|
  
The reward matrix shows the rewards if we change from one state to the next. The probabilities of actually doing so are presented in the table below.
  
||Sports|Sleep|
|---|---|---|
|Sports|0.4|0.6|
|Sleep|0.3|0.7|
  
As you can see there are 2 matrices, the transition matrix (Markov Process) and the reward matrix. There is now another new concept called **return** which is basically the sum of all future rewards. This is modelled by a variable (B). If B=0 i only take into account the present rewards. IF B=1 I have infinite visibility.
To know the value of each state we multiply the rows of both matrices (do not multiply row * column as is done in regular matrix multiplication).

**Value of state**  
Sports = 1*0.4 + 3*0.6 = 0.4+1.8 = 2.2  
Sleep = 4*0.3 + (-1)*0.7= 1.2 - 0.7 = 0.5  

As we can see, on average is more profitable to be in the state of Sports.
  
Finally, the **Markov Decision Process (MDP)** is taking everything into account. Similarly to the Markov Reward Process (MRP) we now include a third dimension which are the actions. If previously we had 2 2D matrices (transition and reward) now we add a third coordinate to both of them called "actions". What are actions? The possible actions that I can take in that state. Given a transition to one state to the next I have different probabilities for every action that I want to take. This values are randomized in order to adapt to the environment.

Well after all this theory I think you're ready for the next chapter.
  
## Chapter 2: OpenAI Gym

Open AI is a platform used developing reinforcement learning algorithms.
There are two entities:  
- Agent
- Environment
These entities can ACT on the environment, receive OBSERVATIONS and REWARDS from the environment.
When we perform an ``action`` on an environment we obtain 4 things:
- observation: How is the environment now
- reward: What is the reward for that action
- done: Is the situation done? This is because we have lost probably
- extra_information: Usually called ``_`` because we don't want to use it.
We can also ``.reset()`` the environment to start again after the simulation is done and at the beginning of each iteration.  
There are many environments for us to play around with.  

## Chapter 3: Deep Learning with PyTorch

It teaches us the ML tool that we'll be used to develop our applications.
The first important concept is a tensor. A tensor is basically a 1D, 2D, 3D array that can be used to calculate different gradients needed.
Creation of tensors:
```python
import torch
import numpy as np
a = torch.FloatTensor(3,2) # these are the dimensions of the tensors
```
For example we can also create a 3 x 2 matrix using this
```python
a = torch.FloatTensor([[1,2],[1,5],[2,9]]) #3x2 matrix
n = np.zeros(shape=(3,2))
a = torch.tensor(n) # cast to transform from np to tensor
```
Watch out for the double ``[`` when creating a 2D tensor. For every dimension we put extra ``[``. Gradients are calculated when we create a NN. Why? Because we need it in order to optimize the network and change its values. 

Gradient meaning:
>Put simply, a gradient is a vector. Its components consist of the partial derivatives of a function and it points in the direction of the greatest rate of increase of the function

Gradient descent meaning:
> Gradient descent is an optimization algorithm used to minimize some function by iteratively moving in the direction of steepest descent as defined by the negative of the gradient. In machine learning, we use gradient descent to update the parameters of our model.

Now we can create a NN. What do we use? Tensors and activation funtions. The most common activation function is ``ReLU``. Google definition:
> ReLU stands for rectified linear unit, and is a type of activation function. Mathematically, it is defined as y = max(0, x). Visually, it looks like the following: ReLU is the most commonly used activation function in neural networks, especially in CNNs

![Relu](photos/relu.png)

Basically Relu is the function y=x but negative values are not taken into account. The following code explains how ReLU works:

```python
def relu(x):
    y = x
    if x<0:
        y = 0
    return y
```

Building a NN. We can use the ``nn`` class in torch to build the NN. You can see the process in the following code. We use two building blocks:
- nn.Linear to display the two layers (input and output)
- nn.ReLU to set the activation function
```python
import torch
model = torch.nn.Sequential(
    torch.nn.Linear(4, 3),
    torch.nn.ReLU(),
    torch.nn.Linear(3, 4),
)
```

The above code will generate a NN with this layout:
![NN](photos/nn_434.png)

|Layer|Number of Neurons|
|---|:---:|
|Input|1|
|Hidden|4|
|Output|4|  


### Loss funtions
Calculate how well the Network is doing. This is done by having an output that we can compare it with. Why is this model bad? 
### Optimizers
Given the loss and the current layer, how can I improve it? Common optimizers below.
- ADAM 
- SGD

### Monitoring the progress of the training
This is specially usegul because we need to know how the model is doing right now. The book recommends TensorBoard (which depends on tensorflow.)
> This is the MatplotLib of ML ~ Nestor 2020





