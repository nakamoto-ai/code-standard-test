"""
_summary_
"""

if __name__ == "__main__":
    s: str = (
        "This is just some random text, there will be giberish asdf asdf"
        + " asdf asd fasdf asd fasd fasdf ads fas dfa sdf adsf"
    )

    s += "hola"

    fail = "This will be longer and unaffected by black: adsf asdfas fdas fdas dfas fdas dfa sfd asdf asdf asdf sdf adfasff"
    print(s)
