import importlib
import time

packages = ['keras', 'sklearn', 'scipy', 'matplotlib.pyplot', 'pandas', 'pandas_datareader', 'tqdm', 'h5py', 'PIL', 'pymongo', 'yaml', 'psutil', 'pyarrow', 'seaborn', 'openpyxl', 'pyspark', 'h2o', 'tensorflow', 'IPython', 'jupyter', 'nltk', 'tables', 'deap', 'django_dag', 'bitstring', 'gym', 'JSAnimation', 'loader', 'sparkdl', 'pprint', 'mysql', 'tensorframes', 'kafka', 'tensorflowonspark', 'jieba']

inc = 0
print("\n")
print("Importing libraries.", end="")
time.sleep(.5)
print(".", end="")
time.sleep(.5)
print(".")
try:
    for lib in packages:
        globals()[lib] = importlib.import_module(lib)
        inc+=1
        if inc == len(packages)//4:
            print("25% Complete")
        elif inc == len(packages)//2:
            print("50% Complete")
        elif inc == len(packages)//4 * 3:
            print("75% Complete")
        time.sleep(.5)
    time.sleep(.5)
	
except ModuleNotFoundError as obj:
    print(obj, "installed. Please install this package before handing in your lab!")

else:
    print("100% Complete!, Your environment seems to be working well!")
    time.sleep(.5)
    print(str(inc)+" packages were imported\n")
