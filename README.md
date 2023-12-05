## Get Started - Setup Steps

### Prerequisites
- You need an OpenAI API key.
- If you want to run the open-source models, you will need to install them locally or run them on RunPod.
  - Here's a YouTube video showing you how: [https://youtu.be/Y5OV58lGTh8](https://youtu.be/Y5OV58lGTh8)

### Setup Scripts
- `configurations.json`: Add your API key to this file.
- `locations.json`: Update this file with the location of the `configurations.json` file.

## Important Information on Requirements.txt

Some important notes about the environment.txt files. Due to the update in the OpenAI API, the `Proprietary_vs_OpenSource Rap Battle.ipynb` and `speak.py` are running on different `requirements.txt` files. I couldn't get the open-source models to work with the latest OpenAI and AutoGen Libs.

So, for the `Proprietary_vs_OpenSource Rap Battle.ipynb`, you will need to run this with the `requirements.txt` file in the folder `Requirements for Notebook`. For `speak.py`, you need to run this with the `requirements.txt` file in the folder `Requirements for speak script`.

The best way to do this is to create two virtual environments, which you can do with Anaconda.

## Running the Project

### The Main Scripts
- The main script is the `Proprietary_vs_OpenSource Rap Battle.ipynb` notebook. This generates the battles. You should run this end-to-end first.
- The `speak.py` script generates the voices from the lyrics by calling the OpenAI API. Run this to render the voices.
