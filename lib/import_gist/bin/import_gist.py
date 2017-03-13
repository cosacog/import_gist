# coding: utf-8
def import_gist(url_gist):
    # import custom functions from gist.github.com
    # usage: mod_name = import_gist(url_gist)
    # params:
    #   url_gist: url of gist. be sure to append '/raw/' to the gist url to load script, not html
    #       e.g. https://gist.githubusercontent.com/cosacog/67ac95feef8a2a1cd373d43a86fe2c9c/raw/
    import os,sys, urllib, tempfile
    fname_func = 'tmp_func.py' # temporary file name of .py
    tmp_dir = tempfile.mkdtemp()
    urllib.urlretrieve(url_gist, filename=os.path.join(tmp_dir,fname_func))
    sys.path.append(tmp_dir)
    import tmp_func as mod_func
    sys.path.remove(tmp_dir)
    return mod_func

if __name__ =='__main__':
    print("I'm sorry. There is no main script.")
