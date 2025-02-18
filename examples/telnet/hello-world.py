#!/usr/bin/env python
"""
A simple Telnet application that asks for input and responds.

The interaction function is a prompt_toolkit coroutine.
Also see the `hello-world-asyncio.py` example which uses an asyncio coroutine.
That is probably the preferred way if you only need Python 3 support.
"""
import logging
from asyncio import Future, run

from prompt_toolkit.contrib.telnet.server import TelnetServer
from prompt_toolkit.shortcuts import PromptSession, clear

# Set up logging
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


async def interact(connection):
    clear()
    connection.send("Welcome!\n")

    # Ask for input.
    session = PromptSession()
    result = await session.prompt_async(message="Say something: ")

    # Send output.
    connection.send(f"You said: {result}\n")
    connection.send("Bye.\n")


async def main():
    server = TelnetServer(interact=interact, port=2323)
    await server.run()


if __name__ == "__main__":
    run(main())
