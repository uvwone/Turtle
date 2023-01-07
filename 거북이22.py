import turtle as t
import random as r

t.shape('turtle')
t.speed(0)
li = ['red', 'green', 'blue']

num = 0
for i in range(10000):
      num = i % len(li)
      t.color(r.choice(li))
      t.fd(i)
      t.right(90)
