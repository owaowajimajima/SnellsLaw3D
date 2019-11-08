# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
from numpy import *
from scipy.linalg import norm


# %%
def rot(p, theta):
    pn = norm(p)
    n=p/pn
    R = array([[cos(theta) + (n[0]** 2)*(1 - cos(theta)), n[0] * n[1] * (1 - cos(theta)) - n[2] * sin(theta),n[0]*n[2]*(1-cos(theta))+n[1]*sin(theta)], [n[1] * n[0] * (1 - cos(theta)) + n[2] * sin(theta), cos(theta) + (n[1]** 2) * (1 - cos(theta)), n[1] * n[2] * (1 - cos(theta)) - n[0] * sin(theta)], [n[2] * n[0] * (1 - cos(theta)) - n[1] * sin(theta), n[2] * n[1] * (1 - cos(theta)) + n[0] * sin(theta), cos(theta) + (n[2]** 2) * (1 - cos(theta))]])
    return R
def rotm(n, theta):
    Rm = rot(n, theta * pi / 180)
    return Rm
def rotx(a):
    Rx = rot([1, 0, 0], a * pi / 180)
    return Rx
def roty(b):
    Ry = rot([0, 1, 0], b * pi / 180)
    return Ry
def F(q,w,e,r):
    R = roty(q).dot(rotx(w)).dot(rotx(e)).dot(roty(r)).dot(array([0,0,1]))
    return R


# %%
#ゴニオステージでの回転を入力
print("上のゴニオをl,r,f,bの順に入力しろ")
l, r, f, b = map(float, input().split())
print("下のゴニオをl2,r2,f2,b2の順に入力しろ")
l2, r2, f2, b2 = map(float, input().split())


# %%
veci = array(F(r2 - l2, f2 - b2, f - b, r - l))
t = cross(veci, array([0, 0, 1]))
thetai = arccos(inner(veci, [0, 0, 1]))
n = 1.168
thetar = (arcsin(sin(thetai) / n)) * 180 / pi
vecQ = rotm(t, -thetar).dot([0, 0, 1])
thetai = thetai * 180 / pi


# %%
print("空気中での角度 : %f" % thetai)
print("物質中での角度 : %f" % thetar)
print("物質中での座標" , end="")
print(vecQ)

