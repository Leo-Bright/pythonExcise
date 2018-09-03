import requests
import json
import datetime
import xlrd
import time

# meta data
chat = {}
product_id = 1
question = "如何开票"


# get and init chats
def get_chats(id):
    get_chat_data = {"product_id": id}
    res_chats = requests.post('http://web-ui.dev.example.com/api/chats', data=json.dumps(get_chat_data))
    result_chats = json.loads(res_chats.content)
    chat["id"] = result_chats["chat"]["id"]
    chat["name"] = result_chats["bot"]["name"]
    print(chat)


def get_now():
    return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')


# send customer msg
send_msg_url = 'http://web-ui.dev.example.com/api/messages/' + str(product_id)


def read_data(data_path):

    work_book = xlrd.open_workbook(data_path)
    sheet = work_book.sheet_by_index(0)
    row = len(sheet._cell_values)
    result_data = []
    for i in range(1, row):
        rowValues = sheet.row_values(i)
        result_data.append(rowValues[1:])
    return result_data


def get_answer(question):

    send_msg_data = {
        "chat": chat,
        "content":
            {
                "type": 'txt',
                "body": question if question else "hello world",
            },
        "posted_at": get_now() if get_now() else "2018-01-01T08:00:00Z",
    }
    res_send = requests.post(send_msg_url, data=json.dumps(send_msg_data))
    res_send.raise_for_status()
    result_send = json.loads(res_send.content)
    # this is answer
    answer = result_send["content"]["body"]
    return answer

if __name__ == "__main__":
    data_path = 'wsy.xlsx'
    out_qa = 'result/out_qa.json'
    get_chats(product_id)
    q_data = read_data(data_path)
    qa_len = len(q_data)
    result = {}
    count = 0
    for q_sub in q_data:
        for q in q_sub:
            count += 1
            print("count:", count)
            print("qustion:", q)
            try:
                ans = get_answer(q)
            except:
                time.sleep(10)
                get_chats(product_id)
                ans = get_answer(q)
            print("answer:", ans)
            if q not in result.keys():
                result[q] = ans

    js_res = json.dumps(result, indent=0, ensure_ascii=False)
    res = open(out_qa, 'w')
    res.write(js_res)
    res.close()









