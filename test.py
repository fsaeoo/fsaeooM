from flask import *
import fsaeooMParser


app = Flask(__name__)
@app.route("/")
def homepage(): 
    template =fsaeooMParser.fparse("""
@~~ comment
text
;;text;;
//text// 
__text__ 
``text`` 
~~text
text~~ 
#1#heading#1#
#2#heading#2#
#3#heading#3#
#4#heading#4#
#5#heading#5#
#6#heading#6#
''Element''


                                  
                                        """)
    context = {}
    return template

app.run(debug=True)
# print(fsaeooMParser.fparse("""
# @~~ comment
# text
# ;;text;;
# //text// 
# __text__ 
# ``text`` 
# ~~text
# text~~ 
# #heading#
# ##heading##
# ###heading###
# ####heading####
# #####heading#####
# ######heading######
# ''List''

                                  
#                                         """))

# print(fsaeooMParser.fparse("""@~~ comment <br>
#      newline here //italic//
#     ;;bold;; """))
