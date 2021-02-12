from lib.plugins.Plugin import Plugin


class Echo(Plugin):
    def __init__(self, data):
        super().__init__("Echo",
                         "Repeats the msg. (limited to 400chars) cmd: !echo <msg>",
                         ["echo"])
        self.data = data


    def echo(self, data):
        if not data["args"]:
            return "Error: echo needs a message. Try: !h echo"

        msg = " ".join(data["args"])

        if len(msg) > 400:
            return "Error: message is too long. Try: !h echo"
        
        return msg