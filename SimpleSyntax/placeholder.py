import tensorflow as tf



p=tf.compat.v1.placeholder('float', None)

operacao=p+2

with tf.compat.v1.Session() as Sess:
    result=Sess.run(operacao, feed_dict={p:[1,2,3]})
    print("--->",result)


p2=tf.compat.v1.placeholder('float', [None,5])
operation2=p2*5

with tf.compat.v1.Session() as Sess:
    dataTMP=[[1,2,3,4,5],[6,7,8,9,10]]
    result=Sess.run(operation2, feed_dict={p2:dataTMP})
    print("--->",result)