import gym
env=gym.make('CartPole-v0')
def basic_policy(observation):
    angle=observation[2]
    return 0 if angle <0 else 1
for i_episode in range (20):
    observation=env.reset()
    for t  in range(100):
        env.render()
        action=basic_policy(observation)
        observation,reward,done,info=env.step(action)
        print(observation)
        if done:
           print("episode finished after {} timesteps".format(t+1))
           break
   
env.close()

