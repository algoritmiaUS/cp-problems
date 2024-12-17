from pathlib import Path
from collections import Counter

# Definición de extensiones y lenguajes
languages = {
    ".c": "C",
    ".cpp": "C++",
    ".cs": "C#",
    ".py": "Python",
    ".hs": "Haskell",
}

# Estructura de datos inicial
data = {key: [] for key in ["Juez Online", "Problemas Resueltos", *languages.values()]}

if __name__ == "__main__":
    path = Path(".")

    for directory in path.iterdir():
        if directory.is_dir() and not directory.name.startswith("."):
            data["Juez Online"].append(directory.name)

            files = [file.suffix for file in directory.iterdir() if file.is_file()]
            data["Problemas Resueltos"].append(len(files))

            counter = Counter(files)

            for ext, lang in languages.items():
                data[lang].append(counter.get(ext, 0))


    columns = list(data.keys()) 
    rows = zip(*data.values()) 

    markdown_table = "| " + " | ".join(columns) + " |\n"
    markdown_table += "| " + " | ".join(["---"] * len(columns)) + " |\n"

    for row in rows:
        markdown_table += "| " + " | ".join(map(str, row)) + " |\n"

    readme_path = "README.md"

    # Identificadores de sección en README
    start_marker = "<!-- START_STATS -->"
    end_marker = "<!-- END_STATS -->"

    with open(readme_path, "r") as f:
        readme_content = f.read()

    # Reemplazar sección de la tabla
    updated_content = readme_content.split(start_marker)[0] + start_marker + "\n"
    updated_content += markdown_table + "\n" + end_marker + readme_content.split(end_marker)[1]

    with open(readme_path, "w") as f:
        f.write(updated_content)

    print("README.md actualizado correctamente.")
