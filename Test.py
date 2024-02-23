import re
def parse_url(link):
    # true then good link!
    if re.match("(http|https)://", link):
        return link
    if re.match("[A-Za-z0-9+&@#\/%?=~_|!:,;]*[.]*[a-z0-9+&@#\/%=~_|]", link):
        return "https://" + link
    return False


print("is www.==https://www..", parse_url("www.") == "https://www.")
