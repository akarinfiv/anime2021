!pip install apng
import os, IPython
from PIL import Image, ImageDraw, ImageFont
from apng import APNG
import IPython,io,requests,math

!wget https://1.bp.blogspot.com/-gyrNbKV7Gws/XWS5lvlXK5I/AAAAAAABUUY/jZMoffMzu5Ix1BG6AKDaBITEIfa1cZuKgCLcBGAs/s1600/kakedasu_school.png

class APolygon(AShape):
    color: any
    slope: float # 最初の傾き

    def __init__(self, width=100, height=None, cx=None, cy=None, N=3, slope=0.0, color=None):
        AShape.__init__(self, width, height, cx, cy)
        self.N = N
        self.slope = slope
        self.color = get_color('#cc528b')

    def render(self, canvas: ACanvas, tick: int):
        theta = math.pi * 2 / self.N
        # 半径
        r = min(self.width, self.height)/2
        # 頂点の数だけ頂点の座標を計算する
        points = []
        for i in range(self.N):
            x = self.cx + r * math.cos(theta*i + self.slope)
            y = self.cy + r * math.sin(theta*i + self.slope)
            points.append((x, y))
        canvas.draw.polygon(points, fill=self.color)

class RollingPolygon(APolygon):

    def render(self, canvas: ACanvas, tick: int):
        theta = math.pi * 4/ self.N
        slope = math.sin(math.pi * 4 * 5 * (tick/200))  # 自転させる
        # 半径
        r = min(self.width, self.height)/2
        # 頂点の数だけ頂点の座標を計算する
        points = []
        for i in range(self.N):
            x = self.cx + r * math.cos(theta*i + self.slope + slope)
            y = self.cy + r * math.sin(theta*i + self.slope + slope)
            points.append((x, y))
        canvas.draw.polygon(points, fill=self.color)

studio = AStudio()
shape = RollingPolygon(width=300, N=9)
studio.append(shape)
for i in range(60):
    studio.render()
IPython.display.Image(studio.create_anime())

class Studio(object):
    bodies: list
    frame: int



    def __init__(self, width=400, height=300, background='white'):
        self.width = width
        self.height = height
        self.background = background
        self.bodies = []
        self.files = []
        self.frame = 0
      
    def append(self, shape):
        self.bodies.append(shape) # 被写体を追加する
        return shape
    def render(self, caption=''):
        # 新しいキャンバスを作る
        canvas = ACanvas(self.width, self.height, self.background)
        # リスト上の形状を順番に描画する
        for body in self.bodies:
            body.render(canvas, self.frame)
        # PNG画像に保存する
        filename = f'frame{self.frame}.png'
        canvas.image.save(filename)
        self.files.append(filename)
        self.frame += 1

    def create_anime(self, filename='anime.png', delay=100):
        APNG.from_files(self.files, delay=int(delay)).save(filename)
        for image in self.files:
            os.remove(image) # 不要なファイルは消す
        self.files = []
        return filename

studio = AStudio()
shape = RollingPolygon(width=200, N=9)
studio.append(shape)
studio.append(AImage(image='kakedasu_school.png',width=180))
for i in range(50):
    studio.render()
studio.append(shape)

IPython.display.Image(studio.create_anime())