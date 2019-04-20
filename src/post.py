"""
Post

Represents a post made by a user
"""

class Post():
    def __init__(self, author: str = "No Author", contents: str = "CAW CAW CAW"):
        self.author = author
        self.contents = contents

# TODO write a util for converting human text into "CAW"