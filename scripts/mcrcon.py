from mcrcon import MCRcon
import os

with MCRcon(os.environ.get('RCON_HOST', "localhost"), os.environ.get('RCON_PASS', "minecraft")) as mcr:
  resp = mcr.command(input())
  print(resp)