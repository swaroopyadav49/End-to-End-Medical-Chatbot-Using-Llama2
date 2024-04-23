from setuptools import find_packages, setup

setup(
    name='Medical Chatbot',
    version='0.0.1',
    author='swaroop',
    author_email='swaroopyadav49@gmail.com',
    install_requires=["ctransformers==0.2.5","sentence-transformers==2.2.2","pinecone-client","langchain==0.0.225",
                         "flask","pypdf","python-dotenv"],
    packages=find_packages()

)