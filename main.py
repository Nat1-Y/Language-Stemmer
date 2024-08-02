import re
import suffix
import plural
import prefix


def stemmer(input):
    word = re.sub(r"[,.!?]", "", input)

    word = prefix.prefix(word)

    word = plural.plural(word)

    word = suffix.suffix(word)

    print(word)


stemmer('ላልተወሰነ')
stemmer('ላልተወሰነዎች')