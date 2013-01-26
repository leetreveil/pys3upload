import unittest
import mocks
import sys
import threading
import s3upload


class upload_tests(unittest.TestCase):

    def test_should_be_able_to_upload_data(self):
        input = ['12', '345']
        mocks.state['mock_boto_s3_multipart_upload_data'] = []
        s3upload.upload('test_bucket', 'some_key', 'some_secret', input, 'some_key', connection=mocks)
        self.assertEqual(mocks.state['mock_boto_s3_multipart_upload_data'], ['12', '345'])

class upload_part_tests(unittest.TestCase):
    
    def test_should_return_error_when_upload_func_raises_error(self):
        def upload_func(*args, **kwargs):
            raise Exception()

        with self.assertRaises(threading.ThreadError):
            raise s3upload.upload_part(upload_func, '_', '_', '_')

    def test_should_retry_upload_five_times(self):
        counter = [0]
        def upload_func(*args, **kwargs):
            counter[0] += 1
            raise Exception()

        s3upload.upload_part(upload_func, '_', '_', '_')
        self.assertEqual(counter[0], 5)

class doc_collector_tests(unittest.TestCase):

    def test_should_be_able_to_read_every_byte_of_data(self):
        input = ['12345']
        result = list(s3upload.data_collector(input, def_buf_size=3))
        self.assertEqual(result, ['123', '45'])

    def test_should_be_able_to_read_single_yield(self):
        input = ['123']
        result = list(s3upload.data_collector(input, def_buf_size=3))
        self.assertEqual(result, ['123'])

    def test_should_be_able_to_yield_data_less_than_buffer_size(self):
        input = ['123']
        result = list(s3upload.data_collector(input, def_buf_size=6))
        self.assertEqual(result, ['123'])

    def test_a_single_item_should_still_be_buffered_even_if_it_is_above_the_buffer_size(self):
        input = ['123456']
        result = list(s3upload.data_collector(input, def_buf_size=3))
        self.assertEqual(result, ['123', '456'])

    def test_should_return_rest_of_data_on_last_iteration(self):
        input = ['1234', '56']
        result = list(s3upload.data_collector(input, def_buf_size=3))
        self.assertEqual(result, ['123', '456'])

if __name__ == '__main__':
    unittest.main()