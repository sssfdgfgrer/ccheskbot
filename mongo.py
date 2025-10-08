import pymongo
from bson import ObjectId
from pymongo.collection import Collection
teleclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
# teleclient["admin"].authenticate("root", "pwdczml12")

teledb = teleclient["GTH_ugeojbk518bot"]
bot = teledb['bot']
user = teledb['user']
hch = teledb['hch']
ggh = teledb['ggh']
fyb = teledb['fyb']
gzpd = teledb['gzpd']
xgmz = teledb['xgmz']
xgjj = teledb['xgjj']
cji = teledb['cji']
fxi = teledb['fxi']
yhmfx = teledb['yhmfx']
qfck = teledb['qfck']
keytext = teledb['keytext']


def keydata(bianhao, key, money):
    keytext.insert({
        'bianhao': bianhao,
        'key': key,
        'money': money
    })

def fanyibao(projectname, text, fanyi):
    fyb.insert_one({
        'projectname':projectname,
        'text': text,
        'fanyi': fanyi
    })
    
def jiancehao(projectname, uid, phone):
    hch.insert_one({
        'projectname': projectname,
        'uid': uid,
        'phone': phone
    })



def user_data(key_id, user_id, username, fullname, lastname, state, creation_time, last_contact_time):
    user.insert_one({
        'count_id': key_id,
        'user_id': user_id,
        'username': username,
        'fullname': fullname,
        'lastname': lastname,
        'state': state,
        'creation_time': creation_time,
        'last_contact_time': last_contact_time,
        'sign': 0,
        'USDT': 0,
        'ptgrade': '新用户'

    })



if __name__ == '__main__':

    user.update_many({},{"$set":{"ptgrade": '新用户'}})
    # print(keyboard)
    # shangtext.insert_one({
    #     'projectname': '广告位文本',
    #     'text': 1
    # })
    # shangtext.insert_one({
    #     'projectname': '广告位',
    #     'text': 1
    # })
    # shangtext.insert_one({
    #     'projectname': '赔率',
    #     'text': 1.8
    # })
    # shangtext.insert_one({
    #     'projectname': '反水',
    #     'text': 0.02
    # })
    # shangtext.insert_one({
    #     'projectname': '抽水',
    #     'text': 0.05
    # })
    pass
