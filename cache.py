import json


def openCache(file):
    try:
        cache_file = open(file, 'r')
        cache_contents = cache_file.read()
        cache_dict = json.loads(cache_contents)
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict


def saveCache(file,cache_dict):
    dumped_json_cache = json.dumps(cache_dict)
    fw = open(file,"w")
    fw.write(dumped_json_cache)
    fw.close() 