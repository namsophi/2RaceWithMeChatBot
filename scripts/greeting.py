from scripts.utils import text_to_speech
import random

GREETINGS = ["Hey good to talk to you, ", "hello, ", "Good to see you, "]


def certain_greeting(name):
    response = random.choice(GREETINGS) + name
    text_to_speech(response)
    return response


def uncertain_greeting(name):
    response = f"Hello! Is this {name}?"
    text_to_speech(response)
    return response
