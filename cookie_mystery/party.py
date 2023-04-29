from typing import List, Dict
from cookie_mystery.bot import Bot
from cookie_mystery.prompts import bots
import random

class Party:
    states = ["Irritable", "Upbeat", "Dour"]
    relations = ["Love", "Hate", "are positively disposed towards"]
    def __init__(self, bots:Dict[str,str])->None:
        self.bots = []
        for name, char_prompt in bots.items():
            state = random.sample(self.states,1)
            bot_relations = []
            for name2, _ in bots.items():
                relation = random.sample(self.relations,1)
                bot_relations.append(f"You {relation} {name2}")
            char_prompt = [f"""You are stranded on an island. This is your character:\n\n{char_prompt}."""]
            char_prompt.append(f"You are {state}")
            char_prompt += bot_relations
            self.bots.append(Bot(name, char_prompt))
                