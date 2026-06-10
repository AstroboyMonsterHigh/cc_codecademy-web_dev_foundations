#!/usr/bin/env python
from livereload import Server

# Create a server instance
server = Server()

# Watch the current directory and all its files
server.watch('.')

# Serve the files - root directory is current folder
# This opens a browser at http://localhost:5500
server.serve(root='.', port=5500)
