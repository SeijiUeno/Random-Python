import cowsay

def greeting(name: str = "42") -> None:
    """
    recives a name and prints a greeting, without a name, name = 42
    """
    cowsay.cow(f"Hello {name}")
