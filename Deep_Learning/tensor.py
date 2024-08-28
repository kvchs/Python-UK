import tensorflow as tf

# 使用 tf.Variable 创建一个可变的张量
a = tf.Variable(0.0, dtype=tf.float32)


# 使用 tf.function 来定义一个函数，在函数内使用 tf.TensorSpec 模拟 placeholder 的行为
@tf.function
def my_function(a_input):
    # 假设 a_input 是一个输入张量
    b = a_input + 1
    return b


# 定义输入张量的规格
a_spec = tf.TensorSpec(shape=(), dtype=tf.float32)

# 创建一个具体的张量
a_tensor = tf.constant(0.0, dtype=tf.float32)

# 调用函数
result = my_function(a_tensor)
print(result)
