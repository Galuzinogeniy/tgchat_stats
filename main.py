import json
from collections import Counter


def multi_replace(string):
    replacements = ['.', '?', ',', '!', '\'', '\"', '(', ')', '*', '«', '»',
                    '{', '}', '[', ']', '/', '-', '_', ':', ';', '+', '=']
    for elm in replacements:
        string = string.replace(elm, '')
    return string


def remove_elements(lst, value):
    while value in lst:
        lst.remove(value)


def convert_seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds


def msgs_stats(name='all'):
    msgs_count = 0
    msgs_text = ''
    msgs = []
    words = []
    voices_count = 0
    video_msgs_count = 0
    duration = 0

    # Common words that will be excluded from the analysis
    ban_list = """я как кто себя тебе — мы ты да нет в с но а и под на или для вы от про без ли из
               за он она оно они их что же бы меня мне там к чем тут того этом тогда где
               i as who yourself to we you yes no in with but and under on or for they their what then where why so from of 
               about that that would me to them them there who this then where when where this then where"""

    # Open and read the "data.json" file which contains the chat data
    with open("data.json", "r", encoding='utf-8') as json_file:

        data = json.load(json_file)

        for msg in data["messages"]:

            if msg["type"] == "message" and (msg["from"] == name or name == 'all'):    # Check if the message is a regular message and sent by the specified participant

                if "media_type" in msg and msg["media_type"] == "voice_message":
                    voices_count += 1
                    try:
                        duration += msg["duration_seconds"]
                    except BaseException:
                        pass

                elif "media_type" in msg and msg["media_type"] == "video_message":
                    video_msgs_count += 1
                    try:
                        duration += msg["duration_seconds"]
                    except BaseException:
                        pass

                try:
                    msgs_count += 1
                    msgs_text += msg["text"] + ' '
                    msgs.append(msg["text"])
                    temp_words_arr = msg["text"].split(' ')

                    for word in temp_words_arr:
                        word = multi_replace(word).lower()

                        if word not in ban_list:
                            words.append(word)

                except BaseException:
                    pass

        msgs.sort(key=len)
        longest_msg = msgs[-1]
        remove_elements(words, '')
        msgs_len = len(msgs_text)
        average_msg_len = msgs_len / msgs_count
        most_common_words = Counter(words).most_common(10)
        share_of_total = round(msgs_count / len(data['messages']), 3) * 100

    return dict(name=name, msgs_count=msgs_count, msgs_len=msgs_len, average_msg_len=average_msg_len,
                longest_msg=longest_msg, most_common_words=most_common_words, voices_count=voices_count,
                videomsgs_count=video_msgs_count, duration=duration, share_of_total=share_of_total,
                words=words, bl_count=msgs_text.count('ы'), msgs_text=msgs_text)


def printer(dt):
    print(f"{dt['name']}:")
    print("Колличество сообщений|Number of messages:", dt['msgs_count'])
    print("Длина сообщений|Messages length:", dt['msgs_len'])
    print(f"Количесвто слов|Number of words: {len(dt['words'])}")
    print("Средняя длина сообщения|Average message length::", round(dt['average_msg_len'], 1))
    print("Количество голосовых|Number of voices:", dt['voices_count'])
    print("Количество кружочков|Number of video messages:", dt['videomsgs_count'])
    duration = convert_seconds_to_hms(dt['duration'])
    print("Суммарная длинна голосовых|Total voices duration:", f'{duration[0]}:{duration[1]}:{duration[2]}')
    print(f"Доля сообщений в чате|Share of messages in the chat: {dt['share_of_total']}%")
    print(f"Колличество ы|Number of 'ы': {dt['bl_count']}")
    print(f"Среднее количество ы в сообщении|Percentage of 'ы' in messages: {round(dt['bl_count'] / dt['msgs_len'], 5) * 100}%")
    print(f"Количество уникальных слов|Number of unique words: {len(set(dt['words']))}")
    print("Самые частые слова|Most common words:")

    for k, elm in enumerate(dt['most_common_words']):
        print(k+1, elm)

    flag = input("Вывести самое длинное сообщение? 1/0|Print the longest message? 1/0\n")
    if flag == '1':
        print("Самое длинное сообщение|Longest message:", dt['longest_msg'])

    flag2 = input("Вывести словарь? 1/0|Print the dictionary? 1/0\n")
    if flag2 == '1':
        dic = list(set(dt['words']))
        dic.sort()
        for elm in dic:
            print(elm)


def main():
    with open("data.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Get the list of chat participants and add 'all' option to analyze all participants
    members = []
    if data["type"] == 'personal_chat':
        for elm in data["messages"]:
            members.append(elm["from"])
        members = list(set(members))
    else:
        members = data['messages'][0]['members']
    members.append('all')

    # Print the list of participants and prompt the user to select one
    for i, elm in enumerate(members):
        print(i+1, elm)
    name = members[int(input("Выберите участника чата|Select a chat participant\n")) - 1]
    printer(msgs_stats(name))


if __name__ == "__main__":
    main()