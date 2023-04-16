from threading import Thread

from consumer import ConsumerA, ConsumerB
from distributor import ContentDistributor
from producer import FileReader


def main():
    distributor = ContentDistributor()
    consumer_a = ConsumerA(distributor)
    consumer_b = ConsumerB(distributor)

    fr = FileReader(distributor)

    t1 = Thread(target=consumer_a.read_data)
    t2 = Thread(target=consumer_b.read_data)

    t1.start()
    t2.start()

    t3 = Thread(target=fr.forward)
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == '__main__':
    main()
