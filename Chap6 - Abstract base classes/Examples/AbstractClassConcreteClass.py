from AbstractClassExample import MediaLoader

class Wav(MediaLoader):

    """
    Cannot create object since it does not implement abstract methods
    Need to implement both of them
    """
    pass

class Ogg(MediaLoader):

    ext = ".ogg"

    def play(self) -> None:
        print("playing ogg file")