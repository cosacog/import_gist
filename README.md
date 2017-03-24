# import_gist
import gist script

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
# be sure to append '/raw/' to the gist url to load script, not html.
url_gist = 'https://gist.githubusercontent.com/cosacog/67ac95feef8a2a1cd373d43a86fe2c9c'
# "/raw/" can be added to the url.
sample_module = import_gist(url_gist)
dir(sample_module) # list functions
```
