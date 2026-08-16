import asyncio
import asyncpg

async def run():
    try:
        conn = await asyncpg.connect("postgresql://prpilot:prpilot_password@localhost:5432/prpilot_db")
        print("Success!")
        await conn.close()
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(run())
