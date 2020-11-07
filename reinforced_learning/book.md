# Book

In order to learn faster I have bought the following book
- Deep Reinforcement Learning Hands-On (Maxim Lapan 2018)
I will be covering everything I am learning in this file. The book is aimed for people that already know how NN work and a strong background in Python and Mathematics.

## Chapter 1
This chapter is an introduction to concepts.
It defines Reinforced Learning key ideas such as the agent, environment, actions, reward, observations etc.
Basically our agent is going to be interacting with its environment. How does it do so? Well it can act on it (actions) and it receives feedback from the environment. It receives observations of its state, and a reward (if appropriate). The reward is a very important concept in RL, given that this is how humans learn. In the following image you can see how the agent interacts with its environment.  
![Agent interacting with the environment](photos/agent_environment.svg)

Then we are introduced to Markov. Who is this guy and why is he famous? He is famous to have coined the term Markov Processes, which is basically an interaction between states. States are linked with other states in the form of a matrix. The value of the matrix is the probability of changing from state A to state B. The most basic example of this is the weather. 

We can have sunny and cloudy weather. If we are in a sunny state we can change to a rainy state or stay sunny. The probabilities are shown in the table below

	Sunny	Rainy
Sunny	0.8	0.2
Rainy	0.1	0.9

The present state is shown in vertical (sunny rainy) and the following state is the horizontal. For example there is a 0.1 probability of changing from Rainy to Sunny weather. Of course this is not perfect, Markov Processes assumes that the current state has no implications over the past state. This is to say that we don't care what the previous states were, we only focus on the weather right now.

To make matters more accurate we introduce the concept of reward into the mix. The reward is a feedback given when we change from one state to the other.

        Sports	Sleep
Sports	1	3	
Sleep	4	-1

The reward matrix shows the rewards if we change from one state to the next. The probabilities of actually doing so are presented in the table below.

	Sports	Sleep
Sports	0.4	0.6
Sleep	0.3	0.7

As you can see there are 2 matrices, the transition matrix (Markov Process) and the reward matrix. There is now another new concept called **return** which is basically the sum of all future rewards. This is modelled by a variable (B). If B=0 i only take into account the present rewards. IF B=1 I have infinite visibility.
