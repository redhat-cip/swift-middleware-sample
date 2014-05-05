from setuptools import setup

setup(name='sample',
    packages=['sample', ],
    zip_safe=False,
    entry_points={
       'paste.app_factory': ['app=sample.app:app_factory'],
       'paste.filter_factory': ['middleware = sample.middleware:filter_factory'],
    },
)
