import os

variables = ["ENV_VAR1", "ENV_VAR2"]
for var in variables:
    print(f"{var}: {os.getenv(var, 'Not Found')}")
