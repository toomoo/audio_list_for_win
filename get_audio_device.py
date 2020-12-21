# coding: UTF-8
import sounddevice as sd

def getdevices():
    devices = sd.query_devices()
    ret = []
    for i, d in enumerate(devices):
        for k, v in d.items():
            if k == 'name': inputname=v.encode().decode('utf_8').replace('\n','').replace('\r', '')
            if k == 'max_input_channels': numofinput=v
            if k == 'max_output_channels':numofoutput=v
        ret.append('[{}] (input, output)=({}, {})  {}'.format(str(i).zfill(2), numofinput, numofoutput, inputname))
    return ret


if __name__ == '__main__':

    items = getdevices()
    i_id, o_id = sd.default.device

    for i,item in enumerate(items):
        if i==i_id : print('> {}'.format(item))
        elif i==o_id : print('< {}'.format(item))
        else: print('  {}'.format(item))
