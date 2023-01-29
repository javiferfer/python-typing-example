# Python typing example

Start using this repository installing the [mypy](https://pypi.org/project/mypy/). This library will check the type annotations in your Python code.

As defined in the project description:
> Mypy is essentially a Python linter on steroids, and it can catch many programming errors by analyzing your program, without actually having to run it. Mypy has a powerful type system with features such as type inference, gradual typing, generics and union types.

Then, run the following command in your terminal:

```
mypy src --config-file mypy.ini
```

**Note**: The config file for this project is `mypy.ini` but there are other config files that can be used ([ref](https://mypy.readthedocs.io/en/stable/config_file.html)).

The library mypy doesn't include third-party libraries, limited only to standard library ([ref](ttps://stackoverflow.com/questions/72457638/why-isnt-mypy-seeing-types-from-typeshed)). Hence, the following error will appear when running:

> basic_example.py:1: error: Skipping analyzing "pandas": module is installed, but missing library stubs or py.typed marker

> basic_example.py:2: error: Skipping analyzing "sklearn.preprocessing": module is installed, but missing library stubs or py.typed marker

To solve this issue, one option is to add the option `ignore_missing_imports = True` to the `mypy.ini` file ([ref](https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports)). For any of the import options mypy will assume that the type of the module is Any, which means that the access to any attribute of the module will automatically succeed.

## Typing for DS libraries

Instead of including the option `ignore_missing_imports = True` to the `mypy.ini` file, the best approach is to install the libraries neeeded by mypy to detect the dependencies. Nevertheless, one of the downsides of `mypy` is that it does not work with external libraries.

Nevertheless, there has been some progress recently on developing packages that allow mypy type checker to recognize some of the most commong DS libraries. In particular, here is the status as January 29th 2023:

- Data processing and modeling
    - Pandas (1.5.3): [pandas-stubs](https://pypi.org/project/pandas-stubs/) (1.5.2.230105)
    - Numpy (1.24.1): Automatically detected

- Data visualization
    - Matplotlib (3.6.3): [data-science-types](https://pypi.org/project/data-science-types/) (0.2.23)

As far as I know, pandas, numpy and matplotlib seem to be the only three main DS libraries that mypy type checker can recognize.

To use them, install:
```
pip install pandas-stubs
pip install data-science-types
```

Then, try them out running:
```
mypy src
```

If everything is well installed, then just the following message should be displayed:

> src/basic_example.py:2: error: Skipping analyzing "sklearn.preprocessing": module is installed, but missing library stubs or py.typed marker

Sklearn is one of those DS libraries for which there is not a mypy type checker. Hence, to avoid errors for unrecognized libraries, uncomment `ignore_missing_imports = True` to the `mypy.ini` file.

Lastly, run the following command. This time there should not be any error displayed.

```
mypy src --config-file mypy.ini
```


## References:

1. [Stub files for matplotlib, numpy, scipy, pandas, etc](https://stackoverflow.com/questions/60247157/how-can-i-get-stub-files-for-matplotlib-numpy-scipy-pandas-etc)

