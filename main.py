import asyncio

from mistralai import agents

@agents.tool
async def get_weather(city: str) -> dict[str, str]:
    """Weather for a city."""
    return {"weather": f"sunny in {city}"}

@agents.tool
async def get_forecast(city: str, days: int) -> list[str]:
    """Weather forecast for a city, one line per day."""
    return [f"day {day}: rain in {city}" for day in range(1, days + 1)]

agent = agents.Agent(
    model="mistral-large-4",
    name="hello-agent",
    instructions="You are a friendly agent. Tell us the weather in a city.",
    tools=[get_weather, get_forecast],
)

async def main() -> None:
    result = await agent.run("What's the weather in Paris?")
    print(result.text)

if __name__ == "__main__":
    asyncio.run(main())