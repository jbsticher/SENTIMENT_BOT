from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float

def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity
    """must pass in name of 'sensitivy when calling function because of *(asterik)"""
    friendly_threshold: float = sensitivity
    hostile_threshold: float = sensitivity

    if polarity >= friendly_threshold:
        return Mood('😀', polarity)
    elif polarity <= hostile_threshold:
        return Mood('😠', polarity)
    else:
        return Mood('😐', polarity)    
    

def run_bot():
    print('\n***Welcome to the Python Setntiment Analyzer("q" to quit).***\n')
    while True:
        user_input: str = input('You: ')
        if user_input.lower().startswith('q'):
            print('\nThank you for stopping by.')
            break
        else:
            mood: Mood = get_mood(user_input, sensitivity=0.3)
            print(f'Bot: {mood.emoji} ({mood.sentiment})')

if __name__ == '__main__':
    run_bot()