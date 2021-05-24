from lib.plugins.Plugin import Plugin
from youtube_search import YoutubeSearch

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
          result = YoutubeSearch(title, max_results=1).to_dict()
          if len(result) < 1 :
              msg = "No videos found"
          else :
              msg = result[0]["title"] + " : " + "https://youtube.com" + result[0]["url_suffix"]
        except:
          msg = "No videos found"
        
        return msg
