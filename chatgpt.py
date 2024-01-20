import asyncio
from openai import AsyncOpenAI
from config import OPENAI_TOKEN

content = """
    в рамках инициативы IAmRemarkable, девушка рассказывает о своем успехе и достижении.напиши
    мотивирующую фразу в дружественном виде в ответ. 
    """


client = AsyncOpenAI(api_key=OPENAI_TOKEN)


async def get_generated_phrase():
    stream = await client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": content}],
        stream=True,
    )

    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")

asyncio.run(main())
