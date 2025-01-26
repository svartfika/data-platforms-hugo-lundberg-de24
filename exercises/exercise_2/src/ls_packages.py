import importlib.metadata as md
import sys

print("Platform: ", sys.platform)
print("Python version: ", sys.version)

print("Installed Python distributions:")
for dist in sorted(md.distributions(), key=lambda x: x.name):
    print(dist.name, dist.version)
