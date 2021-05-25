from lib.plugins.Plugin import Plugin

import lichess.api


class Lichess(Plugin):
    def __init__(self, data):
        super().__init__("Lichess",
                         "Interact with Lichess. cmds: !rating <name> [category]; !tv <name>",
                         ["rating", "tv"])
        self.data = data


    def rating(self, data):
        user = data["args"][0] if data["args"] else data["nick"]
        mode = data["args"][1] if len(data["args"]) > 1 else None

        linick = self.__lichess_username(user)

        try:
            user = lichess.api.user(linick)
        except lichess.api.ApiHttpError:
            return "User not found."

        msg = "%s: " % linick
        perfs = user["perfs"]
        
        if not perfs.keys(): 
            return "No information about user."

        if mode not in perfs:
            relevant_modes = set(["blitz", "rapid", "puzzle", "classical"])

            for mode in list(relevant_modes & set(perfs.keys())):
                msg += "%s: %d, " % (mode, perfs[mode]["rating"])

            msg = msg[:-2]
        else:
            msg += self.__format_rating(perfs, mode)

        return msg


    def tv(self, data):
        user = data["args"][0] if data["args"] else data["nick"]
        return "https://lichess.org/@/%s/tv" % self.__lichess_username(user)


    def __lichess_username(self, nick):
        lichess_usernames = self.data[self.name]["lichess_usernames"]

        if nick in lichess_usernames:
            return lichess_usernames[nick]
        else:
            return nick

    def __format_rating(self, perfs, mode):
        return "%s: %d (N=%d, Δ=%d, σ=%d)" % (mode, perfs[mode]["rating"], perfs[mode]["games"], perfs[mode]["prog"], perfs[mode]["rd"])