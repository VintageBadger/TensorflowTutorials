#import 'tensorflow'
import tensorflow as tf

#Initialize two constants
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

#multiply the two variables
result = tf.multiply(x1,x2)

#print
print(result)