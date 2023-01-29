# python-typing-example

Start using this repository installing the [mypy](https://pypi.org/project/mypy/). This library will check the type annotations in your Python code.

As defined in the project description:
> Mypy is essentially a Python linter on steroids, and it can catch many programming errors by analyzing your program, without actually having to run it. Mypy has a powerful type system with features such as type inference, gradual typing, generics and union types.


Then, run the following command in your terminal:

```
mypy basic_example.py --config-file mypy.ini
```

**Note**: The config file for this project is `mypy.ini` but there are other config files that can be used ([ref](https://mypy.readthedocs.io/en/stable/config_file.html)).

The library mypy doesn't include third-party libraries, limited only to standard library ([ref](ttps://stackoverflow.com/questions/72457638/why-isnt-mypy-seeing-types-from-typeshed)). Hence, the following error will appear when running:

> basic_example.py:1: error: Skipping analyzing "pandas": module is installed, but missing library stubs or py.typed marker
> basic_example.py:2: error: Skipping analyzing "sklearn.preprocessing": module is installed, but missing library stubs or py.typed marker

To solve this issue, one option is to add the option `ignore_missing_imports = True` to the `mypy.ini` file ([ref](https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports)). For any of the import options mypy will assume that the type of the module is Any, which means that the access to any attribute of the module will automatically succeed.
