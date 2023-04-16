from distributor import ContentDistributor


class Consumer:
    id = None

    def __init__(self, distributor: ContentDistributor) -> None:
        self._distributor = distributor
        self._distributor.add_consumer(self)

    def read_data(self) -> None:
        while True:
            message = self._distributor.get_message(self)
            if not message:
                break
            print(f'Consumer {self.id}: {message}\n')

        print(f'Consumer {self.id}: Done\n')


class ConsumerA(Consumer):
    id = 1


class ConsumerB(Consumer):
    id = 2
