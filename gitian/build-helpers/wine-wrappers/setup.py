from distutils.core import setup
import py2exe
setup(
    console=["gcc.py", "dllwrap.py", "swig.py"],
    zipfile=None,
    options={"py2exe": {"bundle_files": 1, "compressed": True}}
)
