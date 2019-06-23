import tensorflow as tf

tf.reset_default_graph();

with tf.name_scope('Operations'):
    with tf.name_scope('Adds'):
        a=tf.add(2,2,name='add')
    with tf.name_scope('Mutls'):
        b=tf.multiply(a,3,name='mult')
        c=tf.multiply(b,a,name='mult2')



with tf.compat.v1.Session() as Sess:
    writer=tf.summary.FileWriter('../dist/outputJR', Sess.graph)
    print(Sess.run(c))