import gymnasium as gym

env = gym.make("HalfCheetah-v4", render_mode="rgb_array")

env = gym.wrappers.RecordVideo(env, "videos")

obs, _ = env.reset()

for _ in range(1000):
    action = env.action_space.sample()
    obs, reward, terminations, truncations, infos = env.step(action)
env.close()
