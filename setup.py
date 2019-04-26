from setuptools import setup

setup(name='marketing-blocks',
      version='0.1',
      description='Handle marketing blocks from back office',
      url='https://github.com/briefmnews/marketing-blocks',
      author='Brief.me',
      author_email='tech@brief.me',
      license=None,
      packages=['marketing_blocks'],
      python_requires="==2.7.*",
      install_requires=[
        'Django>=1.11',
      ],
      zip_safe=False)
