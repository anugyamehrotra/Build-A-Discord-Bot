# import libs & discord api

import discord
import random
import requests
import json

# apis
#api_key = ""  # tenor api

# helper functions
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

def get_gif(search_term="funny"):
    limit = 1
    # credits: anugya mehrotra @ https://github.com/anugyamehrotra
    response = requests.get(
        f"https://tenor.googleapis.com/v2/search?q={search_term}&key={api_key}&limit={limit}&media_filter=minimal"
    )
    if response.status_code == 200:
        data = response.json()
        return data["results"][0]["media_formats"]["gif"]["url"]
    else:
        return "https://media.tenor.com/fail.gif"

class MyClient(discord.Client):

    # credits: anugya mehrotra @ https://github.com/anugyamehrotra
    # logmessage replies
    def __init__(self, *, intents):
        super().__init__(intents=intents)
        self.waiting_for_reply = set() # greeting tracking
        self.waiting_for_rps = set() # rps tracking

    # user greetings
    greetings = [
        'hello'
        'yo',
        'sup',
        'hey',
        'heyy',
        'heyyy',
        'hi',
        'hii',
        'hiii',
        'what’s up',
        # credits: anugya mehrotra @ https://github.com/anugyamehrotra
        'wassup',
        'wazzup',
        'yo yo',
        'ayo',
        'hiya',
        'howdy',
        'what’s good',
        'what’s poppin',
        'yo fam',
        'sup fam',
        'yo dude',
        'yo bro',
        'hey there',
        'heyo',
        'hey fam',
        'yoooo',
        'hey hey',
        'ehyo',
        '’ello',
        'hola'
    ]

    # dyanmic bot replies section one
    dynamicReplies1 = [
        "Hey! I'm doing great, thanks for asking! How about you?",
        "Yo! All systems go here. What's good with you?",
        "Hey hey! Feeling fresh and ready to chat. How’s your day?",
        "Sup! Just chilling in the cloud. What’s up on your end?",
        "Hiya! I'm here and ready to roll. How you doing today?",
        "How’s it going?",
        "What’s up? How are you doing today?",
        "Hope you’re doing well! How’s everything?",
        "Hey! How’s your day treating you?",
        "Yo! How you feeling today?",
        "🎱 The 8-ball says: 'Outlook good!' How about you?",
        "🎱 Consulting the 8-ball... it says you're awesome today!",
        "🎱 The 8-ball says: 'Ask again later.' Just kidding, you're great!",
        "🎱 The 8-ball says: 'Signs point to yes!' Feeling lucky?",
        "🎱 Shaking the 8-ball... it says 'Absolutely!'"
    ]

    # dyanmic bot replies section two
    dynamicReplies2 = [
        "Hey! I'm doing great, thanks for asking! How about you?",
        "Yo! All systems go here. What's good with you?",
        "Hey hey! Feeling fresh and ready to chat. How’s your day?",
        "Sup! Just chilling in the cloud. What’s up on your end?",
        "Hiya! I'm here and ready to roll. How you doing today?",
        "🎱 The 8-ball says: 'Outlook good!' How about you?",
        "🎱 Consulting the 8-ball... it says you're awesome today!"
    ]

    # dyanmic bot replies section three
    # credits: anugya mehrotra 
    # @ https://github.com/anugyamehrotra
    dynamicReplies3 = [
        "Awesome! I'm glad to hear you're doing good.",
        "That's great news! Keep it up!",
        "Nice! Sounds like everything's going well.",
        "Sweet! Let’s keep that positive vibe going.",
        "Great to hear! This chat has been the highlight of my day so far!",
        "🎱 The 8-ball says: 'Outlook good!' How about you?",
        "🎱 Consulting the 8-ball... it says you're awesome today!",
        "🎱 The 8-ball says: 'Ask again later.' Just kidding, you're great!",
        "🎱 The 8-ball says: 'Signs point to yes!' Feeling lucky?",
        "🎱 Shaking the 8-ball... it says 'Absolutely!'"
    ]

    eight_ball_replies = [
        "🎱 Outlook good!",
        "🎱 Ask again later.",
        "🎱 Signs point to yes.",
        "🎱 Cannot predict now.",
        "🎱 Absolutely!",
        "🎱 Don't count on it.",
        "🎱 Very doubtful."
    ]

    bot_reqs = [
        # credits: anugya mehrotra @ https://github.com/anugyamehrotra
        "what do you do",
        "what can you do",
        "what are you for",
        "what's your purpose",
        "what are you here for",
        "what kind of stuff can you do",
        "what do you help with",
        "what can I ask you",
        "what are your skills",
        "what can I use you for",
        "how can you help me",
        "what are you good at",
        "what do you know",
        "what's your deal",
        "what can we talk about"
    ]

    bot_functions = [
        "Hi! I'm Magic Bot! I can do many things! \n I can talk to you with a simple hello. \n You can run $meme for a funny meme! \n You can run $gif for a funny gif! \n We can also play rock-paper-scissors! Just run $rps!"
    ]

    rock_paper_scissors_options = [ 
        "rock", 
        "paper",
        "scissors"
    ]
    
    # greeting function
    async def on_message(self, message):
        if message.author == self.user:
            return

        # user = Web Dev Tutorial @ NP Hacks
        author_id = message.author.id
        content = message.content.lower()

        # reply with section two - second_greeting
        if author_id in self.waiting_for_reply:
            await message.channel.send(random.choice(self.dynamicReplies3))
            self.waiting_for_reply.remove(author_id)
            return

        # reply with section one - initial_greeting
        if any(content.startswith(greet) for greet in self.greetings):
            await message.channel.send(random.choice(self.dynamicReplies1))
            self.waiting_for_reply.add(author_id)
            return

        # bot functionality info
        if any(content.startswith(ask_bot_question) for ask_bot_question in self.bot_reqs):
            for line in self.bot_functions:
                await message.channel.send(line)
            return
        # credits: anugya mehrotra @ https://github.com/anugyamehrotra

        # simple 8-ball replies
        if content.startswith('$8ball'):
            await message.channel.send(random.choice(self.eight_ball_replies))
            return

        # meme command
        if content.startswith('$meme'):
            await message.channel.send(get_meme())
            return

        # gif command
        if content.startswith('$gif'):
            await message.channel.send(get_gif())
            return
        
        if content.startswith('$rps'):
            await message.channel.send("Okay! 3..2..1.. Let's go! Type **rock**, **,paper**, or **scissors** to play!")
            self.waiting_for_rps.add(author_id)
            return
        
        if author_id in self.waiting_for_rps and content in self.rock_paper_scissors_options:
            bot_choice = random.choice(self.rock_paper_scissors_options)
            user_choice = content

            if user_choice == bot_choice:
                result = f"It's a tie! We both chose **{bot_choice}**."
            elif (user_choice == "rock" and bot_choice == "scissors") or \
                (user_choice == "paper" and bot_choice == "rock") or \
                (user_choice == "scissors" and bot_choice == "paper"):
                result = f"You win! I chose **{bot_choice}**."
            else:
                # credits: anugya mehrotra @ https://github.com/anugyamehrotra
                result = f"I win! I chose **{bot_choice}**."

            await message.channel.send(result)
            self.waiting_for_rps.remove(author_id)
            return
        
        if author_id in self.waiting_for_reply:
            await message.channel.send(random.choice(self.dynamicReplies3))
            self.waiting_for_reply.remove(author_id)
            return

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        # credits: anugya mehrotra @ https://github.com/anugyamehrotra


# init discord client
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
# client.run('')  # discord bot token

