import tensorflow as tf


# Working with constants example
valor1=tf.constant(1)
valor2=tf.constant(2)
print("Type---->",type(valor1), " Value:", valor1)

soma=valor1+valor2
print("soma---->", soma, type(soma))


# running the graphs
with tf.Session() as Sess:
    s=Sess.run(soma)
    
    
print("Result:",s , "type", type(s))



