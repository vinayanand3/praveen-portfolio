"""Builds the Rivian composite slide image. Run from the repo root: python3 tools/compose_rivian.py"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
SC=2; W,H=1600*SC,861*SC
BG=(11,13,16); TEAL=(51,214,193)
mono=lambda s: ImageFont.truetype('/System/Library/Fonts/SFNSMono.ttf',s*SC)
canvas=Image.new('RGBA',(W,H),BG+(255,))
# ---- van panel (keeps its studio grey background) ----
van=Image.open('source/images/rivian-edv-amazon.jpeg').convert('RGB')
vb=(0,0,1172,925)
vx0,vy0,vx1,vy1=40*SC,222*SC,620*SC,700*SC
s=min((vx1-vx0)/van.width,(vy1-vy0)/van.height)
vimg=van.resize((int(van.width*s),int(van.height*s)),Image.LANCZOS)
vx1=vx0+vimg.width; vy1=vy0+vimg.height
m=Image.new('L',vimg.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,vimg.width-1,vimg.height-1),radius=18*SC,fill=255)
canvas.paste(vimg,(vx0,vy0),m)
# underbody / skateboard highlight on van (orig coords)
poly=[(300,700),(560,668),(1040,470),(1118,430),(1120,500),(1060,560),(560,800),(330,790)]
poly=[(vx0+x*s,vy0+y*s) for x,y in poly]
ov=Image.new('RGBA',(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
od.polygon(poly,fill=TEAL+(70,))
od.line(poly+[poly[0]],fill=TEAL+(255,),width=2*SC,joint='curve')
# zoom panel geometry
CROP=(470,470,4200,2090)
_sk=Image.open('source/images/rivian-skateboard.jpeg').convert('RGB').crop(CROP)
px0,px1=700*SC,1560*SC
_ph=int((px1-px0-30*SC)*_sk.height/_sk.width)+30*SC
_cy=(vy0+vy1)//2; py0,py1=_cy-_ph//2,_cy+_ph-_ph//2
anchor=(px0,(py0+py1)//2)
sx,sy=int(vx0+1120*s),int(vy0+470*s)
mx=(sx+anchor[0])//2
od.line([(sx,sy),(mx,sy),(mx,anchor[1]),anchor],fill=TEAL+(220,),width=2*SC,joint='curve')
od.ellipse((sx-6*SC,sy-6*SC,sx+6*SC,sy+6*SC),fill=TEAL+(255,))
canvas=Image.alpha_composite(Image.alpha_composite(canvas,ov.filter(ImageFilter.GaussianBlur(8*SC))),ov)
# ---- skateboard zoom panel ----
sk=_sk
pw,ph=px1-px0,py1-py0
ss=min((pw-30*SC)/sk.width,(ph-30*SC)/sk.height)
sk=sk.resize((int(sk.width*ss),int(sk.height*ss)),Image.LANCZOS)
panel=Image.new('RGB',(pw,ph),(255,255,255)); ox,oy=(pw-sk.width)//2,(ph-sk.height)//2; panel.paste(sk,(ox,oy))
pm=Image.new('L',(pw,ph),0); ImageDraw.Draw(pm).rounded_rectangle((0,0,pw-1,ph-1),radius=22*SC,fill=255)
pg=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(pg).rounded_rectangle((px0-4*SC,py0-4*SC,px1+4*SC,py1+4*SC),radius=26*SC,outline=TEAL+(255,),width=4*SC)
canvas=Image.alpha_composite(canvas,pg.filter(ImageFilter.GaussianBlur(10*SC)))
canvas.paste(panel,(px0,py0),pm)
cd=ImageDraw.Draw(canvas)
cd.rounded_rectangle((px0-2*SC,py0-2*SC,px1+2*SC,py1+2*SC),radius=24*SC,outline=TEAL+(255,),width=3*SC)
cd.ellipse((anchor[0]-8*SC,anchor[1]-8*SC,anchor[0]+8*SC,anchor[1]+8*SC),fill=TEAL)
# callout on battery-to-frame joint (orig skateboard coords -> panel)
def P(x,y): return (px0+ox+(x-CROP[0])*ss, py0+oy+(y-CROP[1])*ss)
jx,jy=P(2600,1225)  # frame rail / battery pack side edge
lx,ly=jx+10*SC, jy+110*SC
cd.ellipse((jx-9*SC,jy-9*SC,jx+9*SC,jy+9*SC),outline=TEAL,width=3*SC)
cd.ellipse((jx-3*SC,jy-3*SC,jx+3*SC,jy+3*SC),fill=TEAL)
cd.line([(jx,jy+9*SC),(lx,ly)],fill=TEAL,width=2*SC)
label="BATTERY ↔ FRAME MARRIAGE JOINT"; f=mono(14)
tw=cd.textlength(label,font=f); bx0,by0=lx-tw/2-12*SC,ly
cd.rounded_rectangle((bx0,by0,bx0+tw+24*SC,by0+30*SC),radius=6*SC,fill=TEAL)
cd.text((bx0+12*SC,by0+7*SC),label,font=f,fill=(6,32,28))
cd.text((vx0,vy0-40*SC),"RIVIAN EDV · AMAZON DELIVERY VAN",font=mono(15),fill=(150,158,168))
cd.text((px0,py0-48*SC),"ZOOM · SKATEBOARD PLATFORM",font=mono(22),fill=TEAL)
cd.text((px0,py1+18*SC),"Resident launch engineer for the skateboard structure",font=mono(15),fill=(150,158,168))
canvas.convert('RGB').resize((1600,861),Image.LANCZOS).save('assets/img/rivian_skateboard_composite.jpg',quality=86,optimize=True,progressive=True)
