#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("hidden_4", "C:\Users\Yvonne\Downloads\hidden_4.pyc")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

names = [name for name in dir(module) if not name.startswith("__")]
names.sort()
for name in names:
    print(name)
