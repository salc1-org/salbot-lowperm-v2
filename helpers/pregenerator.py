from pathlib import Path


folders = [
    "./data/",
    "./data/config/",
    "./data/config/perms"
]

files = {
    "./data/config/perms/role_perms.json": {
        "file": "./templates/role_perms.json",
        "force": True
    },
    "./data/config/perms/user_perms.json": {
        "data": "{}"
    }
}

for folder in folders:
    try:
        Path(folder).mkdir(parents=True)
    except Exception as e:
        print(f"Pregeneration error: {e}")


for key in files:
    fdata = str()
    force = False
    if "file" in files[key]:
        path = Path(files[key]["file"])
        
        if not path.exists():
            raise FileNotFoundError(f"Template file {path} not found.")

        with path.open() as f:
            fdata = f.read()

    elif "data" in files[key]:
        fdata = files[key]["data"]

    if "force" in files[key]:
        force = files[key]["force"]

    path = Path(key)

    if path.exists() and not force:
        print(f"Pregenerator skipping {key} as it already exists and is not force overriden.")
        continue

    with path.open('w') as f:
        f.write(fdata)