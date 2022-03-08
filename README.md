# README
This is a corpus of rhyme scheme annotated poetry extracted from the [Public Domain Texts from NBdigital](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-34/) (no: [Fritt tilgjengelege tekster frå NBdigital](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-34/)) corpus from Språkbanken.
Each poem is split into stanzas, and each stanza is annotated on rhyme scheme.

# How to help annotate:
Read the [annotation tool README](annotation_tool/README.md)

# Data set 
The directory `poems` contain unannotated poetry files.  
The file `tsvs/tita_rhymes_poems.tsv` contains the complete rhyme annotated poetry set. 

## Word and sentence pairs based on the annotated data set
The files `tsvs/rhyme_pairs.tsv` and `tsvs/negative_rhyme_pairs.tsv` contain word pairs that rhyme or don't rhyme, respectfully.  
The file `tsvs/sentence_pairs.tsv` contains sentence pairs annotated with rhyme (1=rhyme, 0=not rhyme).

