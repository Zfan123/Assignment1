from search import Problem, breadth_first_tree_search

class my_传教士与野人(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def actions(self, state):
        actions = []
        # 生成当前状态的所有可能行动
        for m in range(3):#传教士
            for c in range(3):#野人
                if 1 <= m + c <= 2:#船每次1，2人
                    actions.append((m, c))#上船，转移
        return actions

    def result(self, state, action):
        # 应用行动到当前状态以得到新状态
        new_state = [state[0], state[1], state[2]]
        if 0<=state[0]<=3 and 0<=state[1]<=3:
            if state[2] == 1:
                # 如果船在左岸，减去传教士和野人 船走减去人
                new_state[0] -= action[0]
                new_state[1] -= action[1]
                new_state[2] = 0
            else:
                # 如果船在右岸，增加传教士和野人 船会来加人
                new_state[0] += action[0]
                new_state[1] += action[1]
                new_state[2] = 1
            print("状态转移：从{}到{}".format(state, new_state))  # 打印状态转移
        return tuple(new_state)

    def goal_test(self, state):
        return state == self.goal

# 定义初始状态和目标状态
initial_state = (3, 3, 1)
goal_state = (0, 0, 0)

# 创建问题实例，将所有情况用图连起来
problem = my_传教士与野人(initial_state, goal_state)

# 使用广度优先树搜索解决问题
solution_node = breadth_first_tree_search(problem)

if solution_node:
    # 提取达到目标状态的一系列行动
    actions = solution_node.solution()
    print("找到解决方案，共 {} 步:".format(len(actions)))
    for step, action in enumerate(actions):
        print("第 {} 步：移动 {} 传教士和 {} 野人到{}岸".format(step + 1, action[0], action[1], "左" if step % 2 == 0 else "右"))
else:
    print("未找到解决方案。")
