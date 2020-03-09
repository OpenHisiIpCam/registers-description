#!/usr/bin/env python3

import sys
import os

import markdown

# Ignore this. Only needed for this example
this_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(this_dir, "./"))

from systemrdl import RDLCompiler, RDLCompileError
from ralbot.html import HTMLExporter

#===============================================================================
#input_file = sys.argv[1]
#output_dir = sys.argv[1]

output_dir = "./output"

#print(output_dir)




top = ['hi3516av200', 'hi3519v101']
#top = ['hi3519v101'] # top level address maps

roots = []
rdlc = RDLCompiler()
rdlc.compile_file('hi3516av200.rdl')
#rdlc.compile_file('hi3516cv300_family.rdl')

for addrspace in top:
    root = rdlc.elaborate(addrspace)
    roots.append(root.top)
htmlexporter = HTMLExporter()
htmlexporter.export(roots, output_dir)

#rdlc = RDLCompiler()

#try:
    #for input_file in input_files:
#    rdlc.compile_file(input_file)
#    root = rdlc.elaborate()
#except RDLCompileError:
#    sys.exit(1)

#md = markdown.Markdown(
#    extensions=['admonition']
#)

#html = HTMLExporter(markdown_inst=md)
#html = HTMLExporter()
#html.export(
#    root,
#    os.path.join(this_dir, output_dir),
#    home_url="/"
#)
