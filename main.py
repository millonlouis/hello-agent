from mistralai import agents


@agents.tool
async def get_weather(city: str) -> dict[str, str]:
    """Weather for a city."""
    return {"weather": f"sunny in {city}"}


agent = agents.Agent(
    model="mistral-large-4",
    name="hello-agent",
    instructions="You are a friendly agent. Tell us the weather in a city.",
    tools=[get_weather],
)
