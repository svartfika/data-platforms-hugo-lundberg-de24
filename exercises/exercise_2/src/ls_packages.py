import importlib.metadata as md
import sys

print("Platform: ", sys.platform)
print("Python version: ", sys.version)

installed_dists = [dist for dist in md.distributions()]
print("Installed Python distributions:")
for dist in sorted(installed_dists, key=lambda x: x.name):
    print(dist.name, dist.version)
