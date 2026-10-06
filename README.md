# Load an STL in Genesis

One script: load a mesh, add a floor, open the viewer, and simulate until you close it.

## Setup (Windows PowerShell)

Install Python 3.12 if needed (Genesis requires Python 3.10–3.13).
Then run these commands in this folder:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install torch==2.10.0 --index-url https://download.pytorch.org/whl/cu128
.\.venv\Scripts\python.exe -m pip install genesis-world
```

## Run

Copy your STL into this folder, then replace `my_object.stl` with its filename:

```powershell
.\.venv\Scripts\python.exe main.py "my_object.stl"
```

For an STL exported in millimeters:

```powershell
.\.venv\Scripts\python.exe main.py "my_object.stl" --scale 0.001
```

The first run can take time to compile. The object starts at z=0.5 meters
and falls onto the floor. Close the Genesis window or press Ctrl+C to stop.
Genesis selects the NVIDIA GPU automatically when CUDA is available.
To hold the object in place, change `fixed=False` to `fixed=True` in `main.py`.

References: [installation](https://genesis-world.readthedocs.io/en/latest/user_guide/overview/installation.html),
[minimal scene tutorial](https://genesis-world.readthedocs.io/en/latest/user_guide/getting_started/hello_genesis.html).
