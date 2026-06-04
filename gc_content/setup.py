from setuptools import setup
setup(name = 'gc_content',
     version = '0.1.0',
     packages = ['gc_content'],
     entry_points = {'console_scripts' : ['gc_content=gc_content.__main__:main']})
