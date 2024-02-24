x = 10
y = 20

temp = x
x = y
y = temp

print("x=" + str(x))
print("y=" + str(y))

#%%
#python'a Özel verilerin yerini değistirme

x = 10
y = 20

x,y = y,x

print("x=" + str(x))
print("y=" + str(y))

# %%

m = 10
a = 50


m,a = a,m

print("m = ",str(m))
print("a = ",str(a))