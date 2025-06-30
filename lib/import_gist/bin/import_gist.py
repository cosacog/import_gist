#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    import os, sys, urllib.request, tempfile, importlib.util
    
    tmp_dir = tempfile.mkdtemp()
    fname_function = tempfile.mktemp(suffix='.py', dir=tmp_dir) # temporary file name of .py
    tmp_func_name = os.path.basename(fname_function).split('.')[0]
    
    # check url_gist: if url includes '#', it is one of the files in the gist.
    if '#' in url_gist_in:
        # if url_gist includes '#', it is one of the files in the gist.
        # remove '#file-' part from url_gist
        url_gist_main, fname_func = url_gist_in.split('#')
        fname_func_raw = fname_func.replace('file-', '').replace('-py', '.py')
        username, gist_id = url_gist_main.split('/')[-2:]
        url_gist_out = f"https://gist.githubusercontent.com/{username}/{gist_id}/raw/{fname_func_raw}"
    else:
        # append '/' at the end
        if url_gist_in[-1] != '/':
            url_gist_in = url_gist_in + '/'
        # append 'raw/' at the end
        if url_gist_in[-5:] != '/raw/':
            url_gist_out = url_gist_in + 'raw/'
        else:
            url_gist_out = url_gist_in
    
    # Download the file
    urllib.request.urlretrieve(url_gist_out, filename=fname_function)
    
    # Import the module using importlib
    spec = importlib.util.spec_from_file_location(tmp_func_name, fname_function)
    mod_func = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod_func)
    
    # Clean up
    try:
        os.remove(fname_function)
        os.rmdir(tmp_dir)
    except:
        pass
    
    return mod_func

if __name__ == '__main__':
    print("I'm sorry. There is no main script.")
    print("Please use this module as a function.")
    print("Usage: mod_name = import_gist(url_gist)")
