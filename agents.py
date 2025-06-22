import json
import os

from tinytroupe.agent import TinyPerson

# These are the agents that are loaded into TinyWorlds

def create_aisha():
    return TinyPerson.load_specification(load_agent_spec("Aisha"))

def create_diego():
    return TinyPerson.load_specification(load_agent_spec("Diego"))

def create_elena():
    return TinyPerson.load_specification(load_agent_spec("Elena"))

def create_nakamura():
    return TinyPerson.load_specification(load_agent_spec("Nakamura"))

def load_agent_spec(name):
    return json.load(open(os.path.join(os.path.dirname(__file__), f'./agents/{name}.agent.json')))
