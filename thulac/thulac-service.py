from ctypes import *
import os
import hug

_lib = None

def init(model_path='', user_dict_path='', pre_alloc_size=1024*1024*16, t2s=False, just_seg=False):
    global _lib
    if _lib == None:
        path = '/usr/local/lib/python3.6/site-packages/thulac' #设置so文件的位置
        _lib = cdll.LoadLibrary(path+'/libthulac.so') #读取so文件
        if len(model_path) == 0:
          model_path = path+'/models' #获取models文件夹位置
        return _lib.init(c_char_p(model_path.encode('utf-8')), c_char_p(user_dict_path.encode('utf-8')), pre_alloc_size, int(t2s), int(just_seg)) #调用接口进行初始化
     
def clear():
    if _lib != None: _lib.deinit()

def seg(data):
    assert _lib != None
    r = _lib.seg(c_char_p(data))
    assert r > 0
    p = _lib.getResult()
    s = cast(p,c_char_p)
    d = '%s'%s.value.decode('utf-8')
    _lib.freeResult()
    return d.split(' ')

init()
#clear()
    
@hug.get('/thulac')
@hug.post('/thulac')
def cut(text):
    if type(locals()['text']) == list:
        result = []
        [result.extend(seg(i.encode('utf-8'))) for i in locals()['text']]
        return result
    else:
        return seg(locals()['text'].encode('utf-8'))
