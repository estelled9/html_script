import httplib2
import re


class HTTPconnection:
    """ Connection instance HTTP """

    def __init__(self, language):
        self.language = language

    def get(self, page):
        h = httplib2.Http(".cache")

        self.url = "http://{0}.wikipedia.org/wiki/{1}".format(
            self.language,
            # page.replace(" ", "_")
            re.sub(r' ', '_', page)
        )

        response, content = h.request(self.url, "GET")
        """Return value is a tuple (response, content)"""
        print(response)


HTTPconnection("fr").get("Edward Snowden")
