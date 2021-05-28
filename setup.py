from setuptools import setup


setup(
    name="marketing-blocks",
    version="1.5.0",
    description="Handle marketing blocks from back office",
    url="https://github.com/briefmnews/marketing-blocks",
    author="Brief.me",
    author_email="tech@brief.me",
    license=None,
    packages=["marketing_blocks", "marketing_blocks.migrations"],
    python_requires=">=3.7",
    install_requires=["Django>=2.2,<4", "django-model-utils>=4"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2",
        "Framework :: Django :: 3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
    zip_safe=False,
)
