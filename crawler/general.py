import os
import re


def create_Data_directory(directory):
    if not os.path.exists(directory):
        print('Creating directory: ' + directory)
        os.makedirs(directory)


def create_Data_files(directory_name, base_url):
    queue = directory_name + '/queue.txt'
    crawled = directory_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    f = open(path, 'w')  # set write mode
    f.write(data)
    f.close()


def append_to_file(path, data):
    file = open(path, 'a')  # append mode
    file.write(data + '\n')
    file.close()


def delete_file_contents(path):
    file = open(path, 'w')
    file.truncate()  # the same as delete all contents
    file.close()


def file_to_set(path):
    results = set()
    f = open(path, 'rt')  # read *.txt file
    for line in f:
        result = line.replace('\n', '')
        results.add(result)  # strip \n character
    f.close()
    return results


def set_to_file(links, path):
    delete_file_contents(path)
    for link in sorted(links):  # for the url is obey a nice order
        append_to_file(path, link)
