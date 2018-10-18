
from google.cloud import translate
import os.path

file_to_translate = input('Type file name to translate\n')
file_check = os.path.exists(file_to_translate)

while file_check == False:
    file_to_translate = input('Type file name to translate\n')
    file_check = os.path.exists(file_to_translate)

text = open(file_to_translate, 'r')
target_language = input('Type target language (shortened form)\n')

translate_client = translate.Client()
translation = translate_client.translate(
                    text.read(),
                    target_language=target_language)
    #text = translation["translatedText"]

translated_file_path = 'translated-{file_to_translate}-to-{target_language}.txt'.format(file_to_translate=file_to_translate, target_language = target_language)

text_file = open(translated_file_path, "w")
text_file.write(translation["translatedText"])
text_file.close()

print('Translation done')
