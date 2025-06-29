from pathlib import Path

# kembali ke root project
path_dir = {"base": Path(__file__).resolve().parents[2]}

path_dir.update({"src": path_dir["base"] / "src"})
path_dir.update({
    "static": path_dir["src"] / "static",
    "template": path_dir["src"] / "template",
})
