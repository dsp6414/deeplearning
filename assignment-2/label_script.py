import os
import random

def gen_data(dir):
    for category in os.listdir(dir):
        for item in os.listdir(dir + category):
            os.system("python label_data.py \"{0}\" {1}".format(dir + category + "/" + item, category))

def split_data(dir, split):
    categories = os.listdir(dir)
    splits = ['train', 'test']
    paths = {x : os.path.join(dir, x) for x in splits}
    for (key, value) in paths.items():
        os.mkdir(value)
        for cat in categories:
            os.mkdir(os.path.join(value, cat))
    for cat in categories:
        print "Starting category {0}".format(cat)
        temp = raw_input()
        location = os.path.join(dir, cat)
        file_all = os.listdir(location)
        files = random.sample(file_all, 3000)
        for i in xrange(len(splits)):
            ''' Count images in each category '''
            # sizes = {x : len(os.listdir(os.path.join(dir, x))) for x in categories}
            sizes = {x : 3000 for x in categories}
            items = random.sample(files, int(float(sizes[cat] * split[i])/100.0))
            files = [x for x in files if x not in items]
            for item in items:
                command = 'cp \"{0}\" {1}'.format(os.path.join(location, item), os.path.join(os.path.join(dir, splits[i]), cat))
                os.system(command)

if __name__ == '__main__':
    dir = "videos/"
    if not os.path.exists('data'):
        gen_data(dir)
    split_data('largeFace', [70,30])
