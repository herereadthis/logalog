import json
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Output file
output_file = "dist.html"

# Initialize Jinja2 environment
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

def load_json(file_path):
    """General function to load a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

file_paths = [
    ('chapters', './json/chapters_metadata.json'),
    ('minor_magical_tools', './json/random_tables/minor_magical_tools.json'),
    ('minor_magical_food_and_drink', './json/random_tables/minor_magical_food_and_drink.json'),
    ('minor_magical_personal_items', './json/random_tables/minor_magical_personal_items.json'),
    ('minor_magical_entertainment', './json/random_tables/minor_magical_entertainment.json'),
    ('minor_magical_dubiously_legal', './json/random_tables/minor_magical_dubiously_legal.json'),
    ('swn_one_roll_npc', './json/random_tables/swn_one_roll_npc.json'),
    ('wwn_appearances_and_mannerisms', './json/random_tables/wwn_appearances_and_mannerisms.json'),
    ('wwn_burning_ambitions', './json/random_tables/wwn_burning_ambitions.json'),
    ('wwn_close_friendships', './json/random_tables/wwn_close_friendships.json'),
    ('oddities', './json/random_tables/oddities.json'),
    ('wrongs_and_injustices', './json/random_tables/wrongs_and_injustices.json'),
    ('tarot', './json/tarot.json')
]

def build():
    template = env.get_template('./main.html')

    data = {key: load_json(file_path) for key, file_path in file_paths}
    html_output = template.render(**data)

    # Write the rendered HTML to the output file
    with open(output_file, 'w') as file:
        file.write(html_output)

    print(f"All sections have been compiled into {output_file}.")

if __name__ == "__main__":
    build()
