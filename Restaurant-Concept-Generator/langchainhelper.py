import os
import json

from dotenv import load_dotenv

load_dotenv()  # reads .env from project root automatically

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(temperature=0.7)
parser = StrOutputParser()



def get_restaurant_name_and_items(cuisine: str) -> dict:
    prompt = PromptTemplate(
        input_variables=["cuisine"],
        template=(
            "You MUST return valid JSON only. No markdown, no backticks, no extra text.\n"
            "Generate a fancy restaurant concept for {cuisine} cuisine.\n\n"
            "Return JSON with EXACT keys and types:\n"
            "{{\n"
            '  "restaurant_name": "string",\n'
            '  "cuisine": "string",\n'
            '  "menu_items": ["string","string","string","string","string","string","string","string"],\n'
            '  "price_range": "one of $, $$, $$$",\n'
            '  "target_customer": "short string",\n'
            '  "tagline": "short string"\n'
            "}}\n"
        ),
    )

    text = (prompt | llm | parser).invoke({"cuisine": cuisine}).strip()

    # Parse JSON
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Quick repair: extract JSON part if model adds extra text
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            return json.loads(text[start:end+1])
        raise
