import argparse
from pathlib import Path
import pandas as pd


def annotations_to_tsv(args):
    """Retrieve annotations and save as tsv
    
    Args:
        args (argparse.Namespace): dict containing path to directory to read from
    """
    dst =  Path(args.dst)
    codes = []
    stanzas = []

    for e in dst.iterdir():
        if e.suffix == ".txt":
            st = e.read_text().split("\n\n")[:-1]
            for s in st:
                lines = s.split("\n")
                codes.append(lines[0])
                stanzas.append("\n".join(lines[1:]))

    poem_df = pd.DataFrame({"rhyme scheme":codes, "stanza": stanzas})
    poem_df.to_csv(f"tsvs/{dst.name}_rhymes_poems.tsv", sep="\t", index=False)

    print(f"All annotations saved to <tsvs/{dst.name}_rhymes_poems.tsv>.")

def check_dir(args):
    """Check that the directory containing annotation exists.
    
    Args:
        args (argparse.Namespace): dict containing path to directory to read from
    """
    directory = Path(args.dst)
    if directory.exists() and directory.is_dir():
        print(f"Directory <{directory}> exists.")
    else:
        print(f"Directory <{directory}> does not exist. Exiting program.")
        exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cleanup rhyme scheme codes and put annotations into a nice tsv")
    parser.add_argument("dst", type=str,
                        help="path to directory where produced annotations are saved")

    args = parser.parse_args()

    check_dir(args)
    annotations_to_tsv(args)