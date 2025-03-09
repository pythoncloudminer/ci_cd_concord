from setuptools import setup, find_packages

# Define the setup configuration
setup(
    name="your_package_name",  # Replace with the name of your package
    version="0.1.0",  # Version of your package
    author="Your Name",  # Your name
    author_email="your.email@example.com",  # Your email address
    description="A short description of your package",
    long_description=open("README.md").read(),  # Optional: Detailed description from README
    long_description_content_type="text/markdown",  # If you use Markdown for README
    url="https://github.com/yourusername/your-repository",  # URL to your project repository
    packages=find_packages(),  # Automatically find packages in your source code
    install_requires=[
        # List your package dependencies here
        "numpy>=1.18.0",
        "pandas>=1.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
)
