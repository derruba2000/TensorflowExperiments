import tensorflow as tf

# Numbers
# Working with constants example
valor1=tf.constant(1)
valor2=tf.constant(2)
print("Type---->",type(valor1), " Value:", valor1)

soma=valor1+valor2
print("soma---->", soma, type(soma))

# running the graphs
with  tf.compat.v1.Session() as Sess:
    s=Sess.run(soma)
    
print("Result:",s , "type", type(s))

# Strings
String1=tf.constant("String 1")
String2=tf.constant("String 2")
print("Type---->", type(String1), "Value:", String1)

# Running the graphs
with  tf.compat.v1.Session() as Sess:
    StringConcat=Sess.run(String1 + String2)

print("Result String", StringConcat, "Type", type(StringConcat))