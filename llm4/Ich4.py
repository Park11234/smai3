from langchain.agents import load_tools, initialize_agent, AgentType

from MyLCH import getOpenAI, getGenAI

if __name__ == '__main__':
    openllm = getOpenAI()
    genllm = getGenAI()

    tools = load_tools(['wikipedia','llm-math'], llm=openllm)

    agent = initialize_agent(
        tools,
        openllm,
        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose = True
    )

    txt = "트럼프가 태어난 해는? 2025년도 트럼프는 몇 살? 한국어로 대답해줘"
    print(agent.run(txt))

