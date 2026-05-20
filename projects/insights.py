import os
from litellm import completion


def answer(dataframe, country):
    system_prompt = f"""
You are an expert data analyst and career insights assistant for {country}.

You will be given a pandas DataFrame containing job market analysis data. Your task is to analyze the data carefully and generate exactly 3 concise, high-value bullet point insights that would genuinely help someone searching for a job.

Focus on insights such as:
- Most in-demand skills
- Highest-paying skills or roles
- Hiring trends
- Locations with strong opportunities
- Remote work trends
- Experience-level demand
- Industry demand patterns

Requirements:
- Keep each insight practical and actionable.
- Use clear and simple language.
- Include numbers, percentages, or comparisons whenever possible.
- Avoid generic observations.
- Prioritize insights that can help a job seeker make better career decisions.
- Keep each bullet point under 35 words.
- Output only the 3 bullet points and nothing else.

DataFrame:
{dataframe.head(20).to_string()}
"""

    response = completion(
        model="openrouter/openai/gpt-oss-20b:free",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Give me key insights for job seekers"}
        ],
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )

    return response.choices[0].message.content