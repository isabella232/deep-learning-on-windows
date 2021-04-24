import gym
env = gym.make('MountainCar-v0')
observation = env.reset()
for step_index in range(1000):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print("Step {}:".format(step_index))
    print("action: {}".format(action))
    print("observation: {}".format(observation))
    print("reward: {}".format(reward))
    print("done: {}".format(done))
    print("info: {}".format(info))
    if done:
        break
observation = env.reset()
env.close()