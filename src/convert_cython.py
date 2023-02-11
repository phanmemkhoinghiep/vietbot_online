from distutils.core import Extension, setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext
# define an extension that will be cythonized and compiled
import click
while True:
    input_file = click.prompt('')
    click.echo('<Input:> %s' % input_file)
    output_file=input_file.replace('.py','')
    ext = Extension(name=output_file, sources=[input_file])
    setup(ext_modules=cythonize(ext))