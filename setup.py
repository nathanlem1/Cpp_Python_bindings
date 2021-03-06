from pathlib import Path

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

recursion_module = Pybind11Extension(
    'pybind_11_recursion',
    [str(fname) for fname in Path('src').glob('*.cpp')],
    include_dirs=['include'],
    extra_compile_args=['-O3']
)

setup(
    name='pybind_11_recursion',
    version=0.1,
    author='Nathanael L. Baisa',
    author_email='nathanaellmss@gmail.com',
    description='Basic pybind11+setup.py example for recursive algorithms: fibonnaci and factorial of an integer number',
    ext_modules=[recursion_module],
    cmdclass={"build_ext": build_ext},
)
