import json

from pathlib import Path

def create_entity(label: str, regex: str, item_list_path: Path, tag: str):

    with open('../assets/custom_entities.json') as f:
        entity_dict = json.load(f)

    entity_list = entity_dict['entity_details']

    entity_list.append({
        "label": label,
        "regex": regex,
        "item_list_path": Path,
        "tag": tag
    })

    with open('../assets/custom_entities.json', 'wb') as json_file:
        json.dump({entity_list}, json_file)


if __name__ == "__main__":
    typer.run(create_entity)
