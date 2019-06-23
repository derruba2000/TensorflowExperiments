import tensorflow as tf


# Dot product example
varTMP=tf.constant([[1.0,2.0,-1.0]], name="inputs")
weightsTMP=tf.constant([[.1,.2,.3]], name="weights")

multTMP=tf.multiply(varTMP, weightsTMP)

sumTMP=tf.reduce_sum(multTMP)

with tf.compat.v1.Session() as Sess:
    result=Sess.run(multTMP)
    result2=Sess.run(sumTMP)


print("--->", result, result2)




