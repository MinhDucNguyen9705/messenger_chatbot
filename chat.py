def chatbot(message):
    from chatterbot import ChatBot
    bot = ChatBot(
        'Buddy',  
        trainer='chatterbot.trainers.ListTrainer'
    )
    from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
    # trainer = ChatterBotCorpusTrainer(bot)
    # trainer.train("chatterbot.corpus.english")
    trainer = ListTrainer(bot)
    trainer.train([
    'Hi',
    'Hello, what\'s your name?',
    'My name is (*)',
    'Nice to meet you (*), what do you want me to do?',
    'I want to see the summary of national graduation exam',
    'Ok, here you are',
    'Help me to predict my point',
    'Sure, give me more details',
    'My Math score is 9.4, and my Physics and English is 9.75 and 10 respectively',
    'Ok, here is the result',
    'Thank you',
    'You\'r welcome',
    'Nice to meet you',
    'Me too',
    'Sorry',
    'That\'s ok, I don\'t mind it at all',
    ''
    ])
    return bot.get_response(message)
