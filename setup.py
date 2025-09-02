from setuptools import setup, find_packages

setup(
    name="expense-tracker",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "expense-tracker=expense_tracker.cli:main"
        ]
    },
    author="Laju Okoro",
    description="A fancy CLI-based personal expense tracker in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
)
