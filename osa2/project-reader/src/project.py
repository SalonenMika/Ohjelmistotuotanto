class Project:
    def __init__(self, name, description, license_info, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license_info = license_info
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies


    def __str__(self):
        authors_formatted = "\n- ".join(self.authors)
        dependencies_str = "\n".join(f"- {dep}" for dep in self.dependencies) or "-"
        dev_dependencies_str = "\n".join(f"- {dev_dep}" for dev_dep in self.dev_dependencies) or "-"

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license_info}"
            f"\nAuthors:\n- {authors_formatted}"
            f"\nDependencies: {dependencies_str}"
            f"\nDevelopment dependencies: {dev_dependencies_str}"
        )
