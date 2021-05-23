from lib.plugins.Plugin import Plugin

class YouTube(Plugin):
    def __init__(self, data):
        super().__init__("YouTube",
                         "Gives the link to the first video of a youtube search",
                         ["youtube"])
        self.data = data


    def youtube(self, data):
        if not data["args"]:
            return "Error: youtube needs a message. Try: !h echo"

        try:
          title = " ".join(data["args"])
          search = VideosSearch(title, limit = 1)
          msg = search.result()["result"][0]["link"]
        except:
          msg = "No videos found"
        
        return msg