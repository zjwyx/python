from multiprocessing import Process,Manager,Lock

def change_dic(dic):
    with lock:
        dic['count'] -= 1



if __name__ == '__main__':
    lock = Lock()
    m = Manager()
    dic = m.dict({'count':100})
    p_1 = []
    for i in range(100):
        p = Process(target=change_dic,args=(dic,))
        p.start()
        p_1.append(p)
    for p in p_1:
        p.join()
    print(dic)
