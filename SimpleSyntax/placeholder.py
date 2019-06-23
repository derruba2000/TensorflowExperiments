import tensorflow as tf



p=tf.compat.v1.placeholder('float', None)

operacao=p+2

with tf.compat.v1.Session() as Sess:
    result=Sess.run(operacao, feed_dict={p:[1,2,3]})
    print("--->",result)

