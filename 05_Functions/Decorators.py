def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
           print("<{0}>{1}</{0}>".format(tag_name, func(name)))

        return func_wrapper

    return tags_decorator


@tags('div')
@tags('p')
def greeting_with_tags(name):
    print("Hello, {0}!".format(name))


greeting_with_tags('John')


def greeting_with_div_p(name):
    print( "Hello, {0}!".format(name))

greeting_with_div_p('John')