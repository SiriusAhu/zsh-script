from utils.utils import *
from utils.Interaction import *

def reset_zshrc():
    """
    reset zshrc to origin
    """
    origin_exist = os.path.exists(ORIGIN_PATH)
    if not origin_exist:
        print("  You can't reset zshrc to origin because you didn't backup it before.")
        tip_userContinue()
        return
    os.system(f"cp {ORIGIN_PATH} {HOME}/.zshrc")
    print("# Note: Reset #")
    print("\t.zshrc file has been reset to its original state.")
    tip_userContinue()

print("---- Reset Menu ----")
print("  This method will reset your .zshrc file to its original state,\n\twhich backed up at the first run.")
print("- Are you sure to reset? (Y/n)")
inpt = input()
if not tip_userMakeDecision(inpt):
    exit(0)
reset_zshrc()
exit(0)