import typer
from pathlib import Path

import spacy
import pickle
from spacy.matcher import PhraseMatcher
from spacy.matcher import Matcher
from spacy.pipeline import EntityRuler
from spacy.tokens import Span

import json
import jsonlines


def create_config(model_name: str, component_to_replace: str, output_path: Path, patterns_path: Path):
    # nlp = spacy.load(model_name)
    nlp = spacy.blank('fr')

    # load premade patterns for generic french entities
    patterns = pickle.load(open(patterns_path, "rb"))

    with open('corpus/patterns.jsonl', 'w') as outfile:
        for entry in patterns:
            print(entry)
            json.dump(entry, outfile)
            outfile.write('\n')
    # ruler.to_disk("/path/to/patterns.jsonl")

    # revert most training settings to the current defaults

    config = {
        "phrase_matcher_attr": None,
        "validate": True,
        "overwrite_ents": False,
        "ent_id_sep": "||",
    }

    entity_ruler = nlp.add_pipe("entity_ruler")
    entity_ruler.initialize(lambda: [], nlp=nlp, patterns=patterns)

    # save the config
    nlp.config.to_disk(output_path)


if __name__ == "__main__":
    typer.run(create_config)
