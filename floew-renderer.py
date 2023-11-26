from flask import *
import floewParser

app = Flask(__name__)
@app.route("/")
def homepage(): 
    template =floewParser.fparse("""
    @~~ comment
    text
                                      ;;text;;
                                      //text// 
                                      __text__ 
                                      ``text`` 
                                      ~~text
                                    text~~ 
                                 #heading#
                                        """)
    context = {}
    return template

app.run(debug=True)

# print(floewParser.fparse("""@~~ comment <br>
#      newline here //italic//
#     ;;bold;; """))

