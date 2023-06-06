
class Console:
    level = 0

    @staticmethod
    def ask(question):
        question = '[?] ' + str(question) + ' : '
        return input(question)

    @staticmethod
    def info(message):
        message = '[+] ' + str(message)
        print(message)

    @staticmethod
    def error(message):
        message = '[!] ' + str(message)
        print(message)
