# NoRSC: Norwegian Rhyme Scheme Corpus
This is a corpus of rhyme scheme annotated poetry extracted from the [Public Domain Texts from NBdigital](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-34/) (no: [Fritt tilgjengelege tekster frå NBdigital](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-34/)) corpus from Språkbanken.

Each poem is split into stanzas, and each stanza is annotated on rhyme scheme.

# Data set 
This data set consists of 5158 stanzas, or 26 198 lines annotated with rhyme scheme codes.

# File structure
The directory `poems` contain unannotated poetry files.   
The file `tsvs/tita_rhymes_poems.tsv` contains v1 of the complete rhyme annotated poetry set.  
The file `tsvs/norwegian_rhyme_scheme_corpus_v11.tsv` contains version 1.1 of the complete rhyme annotated poetry set (89 stanzas are re-annotated).

## Rhyme annotated word pairs and sentence pairs 
The file `tsvs/positive_pairs.tsv` contains 7238 positive rhyme pairs.  
The file `tsvs/negative_pairs.tsv` contains 22 447 negative rhyme pairs.   
The file `tsvs/rhyme_sentence_pairs.tsv` contains 35 409 sentence pairs annotated with rhyme (1=rhyme, 0=not rhyme).  
(These are from v.1)


# How to help annotate:
Read the [annotation tool README](annotation_tool/README.md)
