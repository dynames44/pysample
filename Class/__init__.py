# 클래스 패키지 처리 : 포함시킬 클래스는 전부 기술한다.
from .sampleClass1 import sampleClass1
from .sampleClass2 import sampleClass2

'''
전부 다 매번 기술하지 않는 방법도 있으나....

import os
import importlib

__all__ = []

folder = os.path.dirname(__file__)
for filename in os.listdir(folder):
    if filename.endswith(".py") and filename not in ["__init__.py"]:
        modulename = filename[:-3]
        module = importlib.import_module(f".{modulename}", package=__name__)
        globals()[modulename] = getattr(module, modulename)
        __all__.append(modulename)

'''