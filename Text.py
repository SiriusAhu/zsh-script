class Text:
    def __init__(self) -> None:
        self.text_dont_worry = "Don't worry, the files will only be edited at the end of the process."

    def tip_userMakeDecision(self, inpt):
        """
        Enter, Y, y -> True
        N, n -> False
        else -> Invalid input!
        """
        if inpt not in ["", "Y", "y"]:
            if inpt not in ["n", "N"]:
                text_ = "Invalid input!"
                raise ValueError(text_ + "\n" + self.text_dont_worry)
            else:
                return False
        return True
    
    def tip_userContinue():
        # Press any key to continue
        print("- Press any key to continue...")
        input()