from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain import hub
from agents import geocode_location, haversine_distance

@tool
def geocoder(city: str) -> dict:
    """Converts city names to coordinates"""
    return geocode_location(city)

@tool
def distance_calc(coordinates: str) -> float:
    """Calculates distance between two locations given their coordinates."""
    # Ta bort extra ' och "
    coordinates = coordinates.replace("'", "").replace('"', "").strip()
    coords = [float(x.strip()) for x in coordinates.split(',')]
    lat1, lon1, lat2, lon2 = coords

    return haversine_distance(
        {"lat": lat1, "lon": lon1},
        {"lat": lat2, "lon": lon2}
    )
tools = [geocoder, distance_calc]

# Create AI agent
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key="din api nyckel"
)
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Användaren pratar med agenten
result = agent_executor.invoke({
    "input": "Hur långt är det från Stockholm till Göteborg?"
})
print(result)

# AI:n resonerar själv:
# "Jag behöver först koordinater för Stockholm... [anropar Geocoder]
#  Sedan koordinater för Göteborg... [anropar Geocoder]
#  Nu kan jag beräkna avståndet... [anropar DistanceCalc]"
#