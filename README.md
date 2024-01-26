# UT_code

#### Generates some brains with various "activity" using `nilearn.plotting()` functionality.

| Filename          | Description                                                                                                                |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `main.py`         | Code used to interactively generate custom plots. Cannot be directly replicated as `IMAGES_DIR` is a hidden variable.      |
| `utbrainplots.py` | Generate the plots in the command line and save to a specified directory. Use this if you wish to make the plots yourself. |

#### For command line execution, see below.

First, create a directory.

```bash
mkdir utbrainplots
cd utbrainplots
```

To access the code, you can clone this entire repo

```bash
git clone https://github.com/w-decker/UT_code.git
```

or you can download the necessary files using the command below.

```bash
# if running on mac os: brew install wget
wget https://github.com/w-decker/UT_code/blob/main/utbrainplots.py
wget https://github.com/w-decker/UT_code/blob/main/utils.py

```

To generate the images, use the command line below.

```bash
python3.12 utbrainplots.py -d /path/to/images/dir
```
