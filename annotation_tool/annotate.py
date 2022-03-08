import argparse
from pathlib import Path

def annotate(args):
    """Main loop for rhyme scheme annotation. Lets the user annotate provided stanzas
    Args:
        args (argparse.Namespace): namespace containing path to directories to read/write from/to
    """


    print("""
    =============================================================================================

        It's time for annotation! 
        You should have read the guidelines at annotation_guildelines.md (or else...!)
        Please feel free to quit at any time by typing <q> or <quit>

    =============================================================================================""")
    source_dir = Path(args.source_dir)
    out_dir = Path(args.dir)
    
    source_poems = sorted(list(source_dir.iterdir()))
    out_poems = sorted(list(out_dir.iterdir()))

    already_annotated_poems = len(out_poems)

    if already_annotated_poems > 0:
        print(f"""
    You have already started annotating. 
    Starting where you left off (assuming the source dir is the same as last time).
    ----------------------------------------------------------------------------------------------""")
        prev_poem_i = already_annotated_poems-1
    else:
        prev_poem_i = 0

    for i in range(prev_poem_i, len(source_poems)):
        poem = source_poems[i]

        content = poem.read_text()[:-1] #remove added newline to the end of text
        stanzas = content.split("\n\n")

        name = poem.name[:-4]
        out_file = out_dir / f"{name}_annotated.txt"
        if out_file.exists():
            content = out_file.read_text()[:-1]
            annotated_stanzas = content.split("\n\n")

            missing_stanzas = (len(stanzas) - len(annotated_stanzas))
            if annotated_stanzas[-1] == "": 
                missing_stanzas += 1
                
            if missing_stanzas:
                stanzas = stanzas[-missing_stanzas:]
            else:
                continue        
        
        print(f"""
    Annotating {poem}
    ----------------------------------------------------------------------------------------------
        """)

        for stanza in stanzas:
            annotation = annotate_stanza(stanza)
            
            # the user is done
            if not annotation:
                return
            with out_file.open("a+") as f:
                f.write(annotation)
                f.write("\n\n")

def annotate_stanza(stanza):
    """Lets the user annotate one stanza
    
    Args: 
        stanza (str): the stanza to annotate

    Returns:
        str: the annotated stanza
    """
    lines = stanza.split("\n")
    #longest_line_length = max([len(line) for line in lines])
    print(f"""
    The following stanza has {len(lines)} lines. 
    Please provide a rhyme scheme code of length {len(lines)}
    -----------------------------------------------------------------------------""")
    for line in lines:
        print(f"\t{line}")
    code = input("""
    -----------------------------------------------------------------------------
    """)
    while len(code) != len(lines):
        if code.lower() in ["q", "quit"]:
            return None
        print(f"""
    You provided a rhyme scheme code of length {len(code)}.
    Please provide a rhyme scheme code of length {len(lines)},
    or type "q" or "quit" to exit the program.
    -----------------------------------------------------------------------------""")
        for line in lines:
            print(f"\t{line}")

        code = input("""
    -----------------------------------------------------------------------------
        """)

    inp = None
    while inp not in ["y", "n"]:
        print(f"""
    Please confirm that the annotation is correct.
    This is your annotation:
    -----------------------------------------------------------------------------""")
        for line, c in zip(lines, code):
            print(f"\t{line:<60} {c:>5}")
        
        inp = input("""
    -----------------------------------------------------------------------------
    Does this rhyme scheme look okay? [y/n]
    """).lower()
        if inp == "y":
            print("    Thank you! Saving to file.\n    -----------------------------------------------------------------------------")
            return code+"\n"+stanza
        if inp == "n":
            print("Okay! Try again")
            return annotate_stanza(stanza)

def check_dirs(args):
    """Check that the source directory containing stanzas exists, and that the 
        directory where produced annotations will be placed exists, or ask user 
        to create it.
    
    Args:
        args (argparse.Namespace): dict containing path to directories to read/write from/to

    """

    print("""
    ----------------------------------------------------------------------------------------------
    First we check that the provided directories exist... 
    """)

    source_dir = Path(args.source_dir)
    if source_dir.exists() and source_dir.is_dir():
        print(f"\tSource directory <{source_dir}> exists.")
    else:
        print(f"\tSource directory <{source_dir}> does not exist. Exiting program.")
        exit()

    out_dir = Path(args.dir)
    if out_dir.exists() and out_dir.is_dir():
        print(f"\tOutput directory <{out_dir}> exists")
    else:
        print(f"\tOutput directory <{out_dir}> does not exist")
        inp = None
        while inp not in ["y", "n"]:
            inp = input(f"\tDo you wish to create a new directory <{out_dir}>? [y/n]\n").lower()
            if inp == "y":
                print(f"\tCreating directory {out_dir.name}...")
                out_dir.mkdir(parents=True)
                if out_dir.exists():
                    print(f"\tDirectory <{out_dir}> created.")
            if inp == "n":
                print("\tOk. Exiting program.")
                exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Annotation tool for rhyme scheme annotation")
    parser.add_argument("dir", type=str,
                        help="path to directory where produced annotations are saved")
    parser.add_argument("-s", "--source_dir", type=str, default="../poems/bokmål/",
                        help="path to directory where poems to annotate are stored")

    args = parser.parse_args()

    print("""
    =============================================================================================
                * WELCOME to the Program for Annotation of Rhyme Scheme Etc (PARSE) *
    =============================================================================================

            Here you can annotate the rhyme schemes of stanzas a little bit 
                  faster than typing textfiles manually - hurray!
    """)

    check_dirs(args)
    annotate(args)

    print("""
    =============================================================================================

        (\                                                  
        \'\                                                 
        \'\     __________      
        / '|   ()_________)                                     
        \ '/    \ ~~~~~~~~ \                                    
         \       \ ~~~~~~   \                                    
        ==).      \__________\      Thank you for annotating!   
        (__)       ()__________)                                

    =============================================================================================
    """)