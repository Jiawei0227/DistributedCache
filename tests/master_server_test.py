import requests
import unittest
import threading
import logging, sys
unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: x < y

logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

class TestMasterServer(unittest.TestCase):
    def setUp(self):
        self.url = "http://0.0.0.0:5000/"
        self.kv_url = self.url + "kv"

    def test_1_post(self):
        data = {'key': 'test_key', 'value': 'test_val'}
        logger.debug("POST {0}".format(str(data)))
        r = requests.post(self.kv_url, data=data)
        logger.info("re: {0}".format(r.text))

    def test_2_get(self):
        payload = 'key=test_key'
        logger.debug("GET {0}".format(str(payload)))
        r = requests.get(self.kv_url+'?'+payload)
        logger.info("re: {0}".format(r.text))

    def test_3_lease_thundering_herd(self):
        """one of the get thread should be cache miss, and all others be cache hit"""
        data = {'key': 'hello8', 'value': 'world'}
        logger.debug("POST " + str(data))
        r = requests.post(self.kv_url, data=data)
        payload1 = {'key=hello8'}
        thread1 = threading.Thread(target=send_get_thread, args=(payload1))
        thread2 = threading.Thread(target=send_get_thread, args=(payload1))
        thread3 = threading.Thread(target=send_get_thread, args=(payload1))
        thread1.start()
        thread2.start()
        thread3.start()

        thread1.join()
        thread2.join()
        thread3.join()
        

def send_get_thread(payload):
    logger.info(payload)
    r = requests.get("http://0.0.0.0:5000/kv", params=payload)
    logger.info("re for thread {0} : {1}".format(threading.current_thread().getName(), r.text))

if __name__ == '__main__':
    unittest.main()