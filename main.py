"""
_summary_
"""

if __name__ == "__main__":
    S: str = (
        "This is just some random text, there will be giberish asdf asdf"
        + " asdf asd fasdf asd fasd fasdf ads fas dfa sdf adsf"
    )

    S += "hola"

    FAIL = (
        "This will be longer and unaffected by black: adsf"
        "asdfas fdas fdas dfas fdas dfa sfd asdf asdf asdf sdf aasd fasdf"
        "asdfasdfasdfasdfasdfasdfafdasfdasdfasdfasdfa fafs  asdffasfff asdf asdfa "
        "dfadf asdf adf adsf asdf asdf adsf adsf asd fas"
    )

    T = (
        "asd asdf asdf asdf asdf adsf asdfa sdfa sdfa sdfa sdfas dfas dfasd fasdf asd fasd fasdf asdf asdf asdf "
        "adfsadf asdfasdfasdf asdf asdf asdfa sdfad sfas dfa sdfa sdf"
    )

    print(S)
    print(T)
