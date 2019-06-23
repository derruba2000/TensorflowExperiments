import tensorflow as tf


# Basic assignment
value1=tf.constant(15)
print("1) Type " ,type(value1), " Value ", value1)


# Basic assignment with new name 
value1=tf.constant(15, name="value1")
print("2) Type " ,type(value1), " Value ", value1)

#Creating variable
SumVar=tf.Variable(value1 + 3, name="value1")
print("3) Var Type " ,type(SumVar), " Value ", SumVar)

init=tf.compat.v1.global_variables_initializer()


with tf.compat.v1.Session() as Sess:
    Sess.run(init)
    result=Sess.run(SumVar)
    
print("4) Result ", result, "Type", type(result))



