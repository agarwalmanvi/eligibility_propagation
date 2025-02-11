import os

def lowercase_rename( dir ):
    # renames all subforders of dir, not including dir itself
    def rename_all( root, items):
        for name in items:
            try:
                os.rename( os.path.join(root, name),
                                    os.path.join(root, name.lower()))
            except OSError:
                pass # can't rename it, so what

    # starts from the bottom so paths further up remain valid after renaming
    for root, dirs, files in os.walk( dir, topdown=False ):
        rename_all( root, dirs )
        rename_all( root, files)

if __name__ == "__main__":
    lowercase_rename("/tungstenfs/scratch/gzenke/agarmanv/data/TIMIT/TRAIN")
    lowercase_rename("/tungstenfs/scratch/gzenke/agarmanv/data/TIMIT/TEST")