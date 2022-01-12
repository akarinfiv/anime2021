import IPython

from anime2021.anime import ACanvas, AShape, AStudio, ARectangle, ACircle, RollingPolygon, AImage, test_shape, TrailCircle

import os, IPython, io, requests
from PIL import Image, ImageDraw, ImageFont
from apng import APNG

kotori1 = 'https://3.bp.blogspot.com/-cegQSdM0epc/VxC3XAuatMI/AAAAAAAA54k/h7BYrFMw-dwk0fbJkUAmb9ggX5XTS8KLgCLcB/s800/bird_male.png'
kotori2 = 'http://2.bp.blogspot.com/-qcZeAPes1RQ/VxC3WyeEgHI/AAAAAAAA54g/IVV7OmDcq2Iuaugs_xiEUlGuGgIzP_-sQCLcB/s800/bird_female.png'

sora = 'http://www.sozailab.jp/db_img/sozai/25034/ed2adee6b5b0451155c2a230ef0f66ef.png'

import math

class TORI(AShape):
    color: any

    def __init__(self, width=100, height=None, cx=None, cy=None, image1=kotori1):
        AShape.__init__(self, width, height, cx, cy)
        if image1.startswith('http'):
            self.pic = Image.open(io.BytesIO(requests.get(image1).content))
        else:
            self.pic = Image.open(image1)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox), int(oy)), pic)
        
    def __init__(self, width=100, height=None, cx=None, cy=None, image=kotori2):
        AShape.__init__(self, width, height, cx, cy)
        if image.startswith('http'):
            self.pic = Image.open(io.BytesIO(requests.get(image).content))
        else:
            self.pic = Image.open(image)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox), int(oy)), pic)
       
    def SORAA(shape1, A=100, B=100, a=1, b=1, delta=0):
        # スタジオを用意
        studio = AStudio(500,500)

        # スタジオに背景を追加する
        studio.append(TORI(width=500, height=500, image=sora))   

        # スタジオにUFOを追加する
        studio.append(shape)
        frames = 80
        for t in range(frames):      
            x = 340 + A*math.sin(a*(3*math.pi*t/frames))
            y = 200 + B*math.sin(a*(4*math.pi*t/frames))
            # 被写体の中心を移動させる
            shape.cx = x
            shape.cy = y
            studio.render()
        for t in range(frames):      
            x = 197 + A*math.cos(a*(3*math.pi*t/frames))
            y = 250 + B*math.sin(a*(4*math.pi*t/frames))
            # 被写体の中心を移動させる
            shape.cx = x
            shape.cy = y
            studio.render()

        studio.append(shape1)
        frames = 30
        for t in range(frames):      
            x = 47  + A*math.sin(a*(0.5*math.pi*t/frames))
            y = 35  + A*0.5*t/frames
            # 被写体の中心を移動させる
            shape1.cx = x
            shape1.cy = y
            # 全ての移動が終わったら、撮影
            studio.render()

        frames = 50
        for t in range(frames):      
            x = 59 + A*math.cos(a*(0.5*math.pi*t/frames))
            y = 75 + A*t/frames
            # 被写体の中心を移動させる
            shape1.cx = x
            shape1.cy = y
            # 全ての移動が終わったら、撮影
            studio.render()

        studio.append(shape)
        frames = 80
        for t in range(frames):      
            x = 70 + A*math.cos(a*(3*math.pi*t/frames))
            y = 360 + B*2*t
            # 被写体の中心を移動させる
            shape.cx = x
            shape.cy = y
            studio.render()

        studio.append(shape1)
        frames = 50
        for t in range(frames):      
            x = 160  + A*math.sin(a*(8*math.pi*t/frames))
            y = 140
            # 被写体の中心を移動させる
            shape1.cx = x
            shape1.cy = y
            # 全ての移動が終わったら、撮影
            studio.render()
        

        return studio.create_anime(delay=50)

shape1 = TORI()
IPython.display.Image(shape1.SORAA())