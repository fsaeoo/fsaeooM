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
#   .o                    .                             .   
# o888                  .o8                           .o8   
#  888                .o888oo  .ooooo.  oooo    ooo .o888oo 
#  888                  888   d88' `88b  `88b..8P'    888   
#  888       o8o        888   888ooo888    Y888'      888   
#  888       `"'        888 . 888    .o  .o8"'88b     888 . 
# o888o      o8o        "888" `Y8bod8P' o88'   888o   "888" 
#################################################################################                                  
                                      
                                   

##################################################################################
# THIRD : parse styles
##################################################################################

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
#   .oooo.                 oooo                                  .o8   o8o                                  
# .dP""Y88b                `888                                 "888   `"'                                  
#       ]8P'                888 .oo.    .ooooo.   .oooo.    .oooo888  oooo  ooo. .oo.    .oooooooo  .oooo.o 
#     .d8P'                 888P"Y88b  d88' `88b `P  )88b  d88' `888  `888  `888P"Y88b  888' `88b  d88(  "8 
#   .dP'          o8o       888   888  888ooo888  .oP"888  888   888   888   888   888  888   888  `"Y88b.  
# .oP     .o      `"'       888   888  888    .o d8(  888  888   888   888   888   888  `88bod8P'  o.  )88b 
# 8888888888      o8o      o888o o888o `Y8bod8P' `Y888""8o `Y8bod88P" o888o o888o o888o `8oooooo.  8""888P' 
#                 `"'                                                                   d"     YD           
#                                                                                       "Y88888P'     
#################################################################################
#####################H6#####################
    fparse_text = temp
    temp = re.sub("######", "<h6>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("<h6>[\s|$|\n]", "</h6>",temp, flags=re.MULTILINE)
    temp = re.sub("<h6>.$", "</h6>",fparse_text, flags=re.MULTILINE)
    temp = re.sub("</h6>", "</h6> ",fparse_text, flags=re.MULTILINE)
    fparse_text = temp

#####################H5#####################
    fparse_text = temp
    temp = re.sub("#####", "<h5>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("<h5>[\s|$|\n]", "</h5>",temp, flags=re.MULTILINE)
    temp = re.sub("<h5>.$", "</h5>",fparse_text, flags=re.MULTILINE)
    temp = re.sub("</h5>", "</h5> ",fparse_text, flags=re.MULTILINE)
    fparse_text = temp

#####################H4#####################
    fparse_text = temp
    temp = re.sub("####", "<h4>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("<h4>[\s|$|\n]", "</h4>",temp, flags=re.MULTILINE)
    temp = re.sub("<h4>.$", "</h4>",fparse_text, flags=re.MULTILINE)
    temp = re.sub("</h4>", "</h4> ",fparse_text, flags=re.MULTILINE)
    fparse_text = temp

#####################H3#####################
    fparse_text = temp
    temp = re.sub("###", "<h3>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("<h3>[\s|$|\n]", "</h3>",temp, flags=re.MULTILINE)
    temp = re.sub("<h3>.$", "</h3>",fparse_text, flags=re.MULTILINE)
    temp = re.sub("</h3>", "</h3> ",fparse_text, flags=re.MULTILINE)
    fparse_text = temp

#####################H2#####################
    fparse_text = temp
    temp = re.sub("##", "<h2>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("<h2>[\s|$|\n]", "</h2>",temp, flags=re.MULTILINE)
    temp = re.sub("<h2>.$", "</h2>",fparse_text, flags=re.MULTILINE)
    temp = re.sub("</h2>", "</h2> ",fparse_text, flags=re.MULTILINE)
    fparse_text = temp


#####################H1#####################
    fparse_text = temp
    temp = re.sub("#", "<h1>",fparse_text, flags=re.MULTILINE)
    fparse_text = re.sub("<h1>[\s|$|\n]", "</h1>",temp, flags=re.MULTILINE)
    temp = re.sub("<h1>.$", "</h1>",fparse_text, flags=re.MULTILINE)
    temp = re.sub("</h1>", "</h1> ",fparse_text, flags=re.MULTILINE)
    fparse_text = temp














    return fparse_text
