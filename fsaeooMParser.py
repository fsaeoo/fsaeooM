import re

def fparse(fparser_arg):
    tokens = [
        "**",
        "\\\\",
        "__",
        "``",
        "^^"
    ]
    
    fparse_text = fparser_arg



##################################################################################
# FIRST : parse and delete comments
##################################################################################
   
    temp = re.sub("@~~.*?$\n", "", fparse_text, flags=re.MULTILINE)
    fparse_text = temp

##################################################################################
# SECOND : parse newlines
##################################################################################
    temp =  fparse_text.replace("\n", " <br> ")
    fparse_text = temp


#################################################################################
#   __     _______        _   
#  /_ |   |__   __|      | |  
#   | |      | | _____  _| |_ 
#   | |      | |/ _ \ \/ / __|
#   | |_     | |  __/>  <| |_ 
#   |_(_)    |_|\___/_/\_\\__|                          
#################################################################################                                  
                                      
                                   



#####################ITALIC#####################
    fparse_text = temp
    temp = re.sub("//\s", "</i>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("//", "<i>",temp, flags=re.MULTILINE)
    temp = re.sub("</i>", "</i > ",fparse_text, flags=re.MULTILINE)
#####################BOLD#####################
    fparse_text = temp
    temp = re.sub(";;\s", "</b>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub(";;", "<b>",temp, flags=re.MULTILINE)
    temp = re.sub("</b>", "</b > ",fparse_text, flags=re.MULTILINE)
#####################UNDERLINE#####################
    fparse_text = temp
    temp = re.sub("__\s", "</u>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("__", "<u>",temp, flags=re.MULTILINE)
    temp = re.sub("</u>", "</u > ",fparse_text, flags=re.MULTILINE)
#####################STRIKETHROUGH#####################
    fparse_text = temp
    temp = re.sub("``\s", "</s>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("``", "<s>",temp, flags=re.MULTILINE)
    temp = re.sub("</s>", "</s > ",fparse_text, flags=re.MULTILINE)
#####################CODE#####################
    fparse_text = temp
    temp = re.sub("~~\s", "</code>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("~~", "<code>",temp, flags=re.MULTILINE)
    temp = re.sub("</code>", "</code > ",fparse_text, flags=re.MULTILINE)
                

#################################################################################
#   ___      _    _                _ _                 
#  |__ \    | |  | |              | (_)                
#     ) |   | |__| | ___  __ _  __| |_ _ __   __ _ ___ 
#    / /    |  __  |/ _ \/ _` |/ _` | | '_ \ / _` / __|
#   / /_ _  | |  | |  __/ (_| | (_| | | | | | (_| \__ \
#  |____(_) |_|  |_|\___|\__,_|\__,_|_|_| |_|\__, |___/
#                                             __/ |    
#                                            |___/  
#################################################################################

#####################H6#####################
    fparse_text = temp
    temp = re.sub("#6#", "<h6>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("<h6>[\s|$|\n]", "</h6>",temp, flags=re.MULTILINE)
    temp = re.sub("<h6>.$", "</h6>",fparse_text, flags=re.MULTILINE)
    temp = re.sub("</h6>", "</h6> ",fparse_text, flags=re.MULTILINE)
    fparse_text = temp

#####################H5#####################
    fparse_text = temp
    temp = re.sub("#5#", "<h5>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("<h5>[\s|$|\n]", "</h5>",temp, flags=re.MULTILINE)
    temp = re.sub("<h5>.$", "</h5>",fparse_text, flags=re.MULTILINE)
    temp = re.sub("</h5>", "</h5> ",fparse_text, flags=re.MULTILINE)
    fparse_text = temp

#####################H4#####################
    fparse_text = temp
    temp = re.sub("#4#", "<h4>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("<h4>[\s|$|\n]", "</h4>",temp, flags=re.MULTILINE)
    temp = re.sub("<h4>.$", "</h4>",fparse_text, flags=re.MULTILINE)
    temp = re.sub("</h4>", "</h4> ",fparse_text, flags=re.MULTILINE)
    fparse_text = temp

#####################H3#####################
    fparse_text = temp
    temp = re.sub("#3#", "<h3>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("<h3>[\s|$|\n]", "</h3>",temp, flags=re.MULTILINE)
    temp = re.sub("<h3>.$", "</h3>",fparse_text, flags=re.MULTILINE)
    temp = re.sub("</h3>", "</h3> ",fparse_text, flags=re.MULTILINE)
    fparse_text = temp

#####################H2#####################
    fparse_text = temp
    temp = re.sub("#2#", "<h2>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("<h2>[\s|$|\n]", "</h2>",temp, flags=re.MULTILINE)
    temp = re.sub("<h2>.$", "</h2>",fparse_text, flags=re.MULTILINE)
    temp = re.sub("</h2>", "</h2> ",fparse_text, flags=re.MULTILINE)
    fparse_text = temp


#####################H1#####################
    fparse_text = temp
    temp = re.sub("#1#", "<h1>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("<h1>[\s|$|\n]", "</h1>",temp, flags=re.MULTILINE)
    temp = re.sub("<h1>.$", "</h1>",fparse_text, flags=re.MULTILINE)
    temp = re.sub("</h1>", "</h1> ",fparse_text, flags=re.MULTILINE)
    fparse_text = temp



#################################################################################
#   ____     _      _     _       
#  |___ \   | |    (_)   | |      
#    __) |  | |     _ ___| |_ ___ 
#   |__ <   | |    | / __| __/ __|
#   ___) |  | |____| \__ \ |_\__ \
#  |____(_) |______|_|___/\__|___/
#################################################################################      

    #####################BULLETLIST#####################          
    fparse_text = temp
    temp = re.sub("''", "<li>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("<li>[\s|$|\n]", "</li>", temp, flags=re.MULTILINE)
    temp = re.sub("</li>", "</li> ",fparse_text, flags=re.MULTILINE)
    fparse_text = temp
    














    return fparse_text
