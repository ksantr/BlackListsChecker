from setuptools import setup

setup(name='BlackListsChecker',
      version='0.1',
      description='Check domains or id adresses in the black lists',
      url='https://github.com/ksantr/BlacklistsChecker.git',
      author='ksantr',
      license='MIT',
      packages=['blcheck'],
      install_requires=['gevent'],
      scripts=['bin/blcheck'],
      zip_safe=False,
      long_description="""\
          Python 2.x
          -------------------------------------

          This version requires python-dev tools. (apt-get install python-dev).
          """
      )
