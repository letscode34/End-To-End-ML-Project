import setuptools

with open("README.md",'r',encoding='utf-8') as f:
    long_description = f.read()


REPONAME='End-To-End-ML-Project'
AUTHOR_USER_NAME='letscode34'
SRC_REPO='mlproject'
AUTHOR_EMAIL='letscodemachinelearning@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version='1.0.0',
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="End to End ML Project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}",
    project_urls={
        "But Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}/Issue",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    
)
