import json
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Output file
output_file = "dist.html"

# Initialize Jinja2 environment
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

def load_chapter_metadata():
    with open('./json/chapters_metadata.json', 'r') as file:
        return json.load(file)

def load_oddities():
    with open('./json/random_tables/oddities.json', 'r') as file:
        return json.load(file)

def load_minor_magical_entertainment():
    with open('./json/random_tables/minor_magical_entertainment.json', 'r') as file:
        return json.load(file)

def load_minor_magical_dubiously_legal():
    with open('./json/random_tables/minor_magical_dubiously_legal.json', 'r') as file:
        return json.load(file)

def load_wrongs_and_injustices():
    with open('./json/random_tables/wrongs_and_injustices.json', 'r') as file:
        return json.load(file)

def build():
    chapters = load_chapter_metadata()
    magical_entertainment = load_minor_magical_entertainment()
    minor_magical_dubiously_legal = load_minor_magical_dubiously_legal()
    oddities = load_oddities()
    wrongs_and_injustices = load_wrongs_and_injustices()

    template = env.get_template('./main.html')

    # Render the main template with the necessary context
    html_output = template.render(
        chapters=chapters,
        magical_entertainment=magical_entertainment,
        minor_magical_dubiously_legal=minor_magical_dubiously_legal,
        oddities=oddities,
        wrongs_and_injustices=wrongs_and_injustices
    )

    # Write the rendered HTML to the output file
    with open(output_file, 'w') as file:
        file.write(html_output)

    print(f"All sections have been compiled into {output_file}.")

if __name__ == "__main__":
    build()
