## ! Module not used ! ##

import os
import urllib2
import PIL
from PIL import Image

def goglib_get_icon(game_name, icon_url, path):

    icon_req = urllib2.Request(icon_url)
    icon_data = urllib2.urlopen(icon_req).read()
    icon_file = open(path + '/' + game_name + '.jpg', 'wb')
    icon_file.write(icon_data)
    icon_file.close()

    #pic_src = Image.open(path + '/' + game_name + '.jpg')
    #scale_lvl = 64/float(pic_src.size[0])
    #scaled_height = int(float(pic_src.size[1])*scale_lvl)
    #pic = pic_src.resize((64, scaled_height), PIL.Image.ANTIALIAS)
    #pic.save(path + '/' + game_name + '.jpg')

if __name__ == "__main__":
    import sys
    goglib_get_icon(sys.argv[1], sys.argv[2], sys.argv[3])
