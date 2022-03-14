
# How to help annotate the inter annotator subset:
1. Read the [guidelines](annotation_guidelines.md)
2. Run the annotation script like this: `python3 annotate.py <your-name> -s ../poem_subset
3. Have fun annotating 100 stanzas :D Thank you!

# Notes on the annotation script:
The annotation script is a simple tool to help you annotate rhyme scheme. 
It will read poems from a folder, and present them to you, stanza by stanza (aka split it on double newlines and feed each bit one by one).
![sc_1](screenshot1.png)  
You will be asked to provide a rhyme scheme code for the given stanza, and once you have provided a rhyme scheme code of the correct length, you will see the poem annotated line for line with your rhyme scheme code.  

![sc_2](screenshot2.png)  
You will be asked to confirm that this is correct, and if so your annotation is saved and you will be presented with the next stanza.

Read the [annotation guidelines](annotation_guidelines.md) first, to make sure you annotate correctly. 

## Dependencies
The annotation script was created with Python 3.8.10, but should work for all versions >= 3.4 without installing any packages.

## Running the annotation script
Run the script like this:
```
python3 annotate-py <destination_dir> -s <source_dir>
```
Where `destination_dir` is the directory where your annotations are saved and `source_dir` is where the poems to annotate are stored. In this case, `poems_subset` is used to measure inter-annotator agreement, and `poems` is the _not yet_ full data set of poetry to be annotated.

# After annotation
After you are done annotating, run the after-annotation script like this:
```
python3 annotations_to_tsv <destination_dir>
```
where `<destination_dir>` is the same as above, the directory where your annotations are saved. 
This will create a .tsv-file containing the cleaned up versions of the rhyme schemes. 
All tsv-files are stored in the `tsvs/` folder

## Dependencies
The after-annotation script was run with the following packages:
```
Python 3.8.10
pandas  1.2.1
```
