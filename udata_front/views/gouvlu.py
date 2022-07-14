import logging


from udata_front import theme
from udata.i18n import I18nBlueprint
from udata.sitemap import sitemap


log = logging.getLogger(__name__)

blueprint = I18nBlueprint(
    "gouvlu",
    __name__,
    template_folder="../templates",
    static_folder="../static",
    static_url_path="/static/gouvfr",
)

# PAGE_CACHE_DURATION = 60 * 5  # in seconds

FAQ_URL_PATTERN = "https://github.com/freesoul/udata4-front/edit/master/udata_front/theme/gouvfr/templates/luxembourg-faq/{page_name}.html"


@blueprint.route("/faq/", defaults={"section": "home"})
@blueprint.route("/faq/<string:section>/")
def faq(section):
    return theme.render(
        "luxembourg-faq/{0}.html".format(section),
        page_name=section,
        url_pattern=FAQ_URL_PATTERN,
    )


@blueprint.route("/usage/")
def usage():
    return theme.render("luxembourg/usage.html")


@blueprint.route("/publishing/")
def publishing():
    return theme.render("luxembourg/publishing.html")


@blueprint.route("/strategy/")
def strategy():
    return theme.render("luxembourg/strategy.html")


@blueprint.route("/5yearplan/")
def fiveyearplan():
    return theme.render("luxembourg/5yearplan.html")


@blueprint.route("/docapi/")
def docapi():
    return theme.render("luxembourg/api.html")

@blueprint.route("/requesting/")
def requesting():
    return theme.render("luxembourg/requesting.html")


@sitemap.register_generator
def site_sitemap_urls():
    yield "gouvlu.faq_redirect", {}, None, "weekly", 1
    for section in ("citizen", "producer", "reuser", "developer", "system-integrator"):
        yield "gouvlu.faq_redirect", {"section": section}, None, "weekly", 0.7
    yield "gouvlu.usage_redirect", {}, None, "monthly", 0.2
    yield "gouvlu.publishing_redirect", {}, None, "monthly", 0.2
    yield "gouvlu.strategy_redirect", {}, None, "monthly", 0.2
