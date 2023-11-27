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
                                 #heading#
                                  ##heading##
                                  ###heading###
                                  ####heading####
                                  #####heading#####
                                  ######heading######
                                  
                                  
                                  
                                  
                                  text
                                        """)
    context = {}
    return template

app.run(debug=True)

# print(fsaeooMParser.fparse("""@~~ comment <br>
#      newline here //italic//
#     ;;bold;; """))
