from setuptools import setup
from setuptools.command.build import build


# Override build command
class BuildCommand(build):
    def initialize_options(self):
        build.initialize_options(self)
        self.build_base = "/tmp"


setup(
    name="django_articles",
    version="0.1",
    packages=["articles"],
    install_requires=[],
    python_requires='>=3.9',
    cmdclass={"build": BuildCommand},
)
