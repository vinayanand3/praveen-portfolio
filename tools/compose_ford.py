"""Builds the Ford composite slide image. Run from the repo root: python3 tools/compose_ford.py"""
import numpy as np
from collections import deque
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
SC=2; W,H=1600*SC,861*SC
BG=(11,13,16); TEAL=(51,214,193)
mono=lambda s: ImageFont.truetype('/System/Library/Fonts/SFNSMono.ttf',s*SC)
canvas=Image.new('RGB',(W,H),BG)

# ---- Ford Edge (black bg -> lighten onto canvas) ----
edge=Image.open('source/images/ford-edge.jpeg').convert('RGB').crop((40,0,2100,1300))
ex0=30*SC; ew=640*SC; s=ew/edge.width
edge=edge.resize((ew,int(edge.height*s)),Image.LANCZOS)
ey0=(H-edge.height)//2+20*SC
reg=canvas.crop((ex0,ey0,ex0+edge.width,ey0+edge.height))
canvas.paste(ImageChops.lighter(reg,edge),(ex0,ey0))
E=lambda x,y:(ex0+(x-40)*s, ey0+y*s)
cd=ImageDraw.Draw(canvas)
cd.text((ex0+10*SC,ey0-10*SC),"FORD EDGE",font=mono(15),fill=(150,158,168))

# ---- panels ----
px0,px1=740*SC,1560*SC
P1=(px0,95*SC,px1,415*SC); P2=(px0,495*SC,px1,815*SC)

def flood_black_to(im,col,th=14):
    a=np.array(im).astype(int); dark=a.max(axis=2)<th; h,w=dark.shape
    bg=np.zeros_like(dark); q=deque()
    for x in range(w):
        for y in (0,h-1):
            if dark[y,x] and not bg[y,x]: bg[y,x]=1;q.append((y,x))
    for y in range(h):
        for x in (0,w-1):
            if dark[y,x] and not bg[y,x]: bg[y,x]=1;q.append((y,x))
    while q:
        y,x=q.popleft()
        for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny,nx=y+dy,x+dx
            if 0<=ny<h and 0<=nx<w and dark[ny,nx] and not bg[ny,nx]: bg[ny,nx]=1;q.append((ny,nx))
    m=Image.fromarray((bg*255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.2))
    return Image.composite(Image.new('RGB',im.size,col),im,m)

wh=Image.open('source/images/ford-edge-wheelhouse.jpeg').convert('RGB').crop((300,230,1500,880))
hi=flood_black_to(Image.open('source/images/ford-edge-trailer-hitch.jpeg').convert('RGB'),(244,245,247))
panels=[(P1,wh,(60,102,127),"ZOOM · REAR WHEELHOUSE REINFORCEMENT"),(P2,hi,(244,245,247),"ZOOM · REAR TRAILER-HITCH STRUCTURE")]

# markers on Edge (orig coords)
marks=[E(1880,690),E(2030,860)]
ov=Image.new('RGBA',(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
for (mx,my),(p,_,_,_) in zip(marks,panels):
    ax,ay=p[0],(p[1]+p[3])//2
    midx=ax-(40*SC if p is P1 else 22*SC)
    od.line([(mx,my),(midx,my),(midx,ay),(ax,ay)],fill=TEAL+(220,),width=2*SC,joint='curve')
    od.ellipse((mx-16*SC,my-16*SC,mx+16*SC,my+16*SC),fill=TEAL+(60,),outline=TEAL+(255,),width=2*SC)
    od.ellipse((mx-4*SC,my-4*SC,mx+4*SC,my+4*SC),fill=TEAL+(255,))
    od.ellipse((ax-7*SC,ay-7*SC,ax+7*SC,ay+7*SC),fill=TEAL+(255,))
canvas=canvas.convert('RGBA')
canvas=Image.alpha_composite(Image.alpha_composite(canvas,ov.filter(ImageFilter.GaussianBlur(8*SC))),ov)

for (p,img,bgc,title) in panels:
    pw,ph=p[2]-p[0],p[3]-p[1]
    sc=min((pw-24*SC)/img.width,(ph-24*SC)/img.height)
    im2=img.resize((int(img.width*sc),int(img.height*sc)),Image.LANCZOS)
    pan=Image.new('RGB',(pw,ph),bgc); pan.paste(im2,((pw-im2.width)//2,(ph-im2.height)//2))
    m=Image.new('L',(pw,ph),0); ImageDraw.Draw(m).rounded_rectangle((0,0,pw-1,ph-1),radius=20*SC,fill=255)
    g=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(g).rounded_rectangle((p[0]-4*SC,p[1]-4*SC,p[2]+4*SC,p[3]+4*SC),radius=24*SC,outline=TEAL+(255,),width=4*SC)
    canvas=Image.alpha_composite(canvas,g.filter(ImageFilter.GaussianBlur(9*SC)))
    canvas.paste(pan,(p[0],p[1]),m)
    d=ImageDraw.Draw(canvas)
    d.rounded_rectangle((p[0]-2*SC,p[1]-2*SC,p[2]+2*SC,p[3]+2*SC),radius=22*SC,outline=TEAL+(255,),width=3*SC)
    d.text((p[0],p[1]-38*SC),title,font=mono(19),fill=TEAL)
canvas.convert('RGB').resize((1600,861),Image.LANCZOS).save('assets/img/ford_edge_composite.jpg',quality=86,optimize=True,progressive=True)
