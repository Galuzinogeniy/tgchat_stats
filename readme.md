# tgchat_stats

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Usage](#usage)
- [Data Format](#data-format)
- [Examples](#examples)
- [License](#license)
- [Contributing](#contributing)
- [Authors](#authors)

## Description

**tgchat_stats** is a python script that is designed to parse a telegram chat exported to JSON. The script gives some statistics about the messages of each chat participant.

## Features

- Counts the total number of messages in the chat.
- Calculates the total length of all messages combined.
- Determines the average length of messages in the chat.
- Identifies the most common words used in the chat.
- Calculates the total duration of voice messages in hours, minutes, and seconds.
- Filters statistics based on individual chat participants.
- Displays the percentage of Russian letter "ы" in the chat messages.
- Provides information about the share of messages in the chat compared to the total number of messages.
- and other interesting stats of messages

## Usage

0. Export chat data with telegram desktop
1. Place the data file (data.json)* in the directory with the script
	* when exporting, the file may be named result.json, in which case it must be renamed
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:

   ```bash
   python main.py
   ```

4. The script will prompt you to select a chat participant for which you want to see the statistics. You can also choose the "all" option to analyze the entire chat.
(to test the script, you can change the name of the test.json file to data.json)


## Data Format
I don't know how data is exported from other platforms, but the script works with this format:

```json
{
  "type": "personal_chat",
  "messages": [
    {
      "type": "message",
      "from": "participant_name",
      "text": "message_text",
      "media_type": "media_type (optional)",
      "duration_seconds": "duration (optional)"
    },
    {
      ...
    }
  ]
}
```

Replace "participant_name" with the sender's name, "message_text" with the content of the message, "media_type" with the type of media if it's a voice or video message, and "duration_seconds" with the duration of the media if applicable.

## Examples

I copied this readme template from the Internet and I do not know what to indicate in the examples, everything seems to be clear anyway. But here is the cat:
         ,    ,
        | \--/ |
        ( (0_0)(
         \==Y==/
         /'-"-'>
       _/ < ; (;
      / ,_ |_|_\
     ( _,,)\,,),)
     \ '.___
      '-----'

However, here is an example of how it works:

main.py
 
1 Арнольд Шварцнегер
2 Матвей
3 Zor Nudle
4 Bor Buble
5 Горящий медведь
6 YT ПФДГЯШТЩПУТШН
7 Кто?
8 Степан Егоренко
9 Viktor
а all

Выберите участника чата|Select a chat participant
8

Степан Егоренко:
Колличество сообщений|Number of messages: 14293
Длина сообщений|Messages length: 568001
Количесвто слов|Number of words: 48557
Средняя длина сообщения|Average message length:: 39.7
Количество голосовых|Number of voices: 2
Количество кружочков|Number of video messages: 1
Суммарная длинна голосовых|Total voices duration: 0:37:16
Доля сообщений в чате|Share of messages in the chat: 67.0%
Колличество ы|Number of 'ы': 18784
Среднее количество ы в сообщении|Percentage of 'ы' in messages: 3.3%
Количество уникальных слов|Number of unique words: 34525
Самые частые слова|Most common words: 
*ыыыы, этому тут не место*

Вывести самое длинное сообщение? 1/0|Print the longest message? 1/0
1
Самое длинное сообщение|Longest message: это самое длинное сообщение, в нем много полезной информации. вы не поверите, но с новой кисточкой от максфактор мои ресницы вышли из-под контроля и накинулись на ученых, которые испытывали на них новое биологическое оружие. в результате укусов и скрещивания их днк появился новый вирус, делающий людей агрессивными, голодными и невосприимчивыми к боли. в первый же день было заражено более 40 тысяч человек, я собственными глазами видел, как люди, укушенные ресницами, в считанные минуты сами становились ресницами и набрасывались на своих друзей и родных. планету охватила паника, вирус распространился так быстро, что мы лишились наших лидеров, лишились надежды, потеряли всё. даже те, кому удалось остаться не зараженными, начали терять свой человеческий облик, человеческий разум. мир погрузился во тьму. тьму объёмную, длинную и без комочков. проклятый максфактор.
Вывести словарь? 1/0|Print the dictionary? 1/0
0



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
(янезнаючтоэтозначит)

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to create a pull request. I'm new to programming and this is my first github project, any feedback would be greatly appreciated.

## Authors

     _________
    / ======= \
   / __________\
  | ___________ |
  | |     ыыы | |
  | | 0_0     | |
  | |_________| |________________________
  \=____________/   Galuzinogeniy(https://github.com/Galuzinogeniy))
  / """"""""""" \                       /
 / ::::::::::::: \                  =D-'
(_________________)