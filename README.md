# Fire Fighter – Reinforcement Learning Project

A Deep Reinforcement Learning agent designed to **fight forest fires**, navigate obstacles, and protect the environment using **DQN** and **Policy Gradient** algorithms.

---

## Project Intro Video

<img src="src\assets\agent&env.gif" width="600" />

---

##  Overview

The **Fire Fighter RL Project** is a simulation environment where an intelligent agent learns how to *detect, reach, and extinguish* fires on a **grid-based forest environment**.
The project models the behavior of fires spreading across trees and challenges the agent to control and reduce the damage effectively.

---

##  Project Objectives

1. **Extinguish Fires**

   * The agent’s primary mission is to put out all fires in the forest.

2. **Prevent Fire Spread**

   * Fires can spread to healthy trees. The agent must take action quickly.

3. **Avoid Obstacles**

   * The grid contains obstacles that restrict movement.

4. **Maximize Efficiency**

   * The agent learns to achieve goals with minimal steps and time.

---

##  Environment Description

The environment is a 2D grid containing:

* **Empty Cell** → free movement
* **Tree** → healthy tree that must be protected
* **Fire** → burning cell that must be extinguished
* **Obstacle** → agent cannot pass through

The environment updates every timestep, allowing fire to spread if not controlled.

---

## 🤖 Agent Actions

The agent can perform:

* Move **Up / Down / Left / Right**
* **Extinguish Fire** at its current position

###  Reward System

* **+ Reward** for extinguishing fires
* **+ Reward** for preventing the spread
* **– Penalty** for delayed actions
* **– Penalty** when fire spreads to new trees

---

##  Algorithms Used

### Built Deep Q-Network (DQN) from scratch

DQN approximates the Q-value function using a neural network.

**Training Pipeline:**

1. Initialize Q-Network + Target Network
2. Store transitions (state, action, reward, next_state)
3. Sample batches from Replay Buffer
4. Compute Q-targets
5. Compute MSE Loss
6. Update Q-Network via Gradient Descent
7. Periodically update Target Network


---

### Built Policy Gradient (PG) from scratch

Policy Gradient directly optimizes the probability distribution of actions.

**Training Pipeline:**

1. Initialize Policy Network
2. Collect trajectories (states, actions, rewards)
3. Compute discounted cumulative rewards
4. Compute policy gradient
5. Update the policy using Gradient Ascent


##  PG with Environment using weights

> go to src\assets\agent_using_PG_model_weights.wmv
