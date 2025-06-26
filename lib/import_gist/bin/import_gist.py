#!/usr/bin/env python
# -*- coding: utf-8 -*-
def import_gist(url_gist_in):
    '''
    import custom functions from gist.github.com
    usage: mod_name = import_gist(url_gist)
    params:
      url_gist: url of gist. be sure to append '/raw/' to the gist url to load script, not html
          e.g. https://gist.githubusercontent.com/cosacog/67ac95feef8a2a1cd373d43a86fe2c9c/raw/
    '''
    import os,sys, urllib, tempfile
    import urllib.request
    fname_function = 'tmp_func.py' # temporary file name of .py
    tmp_dir = tempfile.mkdtemp()
    # check url_gist: if url includes '#', it is one of the files in the gist.
    if '#' in url_gist_in:
        # if url_gist includes '#', it is one of the files in the gist.
        # remove '#file-' part from url_gist
        url_gist_main, fname_func = url_gist_in.split('#')
        fname_func_raw = fname_func.replace('file-', '').replace('-py', '.py')
        username, gist_id = url_gist_main.split('/')[-2:]
        url_gist_out = f"https://gist.githubusercontent.com/{username}/{gist_id}/raw/{fname_func_raw}"
    # append '/' at the end
    elif url_gist_in[-1] != '/':
        url_gist_in = url_gist_in + '/'
        # append 'raw/' at the end
        if url_gist_in[-5:] != '/raw/':
            url_gist_out = url_gist_in + 'raw/'
    urllib.request.urlretrieve(url_gist_out, filename=os.path.join(tmp_dir,fname_function))
    sys.path.append(tmp_dir)
    import tmp_func as mod_func
    sys.path.remove(tmp_dir)
    return mod_func

if __name__ =='__main__':
    print("I'm sorry. There is no main script.")
    print("Please use this module as a function.")
    print("Usage: mod_name = import_gist(url_gist)")