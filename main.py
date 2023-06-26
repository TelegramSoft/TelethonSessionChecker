import asyncio
import json
import os
import shutil
import sqlite3

from telethon import TelegramClient


async def main():
    try:
        os.mkdir("bad_sessions")
    except FileExistsError:
        pass

    gc = 0
    to_move = []

    for file in os.listdir():
        if os.path.isfile(file):
            filename, extension = file.split(".")
            if extension != "session":
                continue

            with open(f"{filename}.json", "r") as json_file:
                json_data = json.load(json_file)

            try:
                client = TelegramClient(filename, json_data["app_id"], json_data["app_hash"])
            except sqlite3.DatabaseError:
                print(f"Bad session: {filename}")
                to_move.append(filename)
                continue
            except Exception as err:
                print(f"Bad session: {filename} with error {err.__class__.__name__}")
                to_move.append(filename)
                continue

            try:
                await client.connect()
                if not await client.is_user_authorized():
                    await client.disconnect()
                    print(f"Bad session: {filename}")
                    to_move.append(filename)
                else:
                    gc += 1
                    await client.disconnect()
            except Exception as err:
                await client.disconnect()
                print(f"Bad session: {filename} with error {err.__class__.__name__}")
                to_move.append(filename)
                continue

    for filename in to_move:
        shutil.move(f"{filename}.session", f"bad_sessions/{filename}.session")
        shutil.move(f"{filename}.json", f"bad_sessions/{filename}.json")

    print(f"There are {gc} working sessions")

    input("Press enter to close the window")


if __name__ == '__main__':
    asyncio.run(main())
