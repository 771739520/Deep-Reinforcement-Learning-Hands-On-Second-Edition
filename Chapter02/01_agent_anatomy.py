import random
from typing import List


class Environment:
    def __init__(self):
        self.steps_left = 10

    def get_observation(self) -> List[float]:#->是函数返回值的注释
        return [0.0, 0.0, 0.0]

    def get_actions(self) -> List[int]:
        return [0, 1]

    def is_done(self) -> bool:
        return self.steps_left == 0

    def action(self, action: int) -> float:
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random()


class Agent:
    def __init__(self):
        self.total_reward = 0.0

    def step(self, env: Environment):#参数后的冒号是函数注释，如果有特定的值需要标记（https://cloud.tencent.com/developer/article/1573221）网站有详解
        current_obs = env.get_observation()#这个变量是没有用的
        actions = env.get_actions() #带上小括号就是调用函数了，这里就是调用了class Environment 里的get_actinons函数
        reward = env.action(random.choice(actions))#actions是形参，里面的0或者1是实参。实参就是真实的数值，形参就是变量名
        self.total_reward += reward


if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print("Total reward got: %.4f" % agent.total_reward)
