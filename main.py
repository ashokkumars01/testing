import os

variables = ["ARTIFACTORY_INTERNAL_TOKEN", "ARTIFACTORY_TOKEN"]
for var in variables:
    print(f"{var}: {os.getenv(var, 'Not Found')}")
