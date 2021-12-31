import os
import openai
from openai.openai_object import OpenAIObject
from serendipiart.config import Config

openai.api_key = Config.OPENAI_API_KEY
PROMPT = """
This is an image name generator

1. Colourful Shapes
2. Light All Over
3. Voronoi Masterpiece
4. Lucid Dreams
5. Naughty by Nature
6. Bad and Beyond
7. Rainbow Rain
8."""


def get_caption() -> str:
    response: OpenAIObject = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt=PROMPT,
        temperature=1,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["9."],
    )

    caption: str = response.choices[0].text.strip()
    return caption
