import time


def test_tqdm():
    from tqdm import tqdm

    for _ in tqdm(range(1000)):
        time.sleep(0.001)


def test_alive_bar():
    # pycharm 设置, Edit Configuration - Emulate terminal in output console
    from alive_progress import alive_bar

    for x in 1000, 1500, 700, 0:
        with alive_bar(x) as bar:
            for i in range(1000):
                time.sleep(.005)
                bar()


if __name__ == '__main__':
    test_alive_bar()
    test_tqdm()
