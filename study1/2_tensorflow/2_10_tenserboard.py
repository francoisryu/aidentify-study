import tensorflow as tf

a = tf.constant(1)
b = tf.constant(2)

sess = tf.Session()
with tf.Session() as sess:
    print(sess.run(a + b))
    print(sess.run(a - b))

    # TensorBoard 그래프용 로그 기록
    merged = tf.summary.merge_all()

    writer = tf.summary.FileWriter("/tmp/tensorboard", sess.graph)
    writer.close()
