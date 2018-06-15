try:
    from setuptools import setup
except ImportError:
    # Fallback to the standard library distutils.
    from distutils.core import setup

exec(open('afsutil/__version__.py').read())

setup(
    name='afsutil',
    version=VERSION,
    description='Utilities to setup OpenAFS clients and servers',
    long_description=open('README.rst').read(),
    author='Michael Meffie',
    author_email='mmeffie@sinenomine.net',
    url='https://github.com/openafs-contrib/afsutil',
    license='BSD',
    packages=[
        'afsutil',
        'afsutil.system',
    ],
    entry_points={
        'console_scripts': [
            'afsutil = afsutil.__main__:main'
        ]
    },
    include_package_data=True,
    test_suite='test',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: SunOS/Solaris',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
)
