#import libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from cleaner import clean_corpus

#Creation of ChatBot object
my_chatbot = ChatBot("Byte",read_only=True,Logic_adapters=['chatterbot.logic.BestMatch'],storage_adapters="chatterbot.storage.SQLStorageAdapter")

#Train Chatbot with the built in library package
chatbot=ChatterBotCorpusTrainer(my_chatbot )
chatbot.train("chatterbot.corpus.english")

#Train Bot with whatsapp chat
CHAT_FILE= "chat.txt"

clean_pro_file=clean_corpus(CHAT_FILE)
trainer = ListTrainer(chatbot)
trainer.train(clean_pro_file)

#exit commands
exit_commands = (":q", "quit", "exit")

print("Hi! I'm Byte");
while True:
    query = input("you: ")
    if query in exit_commands:
        break
    else:
        print(f"bot: {my_chatbot.get_response(query)}")
