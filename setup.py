from setuptools import setup, find_packages

setup(name = "Miso",
      version = "0.1",
      description="A package for environmental monitoring",
      url='https://github.com/mviallet/Miso',
      author='Maxime Viallet',
      author_email='viallet.maxime@gmail.com',
      license='GPL3',
      keywords='sensors monitoring',
      packages=find_packages(),
#      install_requires=['sqlite3', 'plotly'],
      python_requires='>=3')
