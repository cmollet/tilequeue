from setuptools import setup, find_packages

version = '0.2.1.dev0'

setup(name='tilequeue',
      version=version,
      description="Queue operations to manage the processes surrounding tile "
                  "rendering.",
      long_description=open('README.md').read(),
      classifiers=[
          # strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Internet :: WWW/HTTP :: Site Management',
          'Topic :: Utilities',
      ],
      keywords='aws queue s3 sqs tile map',
      author='Robert Marianski, Mapzen',
      author_email='rob@mapzen.com',
      url='https://github.com/mapzen/tilequeue',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'boto',
          'hiredis',
          'Jinja2',
          'ModestMaps',
          'TileStache',
          'PyYAML',
          'redis',
          'psycopg2',
      ],
      test_suite='tests',
      tests_require=[
          'mock'
      ],
      entry_points=dict(
          console_scripts=[
              'tilequeue = tilequeue.command:tilequeue_main',
          ]
      )
      )
