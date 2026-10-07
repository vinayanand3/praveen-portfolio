"""Builds the Nissan composite slide image. Run from the repo root: python3 tools/compose_nissan.py"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
SC=2; W,H=1600*SC,861*SC
BG=(11,13,16); TEAL=(51,214,193)
canvas=Image.new('RGB',(W,H),BG)
mono=lambda s: ImageFont.truetype('/System/Library/Fonts/SFNSMono.ttf',s*SC)

def cutout_white(im,th=238):
    a=np.array(im.convert('RGB')).astype(int)
    white=(a.min(axis=2)>th)
    # flood from border: keep only white connected to edges
    from collections import deque
    h,w=white.shape; bgm=np.zeros_like(white); q=deque()
    for x in range(w):
        for y in (0,h-1):
            if white[y,x] and not bgm[y,x]: bgm[y,x]=1; q.append((y,x))
    for y in range(h):
        for x in (0,w-1):
            if white[y,x] and not bgm[y,x]: bgm[y,x]=1; q.append((y,x))
    while q:
        y,x=q.popleft()
        for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny,nx=y+dy,x+dx
            if 0<=ny<h and 0<=nx<w and white[ny,nx] and not bgm[ny,nx]: bgm[ny,nx]=1; q.append((ny,nx))
    alpha=Image.fromarray(((1-bgm)*255).astype('uint8')).filter(ImageFilter.GaussianBlur(1))
    out=im.convert('RGBA'); out.putalpha(alpha); return out

cars=[('NISSAN PATHFINDER','source/images/nissan-pathfinder.jpeg',(31,60,484,300),'white'),
      ('INFINITI QX60','source/images/infiniti-qx60.jpeg',(195,176,1727,974),'black'),
      ('INFINITI QX65','source/images/infiniti-qx65.jpeg',(15,77,625,396),'black')]
rowH=H//3; colX=40*SC; maxW=560*SC; maxH=200*SC
boxes=[]
d=ImageDraw.Draw(canvas)
for k,(name,f,bb,kind) in enumerate(cars):
    im=Image.open(f).convert('RGB').crop(bb)
    s=min(maxW/im.width,maxH/im.height); im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
    y0=k*rowH+ (rowH-im.height)//2 + 14*SC; x0=colX+ (maxW-im.width)//2
    if kind=='white':
        c=cutout_white(im); canvas.paste(c,(x0,y0),c)
    else:
        region=canvas.crop((x0,y0,x0+im.width,y0+im.height))
        canvas.paste(ImageChops.lighter(region,im),(x0,y0))
    d.text((colX, k*rowH+22*SC), name, font=mono(15), fill=(150,158,168))
    w,h=im.size
    boxes.append((x0+int(.66*w), y0+int(.54*h), x0+int(.97*w), y0+int(.84*h)))

# overlay for highlights + lines
ov=Image.new('RGBA',(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
px0,py0,px1,py1=700*SC,120*SC,1560*SC,800*SC
anchor=(px0, (py0+py1)//2)
for (x0,y0,x1,y1) in boxes:
    od.rounded_rectangle((x0,y0,x1,y1),radius=10*SC,fill=TEAL+(46,),outline=TEAL+(255,),width=2*SC)
    sx,sy=x1,(y0+y1)//2
    mx=(sx+anchor[0])//2
    od.line([(sx,sy),(mx,sy),(mx,anchor[1]),(anchor[0],anchor[1])],fill=TEAL+(200,),width=2*SC,joint='curve')
    od.ellipse((sx-5*SC,sy-5*SC,sx+5*SC,sy+5*SC),fill=TEAL+(255,))
glow=ov.filter(ImageFilter.GaussianBlur(8*SC))
canvas=Image.alpha_composite(Image.alpha_composite(canvas.convert('RGBA'),glow),ov)

# zoom panel
panel=Image.new('RGBA',(px1-px0,py1-py0),(0,0,0,0))
pd=ImageDraw.Draw(panel); pd.rounded_rectangle((0,0,panel.width-1,panel.height-1),radius=22*SC,fill=(255,255,255,255))
biw=Image.open('source/images/rear-floor-biw.jpeg').convert('RGB').crop((10,25,460,425))
s=min((panel.width-60*SC)/biw.width,(panel.height-60*SC)/biw.height)
biw=biw.resize((int(biw.width*s),int(biw.height*s)),Image.LANCZOS)
panel.paste(biw,((panel.width-biw.width)//2,(panel.height-biw.height)//2))
mask=Image.new('L',panel.size,0); ImageDraw.Draw(mask).rounded_rectangle((0,0,panel.width-1,panel.height-1),radius=22*SC,fill=255)
pg=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(pg).rounded_rectangle((px0-4*SC,py0-4*SC,px1+4*SC,py1+4*SC),radius=26*SC,outline=TEAL+(255,),width=4*SC)
canvas=Image.alpha_composite(canvas,pg.filter(ImageFilter.GaussianBlur(10*SC)))
canvas.paste(panel,(px0,py0),mask)
cd=ImageDraw.Draw(canvas)
cd.rounded_rectangle((px0-2*SC,py0-2*SC,px1+2*SC,py1+2*SC),radius=24*SC,outline=TEAL+(255,),width=3*SC)
cd.ellipse((anchor[0]-8*SC,anchor[1]-8*SC,anchor[0]+8*SC,anchor[1]+8*SC),fill=TEAL)
cd.text((px0,py0-48*SC),"ZOOM · REAR FLOOR ASSEMBLY",font=mono(22),fill=TEAL)
cd.text((px0,py1+18*SC),"Rear floor assembly released for all three vehicles",font=mono(15),fill=(150,158,168))
out=canvas.convert('RGB').resize((1600,861),Image.LANCZOS)
out.save('assets/img/nissan_rear_floor_composite.jpg',quality=86,optimize=True,progressive=True)
