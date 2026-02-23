import os
from sys import version

from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import tool
from langchain_openai import AzureChatOpenAI

from agents import geocode_location, haversine_distance

load_dotenv(".env.local")


@tool
def geocoder(city: str) -> dict:
    """Converts city names to coordinates"""
    return geocode_location(city)


@tool
def distance_calc(coordinates: str) -> float:
    """Calculates distance between two locations given their coordinates."""
    # Ta bort extra ' och "
    coordinates = coordinates.replace("'", "").replace('"', "").strip()
    # Splitta på semikolon först för att få de två koordinatparen.
    coords = coordinates.replace(";", ",").split(",")
    coords = [float(x.strip()) for x in coords]
    lat1, lon1, lat2, lon2 = coords

    return haversine_distance({"lat": lat1, "lon": lon1}, {"lat": lat2, "lon": lon2})


tools = [geocoder, distance_calc]

llm = AzureChatOpenAI(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Användaren pratar med agenten
result = agent_executor.invoke(
    {"input": "Hur långt är det från Stockholm till Göteborg?"}
)
print(result)

# AI:n resonerar själv:
# "Jag behöver först koordinater för Stockholm... [anropar Geocoder]
#  Sedan koordinater för Göteborg... [anropar Geocoder]
#  Nu kan jag beräkna avståndet... [anropar DistanceCalc]"
#
