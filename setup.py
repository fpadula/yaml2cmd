import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='yaml2cmd',
    version='0.0.1',
    description='Parses yaml files to generate (usually long) shell commands',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    url='https://github.com/fpadula/yaml2cmd',
    license='MIT License',
    author='Felipe Padula Sanches',
    author_email='fpadula92@gmail.com',
    install_requires=['pyyaml'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
)
