import argparse
import string 
from pathlib import Path
import pandas as pd


def clean_scheme(scheme):
    letters = "---"+string.ascii_uppercase.replace("T", "").replace("I","").replace("N","")

    def scheme_to_numeric(scheme):
        scheme = scheme.replace("T", "0")
        scheme = scheme.replace("I", "1")
        scheme = scheme.replace("N", "2")
        unique_chars = (set(scheme) - {"0", "1", "2"})
        unique_chars = sorted(list(unique_chars), key=lambda x: scheme.index(x))
        scheme = "-".join(scheme)    
        for i, c in enumerate(unique_chars, start=3):
            scheme = scheme.replace(c, str(i))
        return scheme

    def numeric_to_scheme(scheme):
        unique_chars = sorted(list(set(scheme.split("-")) - {"0", "1", "2"}), key=int)
        for i, c in enumerate(unique_chars, start=3):
            scheme = scheme.replace(c, letters[i])
        scheme = scheme.replace("-", "")
        scheme = scheme.replace("0", "T")
        scheme = scheme.replace("1", "I")
        scheme = scheme.replace("2", "N")
        return scheme

    scheme = scheme_to_numeric(scheme)
    scheme = numeric_to_scheme(scheme)
    return scheme

def annotations_to_tsv(args):
    """Retrieve annotations and save as tsv
    
    Args:
        args (argparse.Namespace): dict containing path to directory to read from
    """
    dst =  Path(args.dst)
    schemes = []
    stanzas = []
    filenames = []
    indexes = []

    for e in dst.iterdir():
        if e.suffix == ".txt":
            st = e.read_text().split("\n\n")[:-1]
            for i, s in enumerate(st):
                lines = s.split("\n")
                scheme = clean_scheme(lines[0])
                schemes.append(scheme)
                stanzas.append("\n".join(lines[1:]))
                filenames.append(e.name)
                indexes.append(i)

    poem_df = pd.DataFrame({"rhyme scheme":schemes, "stanza": stanzas, "filename": filenames, "stanza number (in file)": indexes})

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