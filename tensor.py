#!/usr/bin/envpython3
#-*-coding:utf-8-*-

import tensorflow as tf
#定义‘符号’变量，也称为占位符
a=tf.placeholder("float", [None, 3])
b=tf.placeholder("float", [None, 3])

y=a*b#构造一个op节点
y_=tf.matmul(a,b)
sess=tf.Session()#建立会话
#运行会话，输入数据，并计算节点，同时打印结果
print(sess.run(y,feed_dict={a:[[1,2,1],[0,1,0], [1,2,3]],b:[[1,2,1],[0,1,0], [1,2,3]]}))
print(sess.run(y_,feed_dict={a:[[1,2,1],[0,1,0], [1,2,3]],b:[[1,2,1],[0,1,0], [1,2,3]]}))
#任务完成,关闭会话.
sess.close()