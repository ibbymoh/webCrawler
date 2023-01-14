import os


def create_project_dic(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


# create que and crawl file

def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        # if this is not a file then we create the file
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# add data unto an existing file

def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# delete the contents of a file
# the readline method returns a list of the lines in  a file
def delete_contents(path):
    with open(path, 'w') as file:
        pass


# Sets allow us to have unique values so we read a file and convert each line to set items

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            # we replace the line value and then add to our set
            results.add(line.replace('\n', ''))
    return results


def set_to_file(links, file):
    delete_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
