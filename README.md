# import_gist
import gist python script

# Requirements
urllib, tempfile

# How to install

```
pip install git+https://github.com/cosacog/import_gist
```

# How to use
```py
# sample
from import_gist import *
# '/raw/' is not mandatory to the url_gist to load script.
url_gist = 'https://gist.githubusercontent.com/cosacog/67ac95feef8a2a1cd373d43a86fe2c9c'
sample_module = import_gist(url_gist)
dir(sample_module) # list functions or classes
```
