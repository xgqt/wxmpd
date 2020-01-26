#!/usr/bin/env python3


from setuptools import setup


def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='Wxmpd',
    version='1.0',
    description='Wxpython MPD contoller',
    author='XGQT',
    author_email='xgqt@protonmail.com',
    url='https://gitlab.com/xgqt/wxmpd',
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='ISC',
    keywords="mpd gui tray",
    python_requires=">=3.5.*",
    packages=['wxmpd'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'wxmpd = wxmpd.cmdline:execute',
        ],
    },
    classifiers=[
        'Development Status :: Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Bug Tracking',
    ]
)
