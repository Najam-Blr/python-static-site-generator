import typer

import ssg.parsers
from ssg.site import Site
from ssg.parsers import Parser, ResourceParser


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest, "parsers": [ssg.parsers.ResourceParser()]}
    Site(**config).build()


typer.run(main)
