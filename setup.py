from setuptools import setup

setup(name='BlacklistsChecker',
      version='0.1',
      description='Check domains or id adresses in the black lists',
      url='https://github.com/ksantr/BlacklistsChecker.git',
      author='ksantr',
      license='MIT',
      packages=['black_lists_check'],
      install_requires=['gevent'],
      scripts=['bin/blacklistscheck'],
      zip_safe=False,
      long_description="""\
          Python 2.x
          -------------------------------------

          This version requires python-dev tools. (apt-get install python-dev).
          """
      )
