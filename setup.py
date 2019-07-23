from setuptools import setup


setup(
    name="marketing-blocks",
    version="0.1.3",
    description="Handle marketing blocks from back office",
    url="https://github.com/briefmnews/marketing-blocks",
    author="Brief.me",
    author_email="tech@brief.me",
    license=None,
    packages=["marketing_blocks", "marketing_blocks.migrations"],
    python_requires=">=2.7",
    install_requires=["Django>=1.11.21", "django-model-utils>=3.1.2"],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=False,
)
