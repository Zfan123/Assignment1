#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import sys
# sys.path.insert(0,'/home1/user/lr/aima-python-master')


# In[4]:


from agents import *

# from notebook import psource


# In[14]:


# psource(TrivialVacuumEnvironment)


# In[15]:


# These are the two locations for the two-state environment
loc_A, loc_B = (0, 0), (1, 0)

# Initialize the two-state environment
trivial_vacuum_env = TrivialVacuumEnvironment()

# Check the initial state of the environment
print("State of the Environment: {}.".format(trivial_vacuum_env.status))

# In[16]:


loc_A = (0, 0)
loc_B = (1, 0)

"""We change the simpleReflexAgentProgram so that it doesn't make use of the Rule class"""


def SimpleReflexAgentProgram(): #没用了，简单反射的函数我写在agent，调用model即可
    """This agent takes action based solely on the percept. [Figure 2.10]"""

    def program(percept):
        loc, status = percept
        if status == 'Dirty':
            return 'Suck'
        elif loc == loc_A:
            return 'Right'
        else:
            return 'Left'

    return program


# Create a simple reflex agent the two-state environment
program = SimpleReflexAgentProgram()
simple_reflex_agent = Agent(program)

# In[17]:

# Create a model-driven agent
simple_reflex_agent = Agent(program=ModelBasedVacuumAgent())

trivial_vacuum_env.add_thing(simple_reflex_agent)

print("ModelDrivenVacuumAgent is located at {}.".format(simple_reflex_agent.location))

for time_step in range(3):  # 执行三个时间步
    trivial_vacuum_env.step()
    print("Time Step: {}".format(time_step + 1))
    print("ModelDrivenVacuumAgent is located at {}.".format(simple_reflex_agent.location))
    print("State of the Environment: {}.".format(trivial_vacuum_env.status))
trivial_vacuum_env.delete_thing(simple_reflex_agent)
# In[22]:


table = {((loc_A, 'Clean'),): 'Right',
         ((loc_A, 'Dirty'),): 'Suck',
         ((loc_B, 'Clean'),): 'Left',
         ((loc_B, 'Dirty'),): 'Suck',
         ((loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
         ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
         ((loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck',
         ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
         ((loc_A, 'Dirty'), (loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
         ((loc_B, 'Dirty'), (loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck'
         }

# In[23]:


# Create a table-driven agent
table_driven_agent = Agent(program=TableDrivenVacuumAgent(table=table))

# In[25]:
# Add the table-driven agent to the environment
trivial_vacuum_env.add_thing(table_driven_agent)

print("TableDrivenVacuumAgent is located at {}.".format(table_driven_agent.location))

for time_step in range(3):  # 执行三个时间步
    trivial_vacuum_env.step()
    print("Time Step: {}".format(time_step + 1))
    print("TableDrivenVacuumAgent is located at {}.".format(table_driven_agent.location))
    print("State of the Environment: {}.".format(trivial_vacuum_env.status))





