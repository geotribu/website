# standard
import datetime

# 3rd party
from babel.dates import format_date
from geotribu_cli.utils.slugger import sluggy


def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """

    # create a jinja2 filter
    @env.filter
    def date_localized(in_date: datetime.date):
        "Localize a date using babel."
        return format_date(date=in_date, format="long", locale="fr_FR")

    @env.filter
    def slugger(in_str: str, replacer: str = "-"):
        "Text slugifier."
        return sluggy(text_to_slugify=in_str, replacer="-")
