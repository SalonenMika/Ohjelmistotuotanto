import toml # type: ignore
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)

        name = data.get("tool", {}).get("poetry", {}).get("name", "N/A")
        description = data.get("tool", {}).get("poetry", {}).get("description", "N/A")
        license_info = data.get("tool", {}).get("poetry", {}).get("license", "N/A")
        authors = data.get("tool", {}).get("poetry", {}).get("authors", [])

        dependencies = list(data.get("tool", {}).get("poetry", {}).get("dependencies", {}).keys())
        dev_dependencies = list(data.get("tool", {}).get("poetry", {}).get("dev-dependencies", {}).keys())

        return Project(name, description, license_info, authors, dependencies, dev_dependencies)
