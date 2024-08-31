from setuptools import setup,find_packages


def Requirements(filename):
    with open(filename,"r") as f:
        req=f.readlines()
        req=[i.replace("\n","") for i in req]
        if "-e ." in req:
            req.remove("-e .")
    return req



setup(
    name="Food Delivery Time Prediction",
    author="Gajender",
    version="0.1",
    author_email="iamsanju0707@gmail.com",
    description="All about the Prediction of Delivering the Food on the Time",
    packages=find_packages(),
    install_requires=Requirements("requirements.txt")
)