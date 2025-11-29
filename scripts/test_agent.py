from app.assistant import Agent

agent = Agent()

print(agent.run("What is the weather in Dhaka?"))
print(agent.run("Check weather for Chittagong"))
print(agent.run("Tell me weather in Sylhet"))