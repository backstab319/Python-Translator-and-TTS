from googletrans import Translator
translator = Translator()
inp = ""
output = translator.translate(inp,dest='kn')
print(output)