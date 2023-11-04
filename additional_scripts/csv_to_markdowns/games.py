import pandas as pd
from tabulate import tabulate

games = ["taboo", 
         "wordle", 
         "wordle_withclue", 
         "wordle_withcritic", 
         "imagegame", 
         "referencegame", 
         "privateshared" ]


descriptions = ["A game where one player tries to get the other player to guess a word without using certain 'taboo' words in their clues.",
    "A game where one player thinks of a word and the other player tries to guess it by suggesting words that are similar or related.",
    "A variant of Wordle where the guesser is given a clue to help them guess the target word.",
    "A variant of Wordle where the guesser's suggestions are evaluated by a third player, who provides feedback on their accuracy.",
    "A game where one player draws a picture and the other player tries to guess what it represents.",
    "A game where one player describes an object and the other player tries to identify it based on the description.",
    "A game where two players are given different pieces of information and must work together to solve a problem."
]

anchoring_process = ["incremental learning/processing",
                     "incremental learning/processing",
                     "incremental learning/processing",
                     "incremental learning/processing",
                     "multimodal grounding",
                     "multimodal grounding",
                     "conversational grounding"]

representational_domains = ["language model/world model",
                            "language model/world model",
                            "language model/world model",
                            "language model/world model",
                            "situation model",
                            "situation model",
                            "discourse model"]


data = {

    "games": games,
    "descriptions": descriptions,
    "anchoring processes": anchoring_process,
    "representational domains": representational_domains
}

df = pd.DataFrame(data)

# Convert dataframe to markdown
md = df.to_markdown(index=False)
# md = tabulate(md, headers='keys', tablefmt='pipe', stralign='center', numalign='center')
print(md)

file_name = "additional_scripts/output_markdowns/games.md"
with open(file_name, "w") as file:
    file.write(md)

# print(f"Markdown content saved to {file_name}")