class ChatMediator:
    def __init__(self):
        self.__users = []

    def addUser(self, user):
        self.__users.append(user)

    def sendMessage(self, message):
        for user in self.__users:
            user.rcvMessage(message)

    def getUsers(self):
        return self.__users


class User:
    def __init__(self, name, chatRoom):
        self.__name = name
        self.__messages = []
        self.__chatRoom = chatRoom
        chatRoom.addUser(self)

    def sendMessage(self, message):
        self.__chatRoom.sendMessage(self.__name + " says: " +message)

    def rcvMessage(self, message):
        self.__messages.append(message)

    def getMessages(self):
        return self.__messages


if __name__ == "__main__":
    chatRoom = ChatMediator()

    robert = User("Robert", chatRoom)
    john = User("John", chatRoom)
    susan = User("Susan", chatRoom)

    robert.sendMessage("Hi guys!")
    susan.sendMessage("Hi Bob!")
    john.sendMessage("I hate you all")

    for user in chatRoom.getUsers():
        print(user.getMessages())
