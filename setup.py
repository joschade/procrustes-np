from setuptools import setup

setup(
   name='procrustes_np',
   version='0.0',
   description='A lightweight and performant impelentation of orthogonal procrustes with numpy as backend',
   author='Johannes Schade',
   author_email='please@donotmailme.com',
   packages=['procrustes_np'],  #same as name
   install_requires=['numpy'], #external packages as dependencies
)
