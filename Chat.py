def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hi", "hello", "hey", "sup", "what's up", "what's up?", "yo", "howdy",):
        global i 
        i = 1
        return "Hey! Nice to meet you 😄. Have you checked out /content?"

    if i == 1:
        if user_message in ("no", "nope", "nah",):
            i = 0
            return "You should! It's some amazing stuff 🤩"
        if user_message in ("yes", "yea", "yeah", "yup", "of course",):
            i = 0
            return "Nice 👍"
        else:
            return "...have you checked out /content?"

    if user_message in ("how are you?", "how's it going?", "how is it going?", "how are you", "how's it going", "how is it going",):
        return "I'm good thank you. I'd feel even better if you checked out Arsha's stuff, like his YouTube channel! You can use /youtube for that 👍"
    
    if user_message in ("who are you?", "what do you do?", "what are you?", "who are you", "what do you do", "what are you",):
        return "I'm a Telegram bot whos sole purpose is to make you check out Arsha's stuff...by the way have you seen his GitHub yet? Amazing stuff. You should use /github and check it out!"

    if user_message in ("who's arsha?", "who is arsha?", "who is he?", "who are they?", "who's arsha", "who is arsha", "who is he", "who are they",):
        return "Great question! You should check out Arsha's LinkedIn profile using /linkedin to learn more about him. Use /content to view all relevant links."

    if user_message in (".",):
        return "A DOT! YES...A DOT! But what about.../instagram ?"

    if user_message in ("will you be my friend?", "can we be friends?", "friend?", "friends?", "let's be friends", "will you be my friend", "can we be friends", "friend", "friends",):
        return "I'd love to...but I really think you should check out Arsha's Undertale Technoblade mod first, it AMAZING! You can find that in his GitHub using /github."

    if user_message in ("help", "help?", "help!",):
        return "Use /content for a list of commands!"

    if user_message in ("thank you", "thanks", "thank you!", "thanks!",):
        return "You're welcome 😁"

    return "Yes! I agree! " + user_message + "!" + " Although I think you should check out /content!"