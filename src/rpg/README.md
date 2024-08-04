# RPG

## Calibre considerations

When converting to EPUB, it uses a pattern for structure detection. This rpg book uses a custom pattern

```
# structure detection
//section[contains(@class, 'chapter')]

# Level 1 TOC
//h1[contains(@class, 'chapter')]

# Level 2 TOC
//h2[contains(@class, 'subchapter')]
```


```bash
# Create local environment directory
python -m venv env

# Activate the virtual environment
source env/bin/activate

# Install required packages
pip install -r requirements.txt

# start the application
python build.py
```
