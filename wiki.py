import wikipediaapi

def wiki_info(req):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    wiki_page = wiki_wiki.page(req)
    try:
        if(wiki_page.exists):
            y = wiki_page.summary
            y.split()
            if (y[-1]==":"):
                x = "Summary does not exist"
            else:
                "".join(y)
                x=y
        else:
            x = "x_x 404 x_x"
    except:
        x = "x_x Something went Wrong x_x"

    return x

