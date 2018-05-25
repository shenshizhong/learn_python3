import logging

logging.basicConfig(level= logging.INFO)  #  注意一定要写这个，不然就不会输出信息
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
