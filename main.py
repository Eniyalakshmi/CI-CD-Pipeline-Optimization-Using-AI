import random

print("CI/CD Pipeline Started ")

data = ["Build Success", "Model Training", "Testing", "Deployment"]

result = random.choice(data)

print("Current Stage:", result)

print("Pipeline Finished Successfully ")
