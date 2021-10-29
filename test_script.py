import requests
import pytest
import json

class Test:
    def test1(self):
        link = 'https://jsonplaceholder.typicode.com/posts'

        response1 = requests.get(link)

        print(response1.status_code)
        print(response1.text)
        print(response1.headers)

    def test2(self):
        link = 'https://jsonplaceholder.typicode.com/posts'

        response2 = requests.post(link, {"title": "foo", "body": "bar", "userid": 1})

        print(response2.status_code)
        print(response2.text)
        print(response2.headers)

    def test3(self):
        link= 'https://jsonplaceholder.typicode.com/posts/1'

        response3 = requests.get(link)

        print(response3.status_code)
        print(response3.text)
        print(response3.headers)

    def test4(self):
        link = 'https://jsonplaceholder.typicode.com/posts/1'
        response4 = requests.put(link, {"id": 1, "title": "foo", "body": "bar", "userid": 1})

        print(response4.status_code)
        print(response4.text)
        print(response4.headers)

    def test5(self):
        link = 'https://jsonplaceholder.typicode.com/posts/1'
        response5 = requests.patch(link, {"title": "foo1"})

        print(response5.status_code)
        print(response5.text)
        print(response5.headers)


    def test6(self):
        link = 'https://jsonplaceholder.typicode.com/posts/1'

        response6 = requests.delete(link)

        print(response6.status_code)
        print(response6.text)
        print(response6.headers)

    def test7(self):
        link = 'https://jsonplaceholder.typicode.com/posts/1/comments'

        response7 = requests.get(link)

        print(response7.status_code)
        print(response7.text)
        print(response7.headers)

    def test8(self):
        link = 'https://jsonplaceholder.typicode.com/albums/1/photos'

        response8 = requests.get(link)

        print(response8.status_code)
        print(response8.text)
        print(response8.headers)

    def test9(self):
        link = 'https://jsonplaceholder.typicode.com/users/1/albums'

        response9 = requests.get(link)

        print(response9.status_code)
        print(response9.text)
        print(response9.headers)

    def test10(self):
        link = 'https://jsonplaceholder.typicode.com/users/1/todos'

        response10 = requests.get(link)

        print(response10.status_code)
        print(response10.text)
        print(response10.headers)

    def test11(self):
        link = 'https://jsonplaceholder.typicode.com/users/1/posts'

        response11 = requests.get(link)

        print(response11.status_code)
        print(response11.text)
        print(response11.headers)



t = Test()
t.test1()
t.test2()
t.test3()
t.test4()
t.test5()
t.test6()
t.test7()
t.test8()
t.test9()
t.test10()
t.test11()

