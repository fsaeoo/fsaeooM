from flask import *
import fsaeoMParser


app = Flask(__name__)
@app.route("/")
def homepage(): 
    template =fsaeoMParser.fparse("""
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

# print(fsaeoMParser.fparse("""@~~ comment <br>
#      newline here //italic//
#     ;;bold;; """))
