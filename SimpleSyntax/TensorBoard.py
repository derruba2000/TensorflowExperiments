import tensorflow as tf

tf.reset_default_graph();

a=tf.add(2,2,name='add')
b=tf.multiply(a,3,name='mult')
c=tf.multiply(b,a,name='mult2')



with tf.compat.v1.Session() as Sess:
    writer=tf.summary.FileWriter('../dist/outputJR', Sess.graph)
    print(Sess.run(c))