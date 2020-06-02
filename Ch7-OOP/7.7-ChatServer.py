class User:

    def __init__(self, name):
        self.name = name
        self.history = []

    def send(self, message):
        self.history.append(message)

    def clear_history(self):
        self.history = []


class ChatServer:

    def __init__(self):
        self.participants = set()
        self.messages = []

    def join(self, participant):
        self.participants.add(participant)
        for message in self.messages[-8:]:
            participant.send(message)

    def leave(self, participant):
        if participant in self.participants:
            self.participants.remove(participant)
            participant.clear_history()

    def send_all(self, participant, text):
        message = [participant.name, text]
        self.messages.append(message)
        for p in self.participants:
            p.send(message)
