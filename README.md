# statistics-for-dummies
UI based data exploration and hypothesis testing tool

## Contributors
- [Hriday Baghar](https://github.com/hbaghar)
- [Ernesto Cediel](https://github.com/emcediel)
- [Keegan Freeman](https://github.com/kafreeman22)
- [Andy Tsai](https://github.com/andyctsai)

## Motivation
Statistics is not an easy subject. Many people would like to be able to perform powerful statistics with their data but don't know how and have no knowledge of statistical software such as Python or R. We have developed an easy to use UI that enables these non-code users to do their statistical analysis with their data as well as data visualization for data exploration and analysis. 

## Dependencies
The dependencies can be installed from the requirements.txt file using

```
python -m pip install -r requirements.txt
```

## Usage

### Online 
_Online hosteed link coming soon!_

### Offline 
After cloning this repository run the following commands in terminal:
```
> cd statistics-for-dummies

> streamlit run src/app.py --global.dataFrameSerialization="legacy"
``` 

## Code structure
```
statistics-for-dummies
├─ .gitignore
├─ LICENSE
├─ README.md
├─ datasets
│  ├─ Iris.csv
│  ├─ Sales.csv
│  └─ biostats.csv
├─ requirements.txt
└─ src
   ├─ app.py
   └─ backend
      ├─ __init__.py
      ├─ data_manipulation.py
      ├─ data_viz.py
      ├─ hypothesis_test_handler.py
      └─ hypothesis_tests.py

```