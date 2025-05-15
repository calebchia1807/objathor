<h2 align="center">
  ObjaTHOR<br>
</h2>

<h4 align="center">
    Improved Objaverse asset annotator and importer for use in THOR.
</h4>

## Requirements
- Blender 3.4 **(Ensure this is downloaded)**
- Conda Environment

## Installation
Create conda environment
```bash
conda create --name objathor python=3.10
```

Install ai2thor:
```bash
pip install --extra-index-url https://ai2thor-pypi.allenai.org ai2thor==0+455cf72a1c8e0759a452422f2128fbc93a3cb06b
```

Install other dependencies:
```bash
pip install objathor[annotation]
pip3 install ai2thor attrs torch objaverse scipy openai prior mathutils
```

Here the following extras are installed: `annotation` to use openai to generate annotations. Also for annotation functionality you must install `nltk` [Install nltk](#nltk-dependencies). To generate renders and convert 'glb' models in the conversion pipeline **you must install Blender v3.4**.

From source:
```bash
pip install -e ".[annotation]"
```

We recommend setting an environment variable with your OpenAI key:
```bash
export OPENAI_API_KEY=[Your key]
```

### NLTK dependencies
Install `nltk` on this commit by running:
```bash
pip install git+https://github.com/nltk/nltk@582e6e35f0e6c984b44ec49dcb8846d9c011d0a8
```

During the first run, NLTK dependencies are automatically installed, but we can also install them ahead:
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet2022'); nltk.download('brown'); nltk.download('averaged_perceptron_tagger')"
```

### AI2-THOR binary pre-downloading
Assuming we're running on a remote Linux server, we can pre-download the THOR binaries with:
```bash
python -c "from ai2thor.controller import Controller; from objathor.constants import THOR_COMMIT_ID; c=Controller(download_only=True, platform='CloudRendering', commit_id=THOR_COMMIT_ID)"
```
(`platform='OSXIntel64'` would be used for a MacOS environment).

## Usage
### Convert all assets in one go
1. Add all .glb files into ```~/objathor/objathor/assets/``` folder.
2. Run the following command to convert all the assets in the folder into THOR asset(s):
   ```bash
   python3 convert_assets.py
   ```
   #### Please open this [python script](/objathor/assets/convert_assets.py) and update all file paths where necessary before running.

### Convert one asset only
Run:
```bash
python main.py --uid <file_name> --glb <path_to_glb> --output <path_to_output> --blender_installation_path <blender_installation_path>
```
#### **uid's <file_name> must be the same as the .glb name in glb's <path_to_glb>
