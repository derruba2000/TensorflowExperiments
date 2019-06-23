import tensorflow as tf


# Variables with vectores
vectorVar=tf.constant([10,32,34], name="vector")
print("1)---->",vectorVar, "Type", type(vectorVar))

SumVar=tf.Variable(vectorVar + 1)
init=tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as Sess:
    Sess.run(init)
    result=Sess.run(SumVar)
print("4) Result ", result, "Type", type(result))


# with for loop
vTMP=tf.Variable(0)
init2=tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as Sess:
    Sess.run(init2)
    for k in range(5):
        vTMP=vTMP+1
        print("5)->",Sess.run(vTMP))


    


