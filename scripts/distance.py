from scripts.utils import text_to_speech


def get_distance_affirmation(distance):
    response = f"Well done. You have travelled {distance} kilometers. " \
               f"We hope you enjoyed the exercise and the places that you " \
               f"visited!"
    text_to_speech(response)
    return response
