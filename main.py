import json
import sys
from dotenv import load_dotenv

from agents import create_diego, create_aisha, create_elena, create_nakamura

# sys.path.insert(0, '..')

import tinytroupe
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld, TinySocialNetwork
# from tinytroupe.examples import *

# Load environment variables from .env file
load_dotenv()

world = TinyWorld("Focus group", [create_diego(), create_aisha(), create_elena(), create_nakamura()])

world.broadcast("""
                Hello everyone! Let's start by introducing ourselves. What is your job and what are some major problems you face 
                in your work? What are major challenges for your industry as a whole? Don't discuss solutions yet, 
                just the problems you face.
                """)

world.run(1)
