from ckanext.gdi_userportal.logic.action.fetcher.prop_fetcher import PropFetcher


class PublisherFetcher(PropFetcher):
    @property
    def _prop_name() -> str:
        return "publisher_name"